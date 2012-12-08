# the imports
from retraction import retractOnState as retract
from utilities import negateFormula as lnot
from propositions import propositionFromFormula as proposition
from updates import updateFormula as update

def ifItHadBeenTheCase(cogstate, formula):
	"""
	INPUT: a cognitive state and a formula
	OUTPUT: a cognitive state
	WHAT IT DOES: given a formula \phi, it
	retracts ~\phi and then updates with \phi
	"""
	# It's so pretty!
	return update(retract(proposition(lnot(formula))), formula)