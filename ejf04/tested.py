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
from edit_transducer import LatticeError,EditTransducer
from edit_transducer import LevenshteinDistance,LevenshteinAutomaton

"""
# Example 1: string_map for Cheeses
# string_map compiles a tuple of words into an FSA equivalent to a trie 
#  (prefix tree)
lexicon = ("gruyere", "cheshire", "roquefort",
           "camembert", "gouda", "caithness")
compiled_lexicon = string_map(lexicon)
# visualization
compiled_lexicon.write('outputs/cheese6.fst')
from subprocess import call
call(['fstdraw','outputs/cheese6.fst','outputs/cheese6.dot'])
call(['dot','-Tps','outputs/cheese6.dot','-o','outputs/cheese6.ps'])
# double click to open with Adobe Distiller, which constructs chees6.pdf,
# which then may be viewed with Adobe Acrobat Reader DC.


"""

"""
# Example 2: levenshtein distance on abba baba example
s_i = "abba"
s_o = "baba"

# EditTransducer object is initialized with an alphabet,
#  and optionally with insert_cost, delete_cost, and substitute_cost.
# LevenShtein distance is similarly initialized
ld = LevenshteinDistance(("a", "b"))
ld.distance(s_i, s_o)  # 2.0

# error condition:
ld.distance(s_i, "babac")
# >>> edit_transducer.LatticeError: Lattice is empty
"""

"""
Example 3. Levenshtein Automaton

lexicon = ("gruyere", "cheshire", "roquefort",
           "camembert", "gouda", "caithness")
la = LevenshteinAutomaton(string.ascii_lowercase, lexicon)
la.closest_match("rockford") # roquefort
la.closest_matches("cheesesure") # an iterator
list(la.closest_matches("cheesesure"))  # [cheshire]
"""
