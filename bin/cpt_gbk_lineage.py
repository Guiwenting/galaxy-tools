#!/usr/bin/env python
import argparse
import logging
logging.basicConfig(level=logging.INFO)


__doc__ = """
Gene Renumbering Tool
=====================

Renumber genes in a genome
"""


def lineage(genbank_files=None, **kwargs):
    from Bio import SeqIO
    rows = []
    for genbank_file in genbank_files:
        records = list(SeqIO.parse(genbank_file, "genbank"))
        for record in records:
            id = record.id
            if '.' in id:
                id = id.split('.')[0]
            try:
                rows.append([id] + record.annotations['taxonomy'])
            except:
                rows.append([id])
                pass
    return rows

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract lineage information from genbank files')
    parser.add_argument('genbank_files', type=file, nargs='+', help='Genbank file')
    parser.add_argument('--version', action='version', version='0.1')
    args = parser.parse_args()
    print '\t'.join(['# ID'] + map(str, range(10)))
    for line in lineage(**vars(args)):
        print '\t'.join(line)