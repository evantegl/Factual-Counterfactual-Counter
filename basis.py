# imports
from pprint import pprint
from truthchecker import tiw as formulaIsTrue
from utilities import subset
from updates import updateFormula, updateLaw
from genworlds import worldgen, sitgen

# variables
meta = 'meta'
values = 'values'
name = 'name'
FS = 'FS'
US = 'US'

# the main functions
def Forceable(situation, proposition, cogstate):
	"""
	INPUT: a triple (situation, proposition, cognitive state)
	OUTPUT: a Boolean
	WHAT IT DOES: Decides whether the given situation forces
	the proposition in the cognitive state.
	"""
	for world in cogstate:
		if world[meta][US]:
			if subset(situation, world):
				if world[meta][name] not in proposition:
					return False
	return True

def Determines(situation, world, cogstate):
	"""
	This is easy
	"""
	return Forceable(situation, [world], cogstate)

def basisOfWorld(worldname,cogstate):
	"""
	INPUT: a pair (worldname, cognitive state)
	OUTPUT: an array of bases
	WHAT IT DOES:
	"""
	return False

def test():
	language=['p','q','r']
	s0=worldgen(language)
	s1=updateFormula(s0, "r")
	s2=updateLaw(s1, "(r)>((p)|(q))")
	situation = {
		'p': True
	}
	pprint("Result 1:")
	pprint(Forceable(situation, [s2[5][meta][name], s2[4][meta][name], s2[6][meta][name], s2[7][meta][name]], s2))
	pprint("Result 2:")
	pprint(Forceable(situation, ["w_5", "w_4", "w_6", "w_7"], s2))

# test()