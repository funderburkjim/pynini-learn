
Examples from the Pynini tutorial at
http://www.opengrm.org/twiki/bin/view/GRM/PyniniDocs

https://www.safaribooksonline.com/oriole/string-processing-with-pythons-pynini-edit-transducers

### test01

`python test01.py` runs various examples drawn from the above source.

It is intended that  a user might modify which examples are run.

### pywrapfst
This is a Python Extension of the openfst library
```
import pywrapfst as fst
```

* openfst:  http://www.openfst.org/twiki/bin/view/FST/WebHome
OpenFst is a library for constructing, combining, optimizing, and searching 
weighted finite-state transducers (FSTs). 
Weighted finite-state transducers are automata where each transition has an 
input label, an output label, and a weight. 
The more familiar finite-state acceptor is represented as 
a transducer with each transition's input and output label equal. 
Finite-state acceptors are used to represent sets of strings 
(specifically, regular or rational sets); 
finite-state transducers are used to represent binary relations between 
pairs of strings (specifically, rational transductions). 
The weights can be used to represent the cost of taking a particular transition.

### drawing an fst
a) install 'dot' program
```
sudo apt-get install graphviz
```
# assume fst is saved in file temp_fst.fst with corresponding symbol tables
# This was done in example2 of test01.py
# Then use shell prgram fstdraw to construct input file for 'dot':
# this 'dot' file is a json file
```
fstdraw --isymbols=temp_isyms.txt --osymbols=temp_osyms.txt temp_fst.fst temp_fst.dot
```
# Use dot to convert this to postcript file
```
dot -Tps temp_fst.dot > temp_fst.ps
```

# In windows, double clicking brings up 'Adobe distiller',
#  which converts the file to temp_fst.pdf
# The latter is viewable with any pdf viewer, such as Adobe reader.
# It gives a pretty picture, like those shown in the openfst documentation.

