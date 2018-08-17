
### Pynini-learn

See readme_install.org for installation of Pynini 
on Ubuntu 14.04 using vagrant.

* [first examples](ejf01/readme.md)
* [singularization](ejf02/readme.md)
* [edit-transducer tutorial](ejf03/readme.md)
* [edit transducer class](ejf04/readme.md)
* [Levenshtein examples](ejf05/readme.md)
* [Levenshtein Automaton for american english words](ejf06/readme.md)
* [Levenshtein Automaton for mw headwords](ejf07/readme.md)

#### Comment on Timing
The mw headwords example concluded that it takes about 5 sec to get
closest spellings for a (misspelled) word, in this lexicon of about 200,000
words.   This is too long to be very useful when checking more than a
few words.   Perhaps there is some additional optimization of the FST.
