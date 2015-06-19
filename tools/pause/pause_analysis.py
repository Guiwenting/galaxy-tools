#!/usr/bin/env python
"""Extract read start from BAM files to Wig format for PAUSE.

Usage:
    bam_to_wiggle.py <BAM file>

"""
import os
import sys
import bx.wiggle
import numpy
import pysam
from Bio import SeqIO
from galaxygetopt.ggo import GalaxyGetOpt as GGO


def get_data(wig_handle):
    data = []
    for row in bx.wiggle.Reader(wig_handle):
        data.append((row[1], row[2]))

    reshaped = numpy.array(data, dtype=numpy.int)
    return reshaped


def main(starts_f=None, starts_r=None, bam_file=None, genome=None, cov_f=None, cov_r=None, **kwd):
    data_f = get_data(starts_f)
    data_r = get_data(starts_r)
    dcov_f = get_data(cov_f)
    dcov_r = get_data(cov_r)
    (max_f, min_f) = peakdet(data_f[:, 1], 40)
    (max_r, min_r) = peakdet(data_r[:, 1], 40)

    records = list(SeqIO.parse(genome, "fasta"))

    (report, rrl) = identify_regions(max_f, max_r, data_f, data_r, dcov_f, dcov_r, len(records[0].seq))

    # 2D table into tsv
    repeat_region_list = ['#start\tend']
    for r in rrl:
        repeat_region_list.append('\t'.join([str(int(x)) for x in r]))

    return (max_f, max_r, '\n'.join(report), '\n'.join(repeat_region_list))


def identify_regions(peak_f, peak_r, data_f, data_r, cov_f, cov_r, gl=0):
    """
        Function to identify double coverage regions in a genome based on some inputs:

        1. peaks (f/r)
        2. Coverage data (f/r)
        3. raw data (f/r)


        There are three possible answers to this question

        1) We have a long region 10-20kb, of double coverage
        2) We have a short region <1kb of double coverage
        3) We fail to identify any such regions

        We can generalise cases 1 and 2 into "a region with ~1.5x+ coverage
        compared to rest of genome", and then separate the cases based on length
        of said region
    """

    # First determine breakpoints
    breaks = sorted([0] + [p[0] for p in peak_f] + [p[0] for p in peak_r] + [gl])
    # Then we'll figure out coverage along each region (will make calculating
    # coverage easier/faster later)
    coverage_data = {}
    for i in range(len(breaks) - 1):
        region_start = breaks[i]
        region_end = breaks[i+1]
        (acov_f, acov_r, acov_avg) = get_coverage(cov_f, cov_r, breaks[i], breaks[i+1])
        coverage_data['%s-%s' % (region_start, region_end)] = acov_avg
        #print "%20s%20s%20s%20s%20s" % (region_start, region_end, acov_f, acov_r, acov_avg)

    report = [
        '# PAUSE Report',
        '',
        'This report was automatically generated by the PAUSE software. It merely records some information about the analysis process',
        '',
        'These regions were examined: ',
        ''
    ]

    findings = ['## Process', '']
    conclusions = ['## Conclusions', '']
    recommendations = ['## Recommendations', '']
    concl_base = []
    # For every pair of peaks
    for pf in peak_f[:, 0]:
        for pr in peak_r[:, 0]:
            # Our hypothesis is that the region between the two* will be double
            # the coverage of the rest of the genome. However, this hypothesis
            # does not hold for regions which make up a significant portion of
            # the genome (e.g. a small region is "outside" and averaged against
            # the rest of the region which is "inside"), so we have to discount regions where outside < inside
            #
            # * (moving right from pf, possibly wrapping around end of genome
            # to get to pr),

            if (pf < pr and pr-pf < (.5 * gl)) or \
                    (pf > pr and (breaks[-1] - pf + pr) < (.5 * gl)):
                report.append('- %s..%s' % (pf, pr))
                if pf < pr:
                    between = get_coverage_for_region(coverage_data, breaks, pf, pr)
                    outside = get_coverage_for_region(coverage_data, breaks, 0, pf) + \
                                get_coverage_for_region(coverage_data, breaks, pr, breaks[-1] ) # right to end
                else:
                    outside = get_coverage_for_region(coverage_data, breaks, pr, pf)
                    between = get_coverage_for_region(coverage_data, breaks, 0, pr) + \
                                get_coverage_for_region(coverage_data, breaks, pf, breaks[-1] ) # right to end

                if between > (outside * 1.75):
                    findings.append(' - Found possible region on [%s..%s], where the average coverage (%s) is larger than the rest of the genome (%s)' % (pf, pr, between, outside ))
                    conclusions.append(' - Region [%s..%s] is likely candidate for a repeat_region' % (pf, pr))
                    concl_base.append([pf, pr])
                else:
                    findings.append(' - Discounted region [%s..%s], as average coverage (%s) was not significantly larger than the rest of the genome (%s)' % (pf, pr, between, outside ))
            else:
                findings.append(' - Discounted region [%s..%s] due to size of region as %% of genome' % (pf, pr))


    if len(conclusions) == 3:
        recommendations.append('Recommend re-opening the genome at base %s' % concl_base[0][0])
    else:
        recommendations.append('Multiple possible regions were found, you should manually inspect these regions to narrow them down to a single correct location for a repeat')

    return (report + [''] + findings + [''] + conclusions + [''] + recommendations + [''], concl_base)


