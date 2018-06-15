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


FIELD_NAMES = [
    "pos1",
    "pos2",
    "pos3",
    "pos4",
    "cType",
    "cForm",
    "lForm",
    "lemma",
    "orth",
    "pron",
    "orthBase",
    "pronBase",
    "goshu",
    "iType",
    "iForm",
    "fType",
    "fForm",
    "iConType",
    "fConType",
    "type",
    "kana",
    "kanaBase",
    "form",
    "formBase",
    "aType",
    "aConType",
    "aModType",
    "lid",
    "lemma_id",
]

TRAIN_FIELDS = {"pos1", "pos2", "pos3", "pos4", "cType", "cForm", "lForm", "lemma", "orth", "pron", "orthBase",
                "pronBase", "goshu", "type", "aType", "aConType", "aModType"}


def makeDict(fields):
    res = {}
    for i in range(len(fields)):
        val = fields[i]
        if val != '*' and len(val) > 0 and FIELD_NAMES[i] in TRAIN_FIELDS:
            res[FIELD_NAMES[i]] = val
    return res


def writePart(lines, fd):
    for line in lines:
        dic = makeDict(line[1:])
        fd.write('\t')
        fd.write(line[0])
        for k in dic:
            v = dic[k]
            fd.write('\t')
            fd.write(k)
            fd.write(':')
            fd.write(v)
        fd.write('\n')
    fd.write('\n')


def writeFull(lines, fd):
    for line in lines:
        surf = line[0]
        fparts = line[1:]
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
        print(",".join(escape(x) for x in featutres), file=fd)
    print("EOS", file=fd)


def process(fd, full, part):
    lines = []
    is_full = True
    for line in csv.reader(fd):
        if len(line) == 1:
            if is_full:
                writeFull(lines, full)
            else:
                writePart(lines, part)
            lines.clear()
            is_full = True
            continue

        lines.append(line)

        if len(line) < 10:
            is_full = False


def main():
    files = sys.argv[1:]
    for file in files:
        full_name = file + ".full-tdata"
        part_name = file + ".part-tdata"
        with open(file, 'rt', encoding='utf-8', newline='') as fd:
            with open(full_name, 'wt', encoding='utf-8') as full:
                with open(part_name, 'wt', encoding='utf-8') as part:
                    process(fd, full, part)


if __name__ == '__main__':
    main()
