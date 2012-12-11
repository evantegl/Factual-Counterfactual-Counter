# imports
from random import choice
from genworlds import worldgen as init
from counterfactual import ifItHadBeenTheCase
from updates import updateFormula, updateLaw
import timeit

# main functions
def parenthesize(formula):
	"""
	INPUT: a string
	OUTPUT a string
	WHAT IT DOES: takes a formula and puts parentheses around it
	"""
	return "(" + formula + ")"

def randomClassicalFormula(complexity, letters = ["p", "q", "r", "s"], connectives = ["~", ">", "&", "|"]):
	"""
	INPUT: a list of letters, a list of connectives, and a number
	OUTPUT: a randomly created classical formula of the given
	complexity
	WHAT IT DOES: inductively builds formulas of lower complexity
	until it reaches the endpoint.
	"""
	i = 0
	formula = choice(letters)
	while i < complexity:
		connective = choice(connectives)
		if connective == "~":
			formula = connective + parenthesize(formula)
		else:
			formula = parenthesize(formula) + connective + parenthesize(choice(letters))
		i += 1
	return formula

# # # # # let's get with the testing
# def test(comp = 1, time=1000):
# 	letters = ["p", "q", "r"]
# 	connectives = ["~", ">", "&", "|"]
# 	# t = timeit.Timer("randomClassicalFormula(1)", "from __main__ import randomClassicalFormula")
# 	print "Complexity: 0 up to " + str(comp) + ";"
# 	print "Testing " + str(time) + " times."
# 	for i in range(comp):
# 		t = timeit.Timer("randomClassicalFormula(" + str(i) + ")", "from __main__ import randomClassicalFormula")
# 		print str(i) + ": " + str(t.timeit(time))

def timeCounterfactualsOfHigherComplexity(n = 1):
	letters = ["p", "q", "r", "s"]
	connectives = ["~", ">", "&", "|"]
	# begin the universe
	S = init(letters)
	# choose a formula, update with it as a law
	S = updateLaw(S, randomClassicalFormula(n))
	# choose a formula, update it normally
	S = updateFormula(S, randomClassicalFormula(n))
	# "If it had been the case that \psi" is a retraction of ~\psi then update with \psi
	S = ifItHadBeenTheCase(S, randomClassicalFormula(n))

def test(n = 4):
	for i in range(1, n):
		t = timeit.Timer("timeCounterfactualsOfHigherComplexity(" + str(i) + ")", "from __main__ import timeCounterfactualsOfHigherComplexity")
		print str(i) + ": " + str(t.timeit())


t = timeit.Timer("timeCounterfactualsOfHigherComplexity(3)", "from __main__ import timeCounterfactualsOfHigherComplexity")
print t.timeit(1)