def get_coverage_for_region(coverage_data, breaks, start, end):
    """Approximately calculate coverage over a region

    Makes use of the coverage data structure, and break list.
    """
    idx_s = breaks.index(start)
    idx_e = breaks.index(end)
    value = 0
    # From the start to the end in break list (should be sorted, hell will
    # break loose if it isn't)
    for i in range(idx_s, idx_e):
        # Grab the relevant regions
        # But multiply by length of region to get back ~appx total area
        value += coverage_data['%s-%s' % (breaks[i], breaks[i+1])] * (breaks[i+1] - breaks[i])
    # Which will then be re-averaged down by total region requested
    return value / (end - start)


def get_coverage(data_f, data_r, start, end):
    f_cov = numpy.mean(data_f[start:end], axis=0)[1]
    r_cov = numpy.mean(data_r[start:end], axis=0)[1]
    return (f_cov, r_cov, (f_cov+r_cov)/2)


def peakdet(v, delta, x=None):
    # https://gist.github.com/endolith/250860
    """
    Converted from MATLAB script at http://billauer.co.il/peakdet.html

    Returns two arrays

    function [maxtab, mintab]=peakdet(v, delta, x)
    %PEAKDET Detect peaks in a vector
    %        [MAXTAB, MINTAB] = PEAKDET(V, DELTA) finds the local
    %        maxima and minima ("peaks") in the vector V.
    %        MAXTAB and MINTAB consists of two columns. Column 1
    %        contains indices in V, and column 2 the found values.
    %
    %        With [MAXTAB, MINTAB] = PEAKDET(V, DELTA, X) the indices
    %        in MAXTAB and MINTAB are replaced with the corresponding
    %        X-values.
    %
    %        A point is considered a maximum peak if it has the maximal
    %        value, and was preceded (to the left) by a value lower by
    %        DELTA.

    % Eli Billauer, 3.4.05 (Explicitly not copyrighted).
    % This function is released to the public domain; Any use is allowed.

    """
    maxtab = []
    mintab = []

    if x is None:
        x = numpy.arange(len(v))

    v = numpy.asarray(v)

    if len(v) != len(x):
        sys.exit('Input vectors v and x must have same length')

    if not numpy.isscalar(delta):
        sys.exit('Input argument delta must be a scalar')

    if delta <= 0:
        sys.exit('Input argument delta must be positive')

    mn, mx = numpy.Inf, -numpy.Inf
    mnpos, mxpos = numpy.NaN, numpy.NaN

    lookformax = True

    for i in numpy.arange(len(v)):
        this = v[i]
        if this > mx:
            mx = this
            mxpos = x[i]
        if this < mn:
            mn = this
            mnpos = x[i]

        if lookformax:
            if this < mx-delta:
                maxtab.append((mxpos, mx))
                mn = this
                mnpos = x[i]
                lookformax = False
        else:
            if this > mn+delta:
                mintab.append((mnpos, mn))
                mx = this
                mxpos = x[i]
                lookformax = True

    return numpy.array(maxtab, dtype=numpy.int), numpy.array(mintab,
                                                             dtype=numpy.int)


