
### Examples using the edit_transducer module.


ref: https://www.safaribooksonline.com/oriole/string-processing-with-pythons-pynini-edit-transducers

#### Installation
git clone https://github.com/kylebgorman/EditTransducer.git

I don't want to install this in the pynini vm Python library at the moment.
So, just copy it to top level in ejf04
cd ejf04
cp EditTransducer/edit_transducer/edit_transducer.py .

### examples
```
python -i
from tested import *
```

Examples are present in comments within tested.py that can be
copy-pasted into interactive session.


### Cheese example in two steps
do the cheese example in two steps:
This requires minor changes to edit_transducer.py so lexicon fst can 
be written to a binary file, and then read back in an application.
```
 -W ignore: ref https://stackoverflow.com/questions/17626694/remove-python-userwarning
```

1) create and save the compiled Levenshtein Automaton
   `python -W ignore make_la.py cheeses.txt cheeses_la.fst`
2) read the compiled LA and do to tests
   `python -W ignore use_la.py  cheeses_la.fst`
   * results 
    ('rockford', [u'roquefort'])
    ('cheesesure', [u'cheshire'])
