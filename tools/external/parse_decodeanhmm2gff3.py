#!/usr/bin/env python
import sys
import uuid
import logging
logging.basicConfig(level=logging.INFO)
from BCBio import GFF
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.Alphabet import IUPAC
log = logging.getLogger(__name__)


def convert(data=None):
    record = None
    length = None
    count = 1

    if data is None:
        data = sys.stdin

    for line in data:
        if line.startswith('>'):
            if record is not None and len(record.features) > 0:
                yield [record]

            header = line.split(' ')[0].strip()[1:]
            record = SeqRecord(
                Seq("ACTG", IUPAC.IUPACUnambiguousDNA),
                id=header
            )

        if line.startswith('%len'):
            length = int(line[5:].strip())

        if line.startswith('%pred'):
            pred = line.strip()
            pred = pred[pred.index(': ') + 2:]
            # %pred NB(0): i 1 8, M 9 28, o 29 44
            regions = pred.split(', ')

            # Ignore regions that are boring
            if len(regions) == 1:
                continue

            if regions[0].startswith('i'):
                n_dir = 'in'
            else:
                n_dir = 'out'

            if regions[-1].startswith('i'):
                c_dir = 'in'
            else:
                c_dir = 'out'

            # Q7TNJ0  UniProtKB   Chain   1   470 .   .   .   ID=PRO_0000072585;Note=Dendritic cell-specific transmembrane protein
            feature = SeqFeature(
                FeatureLocation(1, length),
                type="Chain",
                strand=1,
                qualifiers={
                    'ID': 'tmhmm_tmd_%s-%s' % (count, str(uuid.uuid4())),
                    'Description': 'Transmembrane protein',
                    'Note': 'Transmembrane protein - N %s C %s' % (n_dir, c_dir),
                    'Target': header,
                }
            )
            count += 1
            for region in regions:
                (region_type, start, end) = region.strip().split(' ')
                qualifiers = {
                    'source': 'TMHMM',
                    # 'evidence': 'ECO:0000255',
                }
                # Q7TNJ0  UniProtKB   Topological domain  1   33  .   .   .   Note=Cytoplasmic;evidence=ECO:0000255
                # Q7TNJ0  UniProtKB   Transmembrane   34  54  .   .   .   Note=Helical;evidence=ECO:0000255
                # Q7TNJ0  UniProtKB   Topological domain  55  55  .   .   .   Note=Extracellular;evidence=ECO:0000255
                if region_type == 'i':
                    qualifiers.update({
                        'Note': 'Cytoplasmic',
                    })
                elif region_type == 'M':
                    qualifiers.update({
                        'Note': 'Helical',
                    })
                elif region_type == 'o':
                    qualifiers.update({
                        'Note': 'Extracellular',
                    })

                sub_feat = SeqFeature(
                    FeatureLocation(int(start) - 1, int(end)),
                    type="Transmembrane" if region_type == 'M' else "Topological domain",
                    strand=1,
                    qualifiers=qualifiers,
                )
                feature.sub_features.append(sub_feat)

            record.features.append(feature)


if __name__ == '__main__':
    for record in convert():
        GFF.write(record, sys.stdout)
