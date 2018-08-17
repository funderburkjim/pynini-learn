""" https://www.safaribooksonline.com/oriole/string-processing-with-pythons-pynini-edit-transducers
 usage: from tested import *
"""
from __future__ import division

import string  # Demonstration only.

from pynini import acceptor    # Demonstration only.
from pynini import compose
from pynini import invert
from pynini import isomorphic  # Demonstration only.
from pynini import NO_STATE_ID
from pynini import prune
from pynini import shortestdistance
from pynini import shortestpath
from pynini import string_map
from pynini import synchronize
from pynini import transducer
from pynini import union

"""
example 1:
sheep = acceptor("b") + acceptor("a").plus
sheep.optimize(True)

sheep is in effect a regular expressions that matches a string
that starts with 'b' and is followed by one or more 'a'.
Similar to python 
 re.search(r'^ba+$',s)
For a string s,
 compose(s,sheep).num_states() != 0 
is similar to
 re.search(r'^ba+$',s) != None

"""

"""
Example 2
sheep_to_cow = transducer("b", "m") + transducer("a", "o").plus
sheep_to_cow.optimize(True)

x = compose('baa',sheep_to_cow)
x.num_states() # >> 4
x.stringify()  # >> moo

"""

"""
Example 3: Edit transducer
# For simplicity, we assume a two-character alphabet {"a", "b"}.
match = union("a", "b")
match.optimize(True)

# We use a "1" as a non-zero weight.
insert = transducer("", match, weight=1)
insert.optimize(True)

delete = transducer(match, "", weight=1)
# Or, equivalently: delete = invert(insert)
delete.optimize(True)
#   delete == invert(insert) -> True

substitute = synchronize(transducer(match, match, weight=1))
substitute.optimize(True)

# 'ops' for operations
ops = union(match, delete, insert, substitute)
ops.optimize(True)
#
#The ops transducer currently only accepts zero or one elements of Σ,
# whereas we want a transducer over the infinite set Σ*.
# To do this, we compute its (concatenative) closure:

edit = ops.closure().optimize(True)

s_i = "abba"
s_o = "baba"

lattice = compose(compose(s_i, edit), s_o)

# Every path in this lattice is a possible alignment of the string abba 
# to the string baba, 
# and the cost of that path is the edit distance for that alignment.
# currently, lattice has 25 states
# We can save a copy before pruning:
lattice_unpruned = lattice.copy()
# prune the lattice so it contains only optimized paths
lattice1 = prune(lattice, weight=0)
# lattice1.num_states() # 10

# to draw a postscript file:
lattice1.write('outputs/lattice1.fst')
from subprocess import call
call(['fstdraw','outputs/lattice1.fst','outputs/lattice1.dot'])
#call(['dot','-Tsvg','outputs/lattice1.dot','-o','outputs/lattice1.svg'])
call(['dot','-Tps','outputs/lattice1.dot','-o','outputs/lattice1.ps'])

"""

""" 
Example 4: Edit transducer factored
This is a trick when larger alphabets are to be used.

# For simplicity, we assume a two-character alphabet {"a", "b"}.
match = union("a", "b")
match.optimize(True)

# ------------------------------------------
# first, the four 'left-factor' operations
# ------------------------------------------
# The square brackets cause the string to be interpreted as a "reserved" symbol.
# Note 1/2 works in Python due to 'from __future__ import division'
from __future__ import division
i_insert = transducer("", "[<insert>]", weight=1/2)
i_insert.optimize(True)

i_delete = transducer(match, "[<delete>]", weight=1/2)
# We have to optimize twice to get the minimal machine.
i_delete.optimize(True).optimize(True)

i_substitute = transducer(match, "[<substitute>]", weight=1/2)
# We have to optimize twice to get the minimal machine.
i_substitute.optimize(True).optimize(True)

# 'ops' for operations  
# Question: does change of order (delete,insert -> insert,delete) matter?
#  Probably not
i_ops = union(match, i_insert, i_delete, i_substitute)
i_ops.optimize(True)
#
# ----------------------------------------------------------------
# right-factor transducer
# For the right factor Εo, we need an insert operation that maps from <insert> 
# to the alphabet, a delete operation that maps from <delete> to epsilon, 
# and so on. 
# Rather than building these directly, we can construct the entire set of right 
# operations by inverting the left factor and then 
# swapping <insert> and <delete> with relabel_pairs. 
# This first requires us to look up the integer labels associated with 
# these special symbols:
# ----------------------------------------------------------------
o_ops = invert(i_ops)
syms = o_ops.input_symbols()
insert_label = syms.find("<insert>")
delete_label = syms.find("<delete>")
o_ops.relabel_pairs(ipairs=((insert_label, delete_label),
                                   (delete_label, insert_label)))

# compute clsures of the two sets of operations, and optimize
e_i = i_ops.closure().optimize(True)
e_o = o_ops.closure().optimize(True)

# ----------------------------------------------------------------
#  confirm that the composition of the two factors is in fact isomorphic to 
# the single-machine edit transducer:
# NOTE: I had to r
factored_edit = compose(e_i, e_o)
factored_edit.optimize(True)
assert isomorphic(edit, factored_edit)


#The ops transducer currently only accepts zero or one elements of Σ,
# whereas we want a transducer over the infinite set Σ*.
# To do this, we compute its (concatenative) closure:

edit = ops.closure().optimize(True)

s_i = "abba"
s_o = "baba"

i_edit = compose(s_i, e_i)
o_edit = compose(e_o, s_o)
lattice2 = prune(compose(i_edit, o_edit), weight=0)
# lattice2 is isomorphic to lattice1 from previous example:
isomorphic(lattice2,lattice1)  # > True

# Every path in this lattice is a possible alignment of the string abba 
# to the string baba, 
# and the cost of that path is the edit distance for that alignment.
# currently, lattice has 25 states
# We can save a copy before pruning:
lattice_unpruned = lattice.copy()
# prune the lattice so it contains only optimized paths
lattice1 = prune(lattice, weight=0)
# lattice1.num_states() # 10

# to draw a postscript file:
lattice1.write('outputs/lattice1.fst')
from subprocess import call
call(['fstdraw','outputs/lattice1.fst','outputs/lattice1.dot'])
#call(['dot','-Tsvg','outputs/lattice1.dot','-o','outputs/lattice1.svg'])
call(['dot','-Tps','outputs/lattice1.dot','-o','outputs/lattice1.ps'])

"""
