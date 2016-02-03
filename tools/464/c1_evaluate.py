#!/usr/bin/env python
import argparse
from BCBio import GFF
from gff3 import feature_lambda, feature_test_type
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

from guanine import GuanineClient
g = GuanineClient(
    url='https://cpt.tamu.edu/gses/submit',
    # admin api key
    api_key='7b0634b429df48da9b81bfd8d54bece6',
    # BICH 464 2016 Spring
    id='faff993c-caaf-11e5-80c7-8b44f2907817'
)



def validate(ogs, user_gff3, user_email, offset=213):
    comp = {}
    for rec in GFF.parse(ogs):
        for feature in feature_lambda(
            rec.features,
            feature_test_type,
            {'type': 'CDS'},
            subfeatures=True,
        ):
            if feature.strand > 0:
                offset_end = int(feature.location.end)
            else:
                offset_end = int(feature.location.start)

            comp[offset_end] = feature
    max_score = len(comp)

    user = {}
    for rec in GFF.parse(user_gff3):
        for feature in feature_lambda(
            rec.features,
            feature_test_type,
            {'type': 'CDS'},
            subfeatures=True,
        ):
            if feature.strand > 0:
                offset_end = int(feature.location.end) + offset
            else:
                offset_end = int(feature.location.start) + offset
            user[offset_end] = feature

    results = []

    for user_annotation in sorted(user.keys()):
        if user_annotation in comp:
            # User successfully annotated gene
            # print comp[user_annotation]
            # good.append(user_annotation)
            ogs_feature = comp[user_annotation]
            usr_feature = user[user_annotation]
            if ogs_feature.location.start == usr_feature.location.start + offset and \
                    ogs_feature.location.end == usr_feature.location.end + offset:
                # Success!
                results.append({
                    'points': 1,
                    'message': 'Correct',
                    'stop': user_annotation,
                })
            else:
                results.append({
                    'points': .5,
                    'message': 'Wrong start codon',
                    'stop': user_annotation,
                })
            del comp[user_annotation]
        else:
            # User annotated a non-existent gene
            results.append({
                'points': 0,
                'message': 'Not an actual gene, according to the official gene set',
                'stop': user_annotation,
            })

    for leftover in comp.keys():
        results.append({
            'points': -.5,
            'message': 'Missed a gene in the official gene set',
            'stop': leftover,
        })

    score = sum(x['points'] for x in results)
    print 'Final score: %s / %s' % (score, max_score)
    print

    # Submit score to GUANINE
    g.submit(user_email, 'C1', float(float(score) / max_score))

    for x in results:
        print 'Feature ending with stop codon: {stop}; Points: {points}; Message {message}'.format(**x)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='verify against expectations')
    parser.add_argument('ogs', type=file, help='GFF3 annotations')
    parser.add_argument('user_gff3', type=file, help='GFF3 annotations')
    parser.add_argument('user_email', help='User email')
    args = parser.parse_args()
    validate(**vars(args))
