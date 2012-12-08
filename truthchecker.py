def chop(formula): # count brackets to get main connective and return subformulas
	"""
	INPUT: a formula
	OUTPUT: result as a triple: (connective, subleft, subright)
	WHAT IT DOES: Finds the main connective by counting brackets. It returns the two (or in case of negation: one) subformulas and the connective.
	"""
	min_pcount, pcount = 10000, 0
	conpos=0
	pos=0
	result={}
	for pos, c in enumerate(formula):
		if c == '(': pcount += 1
		if c == ')': pcount -= 1
		if (c == '~' or c == '&' or c=='|' or c==">"):
			if pcount < min_pcount:
				min_pcount = pcount
				result["connective"] = c
				conpos = pos
	if not conpos==0: # we only have a left subformula if it's not a negation
		result["subleft"]=formula[1:(conpos-1)]
	result["subright"]=formula[(conpos+2):-1]
	return result

def tiw(world,formula): # check whether a formula is true in world
	if len(formula)==1: # atomic
		return world["values"][formula]
	else:
		structure=chop(formula)
		if structure["connective"]=="~": # negation
			return not tiw(world,structure["subright"])
		if structure["connective"]=="&": # conjunction
			return ( tiw(world,structure["subleft"]) & tiw(world,structure["subright"]) )
		if structure["connective"]=="|": # disjunction
			return ( tiw(world,structure["subleft"]) | tiw(world,structure["subright"]) )
		if structure["connective"]==">": # disjunction
			return ( tiw(world,structure["subleft"]) <= tiw(world,structure["subright"]) )
