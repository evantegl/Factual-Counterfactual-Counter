from genworlds import *
from pprint import pprint
from updates import *
from basis import *
from texoutput import texify
from retraction import retractOnWorld,retractOnState
from utilities import getWorldByName
from propositions import propositionFromFormula

language = ['p','q','r']

s0 = worldgen(language)
s1=updateFormula(s0, "r")
s2=updateLaw(s1, "(r)>((p)|(q))")
s3=updateFormula(s1, "p")

#pprint(s3)

#print(texify(s3,language))
print "\nThis is s3:"
pprint(s3)

print "\nThe bases of w_7 in s3 are: "
pprint(getAllBases(getWorldByName("w_7",s3),s3))

prop=propositionFromFormula(s3,"p")

print "\nThe retraction w w_7 with [[p]] is:"
pprint(retractOnWorld(s3,"w_7",prop))

s4=retractOnState(s3,prop)

pprint(s4)