#####
# Functions for dealing with propositions
#####

# imports
from pprint import pprint
from truthchecker import tiw as formulaIsTrue

# variables
meta = 'meta'
values = 'values'
name = 'name'
FS = 'FS'
US = 'US'

# main functions
def propositionFromFormula(cogstate, formula):
	"""
	INPUT: A pair (cognitive state, formula) which are a 
	list and a string, respectively.
	OUTPUT: A list.
	WHAT IT DOES: Given the cognitive state, it looks through
	each world in US and checks whether the formula is true there.
	If so, it adds it to a list. The list at the end will be the
	proposition denoted by the formula.
	"""

	proposition = []
	for world in cogstate:
		if formulaIsTrue(world, formula):
			proposition.append(world[meta][name])
	return proposition

def test():
	u = {
		meta: {
			name: 'john',
			FS: True,
			US: True
		},
		values: {
			'p': True,
			'q': False,
			'r': True
		}
	}
	v = {
		meta: {
			name: 'larry',
			FS: True,
			US: False
		},
		values: {
			'p': False,
			'q': True,
			'r': False
		}
	}
	cogstate = [u, v]
	pprint(propositionFromFormula(cogstate, "(p)|(q)"))

test()