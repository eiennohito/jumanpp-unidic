# Field definitions are from rewrite.def

field 1 surface string trie_index
# fields 2-4 are for mecab 
field 5 pos1 string align 5
field 6 pos2 string align 5
field 7 pos3 string align 5
field 8 pos4 string align 5
field 9 cType string align 5
field 10 cForm string align 5
field 11 lForm string
field 12 lemma string
field 13 orth string
field 14 pron string
field 15 orthBase string
field 16 pronBase string
field 17 goshu string
field 18 iType string
field 19 iForm string
field 20 fType string
field 21 fForm string
field 23 iConType string
field 24 fConType string
field 25 type string
field 26 kana string
field 27 kanaBase string
field 28 form string
field 29 formBase string
field 30 aType string
field 31 aConType string
field 32 aModType string
field 33 goihyo string
field 34 goiso string

feature nodeCharType = codepoint_type 0

unk catchall template row 1: single family_everything

# features from feature.def

# LGO0X
ngram [lForm, lemma, pos1, pos2, pos3, pos4, orth]
ngram [lForm, lemma, pos1, pos2, pos3, orth]
ngram [lForm, lemma, pos1, pos2, orth]
ngram [lForm, lemma, pos1, orth]
# LGCO0X
ngram [lForm, lemma, pos1, pos2, cType, cForm, orth]
ngram [lForm, lemma, pos1, pos2, cType, orth]
# LG0X
ngram [lForm, lemma, pos1, pos2, pos3, pos4]
ngram [lForm, lemma, pos1, pos2, pos3]
ngram [lForm, lemma, pos1, pos2]
ngram [lForm, lemma, pos1]
# LGC0X
ngram [lForm, lemma, pos1, pos2, cType, cForm]
ngram [lForm, lemma, pos1, cType, cForm]
# LGCt0X
ngram [lForm, lemma, pos1, pos2, cType]
ngram [lForm, lemma, pos1, cType]
# L0X
ngram [lForm, lemma]
# LGP0X
ngram [lForm, lemma, pos1, pos2, pos3, pos4, pron]
ngram [lForm, lemma, pos1, pos2, pos3, pron]
ngram [lForm, lemma, pos1, pos2, pron]
ngram [lForm, lemma, pos1, pron]
# LGCP0X
ngram [lForm, lemma, pos1, pos2, cType, cForm, pron]
ngram [lForm, lemma, pos1, pos2, cType, pron]
# GC0X
ngram [pos1, cType]
ngram [pos1, pos2, cType]
ngram [pos1, cType, cForm]
ngram [pos1, pos2, cType, cForm]
# G0X
ngram [pos1]
ngram [pos1, pos2]
ngram [pos1, pos2, pos3]
ngram [pos1, pos2, pos3, pos4]
# C0x
ngram [cType]
ngram [cType, cForm]
# O0X
ngram [orth]
ngram [orth, orthBase]
# P0X
ngram [pron]
ngram [pron, pronBase]
# W0X
ngram [goshu]
# WG0X
ngram [goshu, pos1]
# WT0X
ngram [nodeCharType]
# TG0X
ngram [nodeCharType, pos1]


ngram [surface]

# bigrams

ngram [pos1][pos1]
ngram [pos1, pos2][pos1]
ngram [pos1, pos2, pos3, pos4][pos1]
ngram [pos1][pos1]
ngram [pos1, pos2][pos1, pos2]
ngram [pos1, pos2, pos3, pos4][pos1, pos2]
ngram [pos1][pos1, pos2, pos3, pos4]
ngram [pos1, pos2][pos1, pos2, pos3, pos4]
ngram [pos1, pos2, pos3, pos4][pos1, pos2, pos3, pos4]


