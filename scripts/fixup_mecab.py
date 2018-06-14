#!/usr/bin/env python3

# This script converts MeCab analysis result to Juman++ training data
import sys
import csv

def process(fd):
    for line in fd:
        if line == 'EOS\n':
            print('EOS')
            continue

        p1s = line.rstrip().split('\t')
        surf = p1s[0]
        feats = p1s[1]
        fparts = feats.split(',')
        if len(fparts) < 10:
            print(line.rstrip(), file=sys.stderr)
            fparts.append(surf)
            fparts.append(surf)
            fparts.append(surf)
            for _ in range(17 - 8):
                fparts.append('')
            print(','.join(fparts))

        else:
            print(f"{surf},{feats}")


if __name__ == '__main__':
    files = sys.argv[1:]
    for file in files:
        with open(file, 'rt', encoding='utf-8') as fd:
            process(fd)