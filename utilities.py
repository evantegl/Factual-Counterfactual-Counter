# Miscellaneous useful functions

# imports
from pprint import pprint

# variables
meta = 'meta'
values = 'values'
name = 'name'
FS = 'FS'
US = 'US'

def subset(situation, world):
	"""
	INPUT: a pair (situation, world)
	OUTPUT: A boolean.
	WHAT IT DOES: tells you whether the situation
	is a subset of the world.
	"""
	if values not in world.keys():
		for pair in situation.items():
			if pair not in world.items():
				return False
		return True
	# otherwise, the second argument is a situation
	else:
		for pair in situation.items():
			if pair not in world[values].items():
				return False
		return True

def getWorldByName(worldname,cogstate):
	for world in cogstate:
		if world["meta"]["name"]==worldname:
			return world
	return False #this should never happen

def negateFormula(formula):
	return "~(" + formula + ")"

def test():
	situation = {
		'p': True,
		'q': True
	}
	world = {
		meta: {
			name: "soemthing",
			FS: True,
			US: False
		},
		values: {
			'p': True,
			'q': False,
			'r': False,
			's': True
		}
	}
	pprint(subset(situation, world))

# test()