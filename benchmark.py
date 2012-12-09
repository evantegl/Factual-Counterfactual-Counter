from pprint import pprint
from array import array
from genworlds import worldgen
from updates import updateFormula, updateLaw
from counterfactual import ifItHadBeenTheCase
from subprocess import call
from texoutput import *
from random import choice
from utilities import supports
from timeit import timeit
import time
import sys


class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start

def checkRandomSituation(cogstate):
	# generate a random law and update with it:
	law="("+choice(alphabet)+")>("+choice(alphabet)+")"
	#print "  updating with the law "+law
	cogstate = updateLaw(cogstate,law)

	# generate a random fact and update with it:
	fact=choice(alphabet)
	#print "  updating with the fact "+fact
	cogstate = updateFormula(cogstate,fact)

	# generate a random non-trivial counterfactual and check it:
	cfantecedent=choice(alphabet)
	restralph=list(alphabet)
	restralph.remove(cfantecedent)
	cfconsequent=choice(restralph)
	#print "  checking the counterfactual "+cfantecedent+"~>"+cfconsequent+":"
	cogstateNew = ifItHadBeenTheCase(cogstate, cfantecedent)
	#print "  supported: " + str(supports(cogstateNew,cfconsequent))

string="abcdefghijklmnopqrstuvwxyz" #52

for i in range(2,10):
	print "Let's consider "+str(i)+" propositions"
	alphabet=list(string[:i])
	W = worldgen(alphabet)
	print "  Generated all worlds."
	print "  Now we'll check 1000 random counterfactuals in random situations"
	sys.stdout.write(' ')
	with Timer() as t:
		for k in range(10): # do this a lot of times.
			for m in range(100): # do this a lot of times.
				checkRandomSituation(W)
			sys.stdout.write(" . ")
			sys.stdout.flush()
			#print "."
	print('\n  This took %.03f sec.' % t.interval)
	print ""


