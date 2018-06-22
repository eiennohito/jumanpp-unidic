#!/usr/bin/env python3

# This script converts MeCab analysis result to Juman++ training data
import sys
import csv
import random


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

HIRAGANA = 'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろわをんーゎゐゑゕゖゔゝゞ・「」。、'
FULL_KATA = 'ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロワヲンーヮヰヱヵヶヴヽヾ・「」。、'

KATA_TO_HIRA = str.maketrans(FULL_KATA, HIRAGANA)


class Unidic(object):
    def __init__(self):
        self.lookup = {}

    @staticmethod
    def makeKey(fparts):
        pos1 = fparts[0] or '*'
        pos2 = fparts[1] or '*'
        pos3 = fparts[2] or '*'
        pos4 = fparts[3] or '*'
        cType = fparts[4] or '*'
        cForm = fparts[5] or '*'
        lForm = fparts[6] or '*'
        lemma = fparts[7] or '*'
        pron = fparts[9] or '*'
        pronBase = fparts[11] or '*'
        goshu = fparts[12] or '*'
        type = fparts[19] or '*'
        aType = fparts[24] or '*'
        aConType = fparts[25] or '*'
        aModType = fparts[26] or '*'

        return (
            pos1,
            pos2,
            pos3,
            pos4,
            cType,
            cForm,
            lForm,
            lemma,
            pron,
            pronBase,
            goshu,
            type,
            aType,
            aConType,
            aModType
        )

    def add(self, fparts):
        if len(fparts) < 29:
            return

        orth = fparts[8]
        orthBase = fparts[10]

        key = Unidic.makeKey(fparts)

        rds = self.lookup.setdefault(key, [])
        val = (orth, orthBase)
        if orth not in rds:
            rds.append(val)

    def get(self, fparts):
        if len(fparts) < 27:
            return None

        orth = fparts[8]
        orthBase = fparts[10]
        key = Unidic.makeKey(fparts)
        retval = orth, orthBase

        items = self.lookup.get(key, None)
        if items is None:
            return None

        notMe = [item for item in items if item != retval]

        if len(notMe) == 0:
            return None

        return random.choice(notMe)

    def deleteSingles(self):
        todelete = []
        for k, v in self.lookup.items():
            if len(v) == 1:
                todelete.append(k)

        for i in todelete:
            self.lookup.pop(i)


def readUnidic(file):
    unidic = Unidic()
    with open(file, 'rt', newline='', encoding='utf-8') as fd:
        for line in csv.reader(fd):
            unidic.add(line[4:])

    unidic.deleteSingles()

    return unidic


def makeDict(fields):
    res = {}
    for i in range(len(fields)):
        val = fields[i]
        if val != '*' and len(val) > 0 and FIELD_NAMES[i] in TRAIN_FIELDS:
            res[FIELD_NAMES[i]] = val
    return res


def writePart(lines, fd, unidic):
    for line in lines:
        fparts = line[1:]
        dic = makeDict(fparts)
        surf = line[0]
        if unidic is not None:
            changed = unidic.get(fparts)
            if changed is not None:
                surf = changed[0]
                dic['orth'] = surf
                dic['orthBase'] = changed[1]

        fd.write('\t')
        fd.write(surf)
        for k in dic:
            v = dic[k]
            fd.write('\t')
            fd.write(k)
            fd.write(':')
            fd.write(v)
        fd.write('\n')
    fd.write('\n')


def writeFull(lines, fd, unidic):
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

        if unidic is not None:
            changed = unidic.get(fparts)
            if changed is not None:
                orth, orthBase = changed
                featutres[0] = orth
                featutres[9] = orth
                featutres[11] = orthBase
        print(",".join(escape(x) for x in featutres), file=fd)
    print("EOS", file=fd)


def process(fd, full, part, unidic):
    lines = []
    is_full = True
    for line in csv.reader(fd):
        if len(line) == 1:
            if is_full:
                writeFull(lines, full, None)
                writeFull(lines, full, unidic)
            else:
                writePart(lines, part, None)
                writePart(lines, part, unidic)
            lines.clear()
            is_full = True
            continue

        lines.append(line)

        if len(line) < 10:
            is_full = False


def main():
    unidic = readUnidic(sys.argv[1])
    files = sys.argv[2:]
    for file in files:
        full_name = file + ".full-tdata"
        part_name = file + ".part-tdata"
        with open(file, 'rt', encoding='utf-8', newline='') as fd:
            with open(full_name, 'wt', encoding='utf-8') as full:
                with open(part_name, 'wt', encoding='utf-8') as part:
                    process(fd, full, part, unidic)


if __name__ == '__main__':
    main()