if __name__ == "__main__":
    opts = GGO(
        options=[
            ['genome', 'Genome (for length)',
             {'required': True, 'validate': 'File/Input'}],
            ['starts_f', '+ strand start wig data',
             {'required': True, 'validate': 'File/Input'}],
            ['starts_r', '- strand start wig data',
             {'required': True, 'validate': 'File/Input'}],
            ['cov_f', '+ strand start wig data',
             {'required': True, 'validate': 'File/Input'}],
            ['cov_r', '- strand start wig data',
             {'required': True, 'validate': 'File/Input'}],
            ['bam_file', 'Bam File',
             {'required': True, 'validate': 'File/Input'}],
        ],
        outputs=[
            [
                'wig_f',
                '+ strand PAUSE wig results',
                {
                    'validate': 'File/Output',
                    'required': True,
                    'default': 'wig.pause.f',
                    'data_format': 'text/plain',
                    'default_format': 'TXT',
                }
            ],
            [
                'wig_r',
                '- strand PAUSE wig results',
                {
                    'validate': 'File/Output',
                    'required': True,
                    'default': 'wig.pause.r',
                    'data_format': 'text/plain',
                    'default_format': 'TXT',
                }
            ],
            [
                'pause_report',
                'PAUSE Report',
                {
                    'validate': 'File/Output',
                    'required': True,
                    'default': 'pause_report',
                    'data_format': 'text/plain',
                    'default_format': 'TXT',
                }
            ],
            [
                'repeat_region_list',
                'Repeat Region List',
                {
                    'validate': 'File/Output',
                    'required': True,
                    'default': 'pause_repeat_regions',
                    'data_format': 'text/plain',
                    'default_format': 'TXT',
                }

            ]
        ],
        defaults={
            'appid': 'edu.tamu.cpt.pause2.analysis',
            'appname': 'PAUSE2 Analaysis',
            'appvers': '0.1',
            'appdesc': 'run PAUSE analysis',
        },
        tests=[],
        doc=__doc__
    )
    options = opts.params()
    (f, r, pr, rrl) = main(**options)

    if not os.path.exists(options['bam_file'].name + ".bai"):
        pysam.index(options['bam_file'].name)
    sam_reader = pysam.Samfile(options['bam_file'].name, "rb")
    sizes = zip(sam_reader.references, sam_reader.lengths)
    regions = [(name, 0, length) for name, length in sizes]
    header = """track type=wiggle_0 name=%s visibility=full
variableStep chrom=%s\n"""

    data_f = header % ('highlights_f', regions[0][0])
    for row in f:
        data_f += ' '.join(map(str, row)) + "\n"

    data_r = header % ('highlights_r', regions[0][0])
    for row in r:
        data_r += ' '.join(map(str, row)) + "\n"

    from galaxygetopt.outputfiles import OutputFiles
    off = OutputFiles(name='wig_f', GGO=opts)
    off.CRR(data=data_f)
    ofr = OutputFiles(name='wig_r', GGO=opts)
    ofr.CRR(data=data_r)
    ofrp = OutputFiles(name='pause_report', GGO=opts)
    ofrp.CRR(data=pr)
    ofrp = OutputFiles(name='repeat_region_list', GGO=opts)
    ofrp.CRR(data=rrl)