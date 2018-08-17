### singularization example
```
python test02.py
```
singularization example from the Pynini tutorial at
http://www.opengrm.org/twiki/bin/view/GRM/PyniniDocs

https://www.safaribooksonline.com/oriole/string-processing-with-pythons-pynini-edit-transducers


This is what cdrewrite(phi, psi, lambda, rho)
 context dependent rewrite rules:
http://www.aclweb.org/anthology/P96-1031
 An Efficient Compiler for Weighted Rewrite Rules,M. Mohri (AT&T Research)
 and R. Sprout (Bell Laboratoreies), 1996
 phi -> psi / lambda __ rho
phi is to be replaced by psi whenever it is preceded by lambda
and followed by rho.  In general phi etc are regular expressions over
the alphabet of the rules.
  Best to use utf-8 strings.

