from genworlds import *
from pprint import pprint
from updates import *
from basis import *
from texoutput import texify

language = ['p','q','r']

s0 = worldgen(language)
s1=updateFormula(s0, "r")
s2=updateLaw(s1, "(r)>((p)|(q))")
s3=updateFormula(s1, "p")

#pprint(s3)

print(texify(s3,language))

sit1 = {'p': 0, 'q': 1, 'r': 1}
print "\nnow checking this situation and w_5:"
pprint(sit1)
print "determines? ", Determines(sit1,"w_5",s3)
print "basis? ", basisOfWorld(sit1,"w_5",s3)

#sit2 = {'q': 0, 'r': 1, 'p':0}
#print "\nnow checking this situation and w_5:"
#pprint(sit2)
#print "determines? ", Determines(sit2,"w_5",s3)
#print "basis? ", basisOfWorld(sit2,"w_5",s3)