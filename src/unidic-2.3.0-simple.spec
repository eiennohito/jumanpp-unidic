field 1 surface string trie_index align 4
# fields 2-4 are for mecab 
field 5 pos1 string align 5 empty "*"
field 6 pos2 string align 5 empty "*"
field 7 pos3 string align 5 empty "*"
field 8 pos4 string align 5 empty "*"
field 9 cType string align 5 empty "*"
field 10 cForm string align 5 empty "*"
field 11 lForm string align 4 empty "*"
field 12 lemma string storage surface empty "*"
field 13 orth string storage surface empty "*"
field 14 pron string storage lForm empty "*"
field 15 orthBase string storage surface empty "*"
field 16 pronBase string storage lForm empty "*"
field 17 goshu string align 3 empty "*"
field 18 iType string align 3 empty "*"
field 19 iForm string align 3 empty "*"
field 20 fType string align 3 empty "*"
field 21 fForm string align 3 empty "*"
field 22 iConType string align 3 empty "*"
field 23 fConType string align 3 empty "*"
field 24 type string align 3 empty "*"
field 25 kana string storage lForm empty "*"
field 26 kanaBase string storage lForm empty "*"
field 27 form string storage lForm empty "*"
field 28 formBase string storage lForm empty "*"
field 29 aType string align 6 empty "*"
field 30 aConType string align 5 empty "*"
field 31 aModType string align 5 empty "*"
field 32 lid string align 4 empty "*"
field 33 lemma_id string align 3 empty "*"

feature nodeCharType = codepoint_type 0
feature nextCharType = codepoint_type 1
feature charPlus1 = codepoint 1
feature charPlus2 = codepoint 2

unk catchall template row 1: single FAMILY_ANYTHING

ngram [surface]
ngram [pos1]
ngram [pos1, pos2]
ngram [pos1, pos2, pos3]
ngram [pos1, pos2, pos3, pos4]
ngram [cType]
ngram [cType, cForm]
ngram [cForm]
ngram [pos1, cType]
ngram [pos1, cType, cForm]
ngram [pos1, pos2, cType, cForm]
ngram [lemma]
ngram [lForm]
ngram [orth]
ngram [orthBase]
ngram [pron]
ngram [pronBase]

ngram [aType]
ngram [aConType]
ngram [aModType]
ngram [goshu]
ngram [type]
ngram [goshu, type, pos1]

ngram [pron, aType]

ngram [pos1, pos2, cType, cForm, charPlus1]
ngram [pos1, pos2, cType, cForm, charPlus2]
ngram [pos1, pos2, cType, cForm, charPlus1, charPlus2]
ngram [pos1, nodeCharType, nextCharType]

ngram [pos1][pos1]
ngram [pos1, pos2][pos1]
ngram [pos1, pos2, pos3, pos4][pos1]
ngram [pos1, pos2, cType, cForm][pos1]
ngram [lemma, pos1, pos2, cType, cForm][pos1]
ngram [pos1][pos1, pos2]
ngram [pos1, pos2][pos1, pos2]
ngram [pos1, pos2, pos3, pos4][pos1, pos2]
ngram [pos1, pos2, cType, cForm][pos1, pos2]
ngram [lemma, pos1, pos2, cType, cForm][pos1, pos2]
ngram [pos1][pos1, pos2, pos3, pos4]
ngram [pos1, pos2][pos1, pos2, pos3, pos4]
ngram [pos1, pos2, pos3, pos4][pos1, pos2, pos3, pos4]
ngram [pos1, pos2, cType, cForm][pos1, pos2, pos3, pos4]
ngram [lemma, pos1, pos2, cType, cForm][pos1, pos2, pos3, pos4]
ngram [pos1][pos1, pos2, pos3, pos4]
ngram [pos1, pos2][pos1, pos2, pos3, pos4]
ngram [pos1, pos2, pos3, pos4][pos1, pos2, pos3, pos4]
ngram [pos1, pos2, cType, cForm][pos1, pos2, pos3, pos4]
ngram [lemma, pos1, pos2, cType, cForm][pos1, pos2, pos3, pos4]
ngram [pos1][lemma, pos1, pos2, cType, cForm]
ngram [pos1, pos2][lemma, pos1, pos2, cType, cForm]
ngram [pos1, pos2, pos3, pos4][lemma, pos1, pos2, cType, cForm]
ngram [pos1, pos2, cType, cForm][lemma, pos1, pos2, cType, cForm]
ngram [lemma, pos1, pos2, cType, cForm][lemma, pos1, pos2, cType, cForm]

ngram [pron][pron]
ngram [pron, aType][pron]
ngram [pron, aType][pron, aType]
ngram [aConType][pron]
ngram [aConType, aModType][pron]
ngram [aType, aConType][pron]
ngram [aType, aConType, aModType][pron]
ngram [pron, aType, aConType][pron]
ngram [pron, aType, aConType, aModType][pron]
ngram [pron, aType, aConType][pron, aType, aConType]
ngram [pron, aType, aConType, aModType][pron, aType, aConType, aModType]
ngram [surface][surface]

ngram [goshu][goshu]
ngram [type][type]
ngram [goshu, type, pos1][goshu, type, pos1]

ngram [pos1][pos1][pos1]
ngram [pos1, pos2, pos3, pos4, cType, cForm][pos1, pos2, pos3, pos4, cType, cForm][pos1, pos2, pos3, pos4, cType, cForm]
ngram [lemma, pos1][lemma, pos1][lemma, pos1]

train loss
    surface 1,
    pos1 1,
    pos2 1,
    pos3 1,
    pos4 1,
    cType 1,
    cForm 1,
    lForm 1,
    lemma 1,
    orth 1,
    pron 1,
    orthBase 1,
    pronBase 1,
    goshu 1,
    type 1,
    aType 1,
    aConType 1,
    aModType 1
