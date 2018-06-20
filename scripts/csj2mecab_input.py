#!/usr/bin/env python3

# This script convers BCCWJ data to MeCab data for ... analysis
import sys
import csv


def process(fd):
    length = 0
    prevPhrId = ""

    for parts in csv.reader(fd, dialect='excel-tab'):

        if len(parts) < 12:
            continue

        id = parts[3]
        xSurf = parts[5]
        writSurf = parts[7]
        lemmaRd = parts[8]
        lemma = parts[9]
        pos1 = parts[11]

        if '(' in xSurf or ')' in xSurf:
            continue

        idParts = id.split(' ')
        phrId = idParts[0]

        if prevPhrId != phrId and length > 8:
            print('EOS')
            length = 0

        prevPhrId = phrId
        length += 1

        features = [
            pos1,
            '*',
            '*',
            '*',
            '*',
            '*',
            lemmaRd,
            '*',
            '*'
        ]

        featureString = ",".join(x or '*' for x in features)
        print(f'{writSurf}\t{featureString}')


if __name__ == '__main__':
    files = sys.argv[1:]
    for file in files:
        with open(file, 'rt', encoding='utf-8', newline='') as fd:
            process(fd)
            print('EOS')
