#!/usr/bin/env python3

# This script converts MeCab analysis result to Juman++ training data
import sys
import csv


def escape(x):
    if '"' in x or ',' in x:
        replaced = x.replace('"', '""')
        return f'"{replaced}"'
    else:
        return x


def process(fd):
    for line in csv.reader(fd):
        if len(line) == 1:
            print('EOS')
            continue

        surf = line[0]
        fparts = line[1:]
        if len(fparts) < 10:
            print(line.rstrip(), file=sys.stderr)
            fparts.append(surf)
            fparts.append(surf)
            fparts.append(surf)
            for _ in range(17 - 8):
                fparts.append('')
            print(','.join(fparts))
        else:
            featutres = [
                surf,
                fparts[0],
                fparts[1],
                fparts[2],
                fparts[3],
                fparts[4],
                fparts[5],
                fparts[6],
                fparts[7],
                fparts[8],
                fparts[9],
                fparts[10],
                fparts[11],
                fparts[12],
                fparts[19],
                fparts[24],
                fparts[25],
                fparts[26]
            ]
            print(",".join(f'{escape(x)}' for x in featutres))


if __name__ == '__main__':
    files = sys.argv[1:]
    for file in files:
        with open(file, 'rt', encoding='utf-8', newline='') as fd:
            process(fd)
