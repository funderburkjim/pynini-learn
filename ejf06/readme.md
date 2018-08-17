
## Levenshtein Automaton for american english words

Examples using the edit_transducer module.

### install list of american words for ubuntu:
```
sudo apt-get install wamerican
```

directory is:
/usr/share/dict/wamerican
list of words in 
/usr/share/dict/american-english
# copy to local 
cp /usr/share/dict/american-english ameng

99171 words
938848 file size . 

### get alphabet used in lexicon
```
python make_alphabet.py ameng ameng_letters.txt
```

 69 letters used.

### Minor addition to edit_transducer
It takes some time to generate the Levenshtein Automaton for a lexicon.
Changes were made to the edit_transducer module to allow:

* writing the compiled lexicon Levenshtein Automaton
* reading the compiled automaton

### create and save the compiled Levenshtein Automaton
```
date
python -W ignore make_la.py ameng_letters.txt ameng  ameng_la.fst
date
```
Took 19 sec
ameng_la.fst is 4411944 bytes (~ 4MB)

### interactive program for nearest matches

```
 python -W ignore use_la.py ameng_letters.txt ameng_la.fst
```
this has input loop for entering a word.

