
## Levenshtein Automaton for mw headwords

Examples using the edit_transducer module.

### lexicon of Sanskrit words
We start with a copy of mw/pywork/mwhw2.txt  This is a list of
headwords (with duplicates) for the *Monier-Williams Sanskrit-English Dictionary* of 1899.  It was obtained from the digitization at
http://www.sanskrit-lexicon.uni-koeln.de/.

From mwhw2, generate a list of the distinct headwords.  These are
Sanskrit words spelled with the [SLP1 transliteration](https://en.wikipedia.org/wiki/SLP1).
```
python make_lexicon.py ../mwhw2.txt mwlexicon.txt
```
193905 words
2048491 file size .

### get alphabet used in lexicon
```
python make_alphabet.py mwlexicon.txt mwlexicon_letters.txt
```
 52 letters used.


### create and save the compiled Levenshtein Automaton
```
date
python -W ignore make_la.py mwlexicon_letters.txt mwlexicon.txt  mwlexicon_la.fst
date
```
Took 60 secs
mwlexicon_la.fst is 17064032 (~ 17MB)

### Interactive program to find 'nearest matches'
```
2) python -W ignore use_la.py mwlexicon_letters.txt mwlexicon_la.fst
```

### batch program to find nearest matches
The pwis_notmw2.txt contains information on 1585 presumed Sanskrit words
derived from another dictionary (see [PW IAST corrections](https://github.com/sanskrit-lexicon/CORRECTIONS/issues/419)).  Many of these are misspelled.  Previous
work identifed possible corrections in various ways.  However, this previous
work left 309 cases with no suggestions.  Our objective is to use the
Levenshtein Automaton to generate suggestions for these 309.
The output (pwis_notmw3.txt) also has 1585 records, with the suggestions
generated for the 309 marked by '(LevAuto)'.

```
 python -W ignore use_la_pwis.py mwlexicon_letters.txt mwlexicon_la.fst pwis_notmw2.txt pwis_notmw3.txt
```

### Timing 
The construction of the suggestions in pwis_nowmw3.txt seemed to take a long
time.  I did two timing tests.

* test 1: 1707 secs for 309 cases. 5.5 sec per search
  * 2gb memory in virtual machine
* test 2: 1766 sec  5.7 secs per search
  * 4gb memory in virtual machine

These times seem slow.   Perhaps there is some detail of optimization
that would improve the times.

### Burnouf spelling suggestions
09-26-2018

```
vagrant up
vagrant ssh
cd /vagrant/ejf07
 python -W ignore bur_la.py mwlexicon_letters.txt mwlexicon_la.fst bur_input.txt bur_output.txt
```

194 words
time: 924 sec. 4.8sec/word
