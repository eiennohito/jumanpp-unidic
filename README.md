# What is it

[Unidic](http://unidic.ninjal.ac.jp/) version of [Juman++](https://github.com/ku-nlp/jumanpp). 

# How to use it

There are no pre-trained models yet, you need to make you own.

## Prerequisites

For running:

* Unix-like environment
* C++14-compatible compiler
* CMake 3.1 or later

For training additionally:

* Python 3 or later
* MeCab
* Offline version of BCCWJ

## Compiling Programs

```bash
git clone git@github.com:eiennohito/jumanpp-unidic.git --recursive
cd jumanpp-unidic
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j
```

You will need `jumanpp/src/core/tool/jumanpp_tool` binaries for making a model
and `src/jumanpp-unidic-simple` for the analysis.

## Training a Model

We will update BCCWJ tags to the modern Unidic,
create training data for Juman++ and train a model.

You will need about 10G of RAM to train a model using BCCWJ.

Paths for all binaries are written from the `build` directory.

First lets prepare training corpus data.

1. Download Unidic 2.3.0 from [the official page](http://unidic.ninjal.ac.jp/back_number#unidic_bccwj)
1. Add following lines to the Unidic `dicrc`:
```
node-format-unidic22q = "%M","%f[0]","%f[1]","%f[2]","%f[3]","%f[4]","%f[5]","%f[6]","%f[7]","%f[8]","%f[9]","%f[10]","%f[11]","%f[12]","%f[13]","%f[14]","%f[15]","%f[16]","%f[17]","%f[18]","%f[19]","%f[20]","%f[21]","%f[22]","%f[23]","%f[24]","%f[25]","%f[26]","%f[27]","%f[28]"\n
unk-format-unidic22q = "%M","%f[0]","%f[1]","%f[2]","%f[3]","%f[4]","%f[5]"\n
bos-format-unidic22q =
eos-format-unidic22q = EOS\n
```
1. Convert BCCWJ to MeCab constrained analysis mode.
```bash
python3 ../scripts/bccwj2mecab_input.py <path to BCCWJ>/CORE/SUW/core_SUW.txt > core.mecab.in
```
1. "Modernize" BCCWJ with newer Unidic using MeCab constrained analysis mode: 
```bash
mecab -d <unidic-2.3.0> -Ounidic22q -p core.mecab.in > core.mecab.out
```
1. Convert modernized BCCWJ to the Juman++ training input:
```bash
python3 ../scripts/fixup_mecab.py core.mecab.out
```

After these steps there should be files `core.mecab.out.full-tdata` and `core.mecab.out.part-tdata`
near the `core.mecab.out`.
Now let's create a seed model (without parameters).

1. Create a raw analysis dictionary for Juman++ by concatenating `scripts/header.csv` and `lex.csv` from Unidic.
1. Compile an analysis dictionary: 
```bash
jumanpp/src/core/tool/jumanpp_tool index \
    --spec ../src/unidic-2.3.0-simple.spec \
    --dict-file <concatenated dictionary> \
    --output unidic.seed

```

And finally, let's train a model:
```bash
../scripts/train.sh jumanpp/src/core/tool/jumanpp_tool unidic.seed \
    core.mecab.out.full-tdata core.mecab.out.part-tdata \
    unidic.model
```

You can do analysis now with Juman++!

```
src/jumanpp-unidic-simple unidic.model
```

## Embedding a RNN

Coming soon...