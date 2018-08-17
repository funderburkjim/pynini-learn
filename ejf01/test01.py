# -*- coding: utf-8
import pynini
def example0():
 # x is a vector of FST objects
 s = u"Pont l'Evêque"
 x = pynini.acceptor(s)
 print(u"Byte string acceptor from %s" %s)
 print(x)
 y =  pynini.acceptor(u"Pont l'Evêque",token_type="utf8")
 print(u"utf8 string acceptor from %s" %s)
 print (y)

def example1():
 # ref: http://www.openfst.org/twiki/bin/view/FST/FstQuickTour#CreatingShellFsts
 # A vector FST is a general mutable FST 
 example = pynini.Fst()
 Arc = pynini.Arc
 # A vector FST is a general mutable FST 
 example.add_state( ) # 1st state will be state 0 (returned by AddState)
 example.set_start(0) # arg is state ID
 # Adds two arcs exiting state 0.
 # Arc constructor args: ilabel, olabel, weight, dest state ID. 
 example.add_arc(0,Arc(1,1,0.5,1)) # 1st arg is src state ID 
 example.add_arc(0,Arc(2,2,1.5,1))
 # Adds state 1 and its arc. 
 example.add_state();
 example.add_arc(1,Arc(3,3,2.5,2))
 # Adds state 2 and set its final weight. 
 example.add_state()
 example.set_final(2,3.5) # 1st arg is state ID, 2nd arg weight 
 print("example1=")
 print example
 # next works, but the output is in a binary format
 filename="example1.fst"
 print "writing",filename
 example.write(filename) 
 print "reading",filename
 exfile = pynini.Fst.read(filename)
 print "printing fst read from file"
 print exfile

def example1a():
 # tries to use letters for labels; get error:
 # TypeError: an integer is required
 # A vector FST is a general mutable FST 
 example = pynini.Fst()
 Arc = pynini.Arc
 # A vector FST is a general mutable FST 
 example.add_state( ) # 1st state will be state 0 (returned by AddState)
 example.set_start(0) # arg is state ID
 # Adds two arcs exiting state 0.
 # Arc constructor args: ilabel, olabel, weight, dest state ID. 
 example.add_arc(0,Arc('a','x',0.5,1)) # 1st arg is src state ID 
 example.add_arc(0,Arc('b','y',1.5,1))
 # Adds state 1 and its arc. 
 example.add_state();
 example.add_arc(1,Arc('c','z',2.5,2))
 # Adds state 2 and set its final weight. 
 example.add_state()
 example.set_final(2,3.5) # 1st arg is state ID, 2nd arg weight 
 print("example1a=")
 print example

def example2():
 """ 
  ref: http://www.openfst.org/twiki/bin/view/FST/FstQuickTour#CreatingShellFsts
  construct fst with symbol tables, using fstcompile external program
  The formats are called AT&T formats
 """
 text = """
0 1 a x .5
0 1 b y 1.5
1 2 c z 2.5
2 3.5
 """
 isyms = """
<eps> 0
a 1
b 2
c 3
 """
 osyms = """
<eps> 0
x 1
y 2
z 3
 """
 import codecs,re
 with codecs.open("temp_fst.txt","w","utf-8") as f:
  f.write(text)
 with codecs.open("temp_isyms.txt","w","utf-8") as f:
  f.write(isyms)
 with codecs.open("temp_osyms.txt","w","utf-8") as f:
  f.write(osyms)

 from subprocess import call
 # Creates binary Fst from text file. 
 # The symbolic labels will be converted into integers using the symbol table files. 
 cmd = 'fstcompile --isymbols=temp_isyms.txt --osymbols=temp_osyms.txt temp_fst.txt temp_fst.fst'
 callargs = re.split(r' +',cmd)
 call(callargs)
 # As above but the symbol tables are stored with the FST. 
 #$ fstcompile --isymbols=isyms.txt --osymbols=osyms.txt --keep_isymbols --keep_osymbols text.fst binary.fst

 print "example 2 finished constructing temp_fst.fst from strings"
 example = pynini.Fst.read("temp_fst.fst")
 print example
 print "To get a string representation of temp_fst.fst:"
 print "fstprint --isymbols=temp_isyms.txt --osymbols=temp_osyms.txt temp_fst.fst tempout.txt"

 cmd = 'fstcompile --isymbols=temp_isyms.txt --osymbols=temp_osyms.txt --keep_isymbols --keep_osymbols temp_fst.txt temp_fstkeepsyms.fst'
 callargs = re.split(r' +',cmd)
 call(callargs)
 print "example 2 finished constructing temp_fstkeepsyms.fst from strings"
 example = pynini.Fst.read("temp_fstkeepsyms.fst")
 print example

 print "To get a string representation of temp_fstkeepsyms.fst:"
 print "fstprint temp_fstkeepsyms.fst tempout_keepsyms.txt"

if __name__ == "__main__":
 example2()
 exit()
 example0()
 example1()
 try:
  example1a()
 except:
  print "example1a is known to fail"
 example2()
