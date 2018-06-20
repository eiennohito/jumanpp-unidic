#!/usr/bin/env python3

# This script convers BCCWJ data to MeCab data for ... analysis
import sys
import csv

def process(fd):
    first = True

    for parts in csv.reader(fd, dialect='excel-tab'):
        bos = parts[9]
        lemma = parts[12]
        lForm = parts[13]
        eng = parts[14]
        kind = parts[15]
        pos = parts[16]
        cType = parts[17] or '*'
        cForm = parts[18] or '*'
        writForm = parts[21]
        writSurf = parts[22]
        pron = parts[24]

        posParts = pos.split('-')
        pos2 = pos3 = pos4 = '*'
        if len(posParts) == 1:
            pos1 = pos
        elif len(posParts) == 2:
            pos1 = posParts[0]
            pos2 = posParts[1]
        elif len(posParts) == 3:
            pos1 = posParts[0]
            pos2 = posParts[1]
            pos3 = posParts[2]
        else:
            pos1 = posParts[0]
            pos2 = posParts[1]
            pos3 = posParts[2]
            pos4 = posParts[3]

        if bos == 'B' and not first:
            print('EOS')

        if eng:
            lemma = f"{lemma}-{eng}"

        features = [
            pos1,
            pos2,
            pos3,
            pos4,
            cType,
            cForm,
            lForm,
            lemma,
            writSurf,
            pron,
            '*'
        ]

        featureString = ",".join(x or '*' for x in features)
        print(f'{writSurf}\t{featureString}')
        first = False


if __name__ == '__main__':
    files = sys.argv[1:]
    for file in files:
        with open(file, 'rt', encoding='utf-8', newline='') as fd:
            process(fd)
            print('EOS')
