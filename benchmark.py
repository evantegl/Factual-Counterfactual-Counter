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

def checkRandomCounterfactual(cogstate):
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
	result=supports(cogstateNew,cfconsequent)

def checkRandomImplication(cogstate):
  	# generate a random law and update with it:
	law="("+choice(alphabet)+")>("+choice(alphabet)+")"
	#print "  updating with the law "+law
	cogstate = updateLaw(cogstate,law)

	# generate a random fact and update with it:
	fact=choice(alphabet)
	#print "  updating with the fact "+fact
	cogstate = updateFormula(cogstate,fact)

	# generate a random non-trivial implication and check it:
	imantecedent=choice(alphabet)
	restralph=list(alphabet)
	restralph.remove(imantecedent)
	imconsequent=choice(restralph)
	#print "  checking the implication "imantecedent+"->"imconsequent+":"
	cogstateNew = updateLaw(cogstate, imantecedent)
	result = supports(cogstateNew,imconsequent)

string="abcdefghijklmnopqrstuvwxyz" #52

for i in range(2,10):
	print "Let's consider "+str(i)+" propositions"
	alphabet=list(string[:i])
	W = worldgen(alphabet)
	print "  Generated all worlds. Now we'll check 1000 random implications in random situations"
	sys.stdout.write(' ')
	with Timer() as t:
		for k in range(10): # do this a lot of times.
			for m in range(100): # do this a lot of times.
				checkRandomImplication(W)
			sys.stdout.write(" . ")
			sys.stdout.flush()
			#print "."
	print('\n  This took %.03f sec.' % t.interval)
	print ""

for i in range(2,10):
	print "Let's consider "+str(i)+" propositions"
	alphabet=list(string[:i])
	W = worldgen(alphabet)
	print "  Generated all worlds. Now we'll check 1000 random counterfactuals in random situations"
	sys.stdout.write(' ')
	with Timer() as t:
		for k in range(10): # do this a lot of times.
			for m in range(100): # do this a lot of times.
				checkRandomCounterfactual(W)
			sys.stdout.write(" . ")
			sys.stdout.flush()
			#print "."
	print('\n  This took %.03f sec.' % t.interval)
	print ""