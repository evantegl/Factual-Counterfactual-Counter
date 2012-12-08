from genworlds import *
from pprint import pprint
from updates import *
from basis import *
from texoutput import texify
from retraction import retractOnWorld,retractOnState
from utilities import getWorldByName
from propositions import propositionFromFormula
from counterfactual import ifItHadBeenTheCase

language = ['p','q','r']

s0 = worldgen(language)
s1=updateFormula(s0, "r")
s2=updateLaw(s1, "(r)>((p)|(q))")
s3=updateFormula(s1, "p")

print "\nThis is s3:"

print(texify(s3))

print "\nThe bases of w_7 in s3 are: "
pprint(getAllBases(getWorldByName("w_7",s3),s3))

prop=propositionFromFormula(s3,"p")

print "\nThe retraction of w_7 with [[p]] is:"
pprint(retractOnWorld(s3,"w_7",prop))

print "\nThe retraction of s3 with [[p]] is:"
s4=retractOnState(s3,prop)

pprint(s4)

print(texify(s4))

s5=ifItHadBeenTheCase(s3,"~(p)")

print "\nThis is s5:"
print texify(s5)