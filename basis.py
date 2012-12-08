# imports
from pprint import pprint
from truthchecker import tiw as formulaIsTrue
from utilities import subset
from updates import updateFormula, updateLaw
from genworlds import worldgen, sitgen, subsitgen

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

def Determines(situation, worldname, cogstate):
	"""
	This is easy
	"""
	return Forceable(situation, [worldname], cogstate)

def basisOfWorld(situation, worldname, cogstate):
	"""
	INPUT: a pair (worldname, cognitive state)
	OUTPUT: an array of bases
	WHAT IT DOES: check if worldname
	"""
	if not Determines(situation, worldname, cogstate):
		return False
	# now check whether its minimal:
	subsituations=subsitgen(situation)
	for subsituation in subsituations:
		if Determines(subsituation, worldname, cogstate):
			return False
	return True

def getAllBases(world, cogstate):
	"""
	INPUT: a world and a cognitive state
	OUTPUT: an array of situations that are bases
	WHAT IT DOES: finds all the bases for a world in a cognitive
	state.
	"""
	bases = []
	for situation in sitgen(world):
		if basisOfWorld(situation, world[meta][name], cogstate):
			bases.append(situation)
	return bases

def test():
	language=['p','q','r','s']
	s0=worldgen(language)
	s1=updateFormula(s0, "r")
	s2=updateLaw(s1, "(r)>((p)|(q))")
	situation = {
		'p': True
	}
	# pprint("Result 1:")
	# pprint(Forceable(situation, [s2[5][meta][name], s2[4][meta][name], s2[6][meta][name], s2[7][meta][name]], s2))
	# pprint("Result 2:")
	# pprint(Forceable(situation, ["w_5", "w_4", "w_6", "w_7"], s2))
	w0 = {
		meta: {
			name: "w0",
			FS: True,
			US: True
		},
		values: {
			'p': True,
			'q': False,
			'r': False,
			's': True
		}
	}
	w1 = {
		meta: {
			name: "w1",
			FS: True,
			US: True
		},
		values: {
			'p': False,
			'q': True,
			'r': False,
			's': False
		}
	}
	w2 = {
		meta: {
			name: "w2",
			FS: True,
			US: True
		},
		values: {
			'p': False,
			'q': False,
			'r': True,
			's': True
		}
	}
	cogstate = [w0, w1, w2]
	pprint(getAllBases(w0, cogstate))

# test()