##### Import all the functions we need #####
from pprint import pprint
from truthchecker import tiw as formulaIsTrue

##### Set up our metavariables, whatever they are #####
meta = "meta"
FS = "FS"
US = "US"

# Main functions defined in here
def formulaIsConsistent(cogstate, formula):
	"""
	INPUT: a pair (cognitive state, formula)
	OUTPUT: a cognitive state
	WHAT IT DOES: Should tell you whether the formula is true in
		at least one world in FS.
	"""
	for world in cogstate:
		if world[meta][US]:
			if formulaIsTrue(world, formula):
				return True
	return False

def destroyWorld(world):
	"""
	INPUT: a world
	OUTPUT: a world
	WHAT IT DOES: Tells the world it's not in FS or US.
	"""
	newWorld = world
	newWorld[meta][FS] = newWorld[meta][US] = False
	return newWorld

def destroyAllWorlds(cogstate):
	"""
	INPUT: a cognitive state
	OUTPUT: the empty cognitive state
	WHAT IT DOES: Destroys all worlds.
	"""
	newstate = []
	for world in cogstate:
		newstate.append(destroyWorld(world))
	return newstate

def updateFormula(cogstate, formula):
	"""
	INPUT: a pair (cognitive state, formula) where cognitive states
		are arrays of world objects and formulas are strings.
	OUTPUT: another cognitive state
	WHAT IT DOES: It should go through each world and call a function
		that checks whether the formula is true at each world. If it
		isn't, mark it as not being in FS; do nothing otherwise.
	"""
	newstate = []
	if formulaIsConsistent(cogstate, formula):
		for world in cogstate:
			if not formulaIsTrue(world, formula):
				world[meta][FS] = False
			newstate.append(world)
	else:
		newstate = destroyAllWorlds(cogstate)
	return newstate

def updateLaw(cogstate, law):
	"""
	INPUT: a pair (cognitive state, law) where cognitive states
		are arrays of world objects and the law is a string
	OUTPUT: another cognitive state
	WHAT IT DOES: Should go through each world and call a function
		that checks whether the formula is true at each world,
		and if it is do nothing, else mark it as not being in
		US or FS.
	"""
	newstate = []
	if formulaIsConsistent(cogstate, law):
		for world in cogstate:
			if not formulaIsTrue(world, law):
				world[meta][FS] = False
				world[meta][US] = False
			newstate.append(world)
	else:
		newstate = destroyAllWorlds(cogstate)
	return newstate
