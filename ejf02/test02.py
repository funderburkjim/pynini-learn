# -*- coding: utf-8
import pynini
def example0():
 """ This works, but has a lot of extra debug code, and doesn't permit
     all printable characters It gives the singularize example from
     PyniniDocs, with corrections
 """
 import string
 if True:
  vowel = pynini.union("a","e","i","o","u")
  consonant = pynini.union("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
  space = pynini.union("1"," ")
  sigma_star = pynini.union(vowel,consonant,space).closure()
  lowercase = pynini.union(vowel,consonant)
  sigma = pynini.union("a","e","i","o","u",
   "b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z", "1"," ")
  sigma_star = sigma.closure()
  #lowercase1 = pynini.acceptor(string.ascii_lowercase)
  #sigma1_list = list(string.ascii_lowercase) +['1',' ']
  sigma1_list = list(string.ascii_letters + string.digits) +[' ','.']
  sigma1 = pynini.union(*sigma1_list)
  sigma1_star = sigma1.closure()
  sigma_star = sigma1_star
  #print "lowercase==lowercase1",lowercase==lowercase1
  #print "lowercase=\n",lowercase
  #print "lowercase1=\n",lowercase1
  #sigma_star = pynini.union(lowercase,space).closure()
  #sigma_star = pynini.union(lowercase,space).closure()
  #exit(1)
 if False:
  #print "punctuation = ",string.punctuation
  ascii_letters = pynini.acceptor(string.ascii_letters)
  ascii_digits = pynini.acceptor(string.digits)
  sigma_star = pynini.union(ascii_letters,ascii_digits," ").closure()
 #print 'sigma-star=\n',sigma_star 
 #exit(1)
 singular_map = pynini.union(
    pynini.transducer("feet", "foot"),
    pynini.transducer("pence", "penny"),
    # Any sequence of bytes ending in "ches" strips the "es";
    # the last argument -1 is a "weight" that gives this analysis
    # a higher priority, if it matches the input.
    sigma_star + pynini.transducer("ches", "ch", -1), 
    # Any sequence of bytes ending in "s" strips the "s".
    sigma_star + pynini.transducer("s", ""))
 # right context. [EOS] is end-of-string
 rc = pynini.union(".", ",", "!", ";", "?", " ", "[EOS]")
 # cdrewrite(tau, lambda, rho, sigma_star, direction="ltr", mode="obl")
 # 
 singularize = pynini.cdrewrite(singular_map, " 1 ", rc, sigma_star)

 def singularizeFcn(stringin):
  #return pynini.shortestpath(
  #    pynini.compose(string.strip(), singularize)).stringify()
  #print "singularize has type=",type(singularize)
  #print(singularize)
  #s1 = string.strip(stringin)
  dbg=False
  if dbg: print "string=",stringin
  s1 = stringin.strip()
  if dbg: print "s1=",s1
  s2 = pynini.union(s1)
  if dbg: print "s2=",s2
  a = pynini.compose(s2,singularize)
  if dbg: print "a has type=",type(a),"a="
  if dbg: print(a)
  
  b = pynini.shortestpath(a)
  if dbg: print "b="
  if dbg: print b
  ans = b.stringify()
  return ans
  #return pynini.shortestpath(
  #    pynini.compose(string.strip(), singularize)).stringify()

 sample_strings = [
  "the current temperature in new york is 1 degrees",

  "The current temperature in New York is 1 degrees",
  "That measures 1 feet",
  "That measures 1.2 feet",
  "That costs just 1 pence",
  "The current temperature in N.Y.C. is 1 degrees.",
 ]
 for i,s in enumerate(sample_strings):
  print "Case ",i
  print "  Input = ",s
  t = singularizeFcn(s)
  print " Output = ",t
  #break # dbg just 1 exxample
 print "example0 done"

def example1():
 """ This implements the singularize example of PyniniDocs; the alphabet
     contains letters, digits, space and all punctuation except '[' and ']' (which
     have special significance in Pynini.
 """
 import string
 alphabet = set(string.letters + string.digits + string.punctuation + ' ') 
 alphabet = alphabet - set(['[',']'])
 #print (set(string.printable) - alphabet)  # characters not included
 # >>> set(['\t', '\x0b', '\n', '\r', '\x0c', '[', ']'])
 sigma_list = list(alphabet)  
 #print sigma_list
 sigma = pynini.union(*sigma_list)
 sigma_star = sigma.closure() # not sure why this is needed
 singular_map = pynini.union(
    pynini.transducer("feet", "foot"),
    pynini.transducer("pence", "penny"),
    # Any sequence of bytes ending in "ches" strips the "es";
    # the last argument -1 is a "weight" that gives this analysis
    # a higher priority, if it matches the input.
    sigma_star + pynini.transducer("ches", "ch", -1), 
    # Any sequence of bytes ending in "s" strips the "s".
    sigma_star + pynini.transducer("s", ""))
 # right context. [EOS] is end-of-string
 rc = pynini.union(".", ",", "!", ";", "?", " ", "[EOS]")
 # cdrewrite(tau, lambda, rho, sigma_star, direction="ltr", mode="obl")
 # 
 singularize = pynini.cdrewrite(singular_map, " 1 ", rc, sigma_star)

 def singularizeFcn(stringin):
  try:
   ans= pynini.shortestpath(
      pynini.compose(stringin.strip(), singularize)).stringify()
  except Exception as e:
   print("Error from singularizeFcn:",e)
   ans = stringin
  return ans

 sample_strings = [
  "The current temperature in New York is 1 degrees",
  "That measures 1 feet",
  "That measures 1.2 feet",
  "That costs just 1 pence",
  "The current temperature in N.Y.C. is 1 degrees.",
  # additional examples.
  "The length is 1 inches",
  "there is only 1 chess piece that is the black king.",
  "That measures 1feet",
  "That measures1 feet",
  "The length is example 1 feet and 1 inches",  # doesn't change feet to foot?
  "The length is example 1 inches and 1 feet", # changes both -- good
  "1 pence and 1 feet",
  "1 inches and 1 centimeters", # doesn't change inches; changes centimeters
  "exactly 1 inches and 1 centimeters", # changes both
 ]
 for i,s in enumerate(sample_strings):
  print "Case ",i
  print "  Input = ",s
  t = singularizeFcn(s)
  print " Output = ",t
  #break # dbg just 1 exxample
 print " done"


def example0_bad():
 """ This code is similar to the sample in PyniniDocs, but
  does not work.  The problem seems to be that sigma_star is not
  a big enough alphabet for the examples.
 """
 vowel = pynini.union("a","e","i","o","u")
 consonant = pynini.union("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                         "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")
 sigma_star = pynini.union(vowel, consonant).closure()
 #print 'sigma-star=\n',sigma_star 
 #exit(1)
 singular_map = pynini.union(
    pynini.transducer("feet", "foot"),
    pynini.transducer("pence", "penny"),
    # Any sequence of bytes ending in "ches" strips the "es";
    # the last argument -1 is a "weight" that gives this analysis
    # a higher priority, if it matches the input.
    sigma_star + pynini.transducer("ches", "ch", -1), 
    # Any sequence of bytes ending in "s" strips the "s".
    sigma_star + pynini.transducer("s", ""))
 # right context. [EOS] is end-of-string
 rc = pynini.union(".", ",", "!", ";", "?", " ", "[EOS]")
 # cdrewrite(tau, lambda, rho, sigma_star, direction="ltr", mode="obl")
 # 
 singularize = pynini.cdrewrite(singular_map, " 1 ", rc, sigma_star)
 def singularizeFcn(string):
  #return pynini.shortestpath(
  #    pynini.compose(string.strip(), singularize)).stringify()
  print "singularize has type=",type(singularize)
  #print(singularize)
  #s1 = string.strip(string)
  print "string=",string
  s1 = string.strip()
  print "s1=",s1
  s2 = pynini.union(s1)
  print "s2=",s2
  a = pynini.compose(s2,singularize)
  print "a has type=",type(a),"a="
  print(a)

  b = pynini.shortestpath(a)
  print "b="
  print b
  ans = b.stringify()
  return ans
  #return pynini.shortestpath(
  #    pynini.compose(string.strip(), singularize)).stringify()

 sample_strings = [
  "the current temperature in new york is 1 degrees",
  "The current temperature in New York is 1 degrees",
  "That measures 1 feet",
  "That measures 1.2 feet",
  "That costs just 1 pence",
  "The current temperature in N.Y.C. is 1 degrees",
 ]
 for i,s in enumerate(sample_strings):
  print "Case ",i
  print "  Input = ",s
  t = singularizeFcn(s)
  print " Output = ",t
  break # dbg just 1 exxample
 print "example0 done"
def example1x():
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
 example1()
 exit()
 example0()
 example1()
 try:
  example1a()
 except:
  print "example1a is known to fail"
 example2()
