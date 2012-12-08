import itertools

truthvalues=[0,1]

def worldgen(language): #
  	"""
	INPUT: a language
	OUTPUT: a cognitive state
	WHAT IT DOES: generates the neutral coginitve state which includes
		all 2^n possible worlds for n propositions.
	"""
	result=[]
	worldname=-1
	truthtable = itertools.product(truthvalues, repeat=len(language))
	for line in truthtable:
		worldname=worldname+1
		world={}
		world["meta"]={}
		world["values"]={}
		world["meta"]["name"]="w_"+str(worldname)
		world["meta"]["US"]=True
		world["meta"]["FS"]=True
		for j in range(len(language)):
			world["values"][language[j]]=line[j]
		result.append(world)
	return result

def sitgen(world):
  	"""
	INPUT: a pair (world, language)
	OUTPUT: an array of situations
	WHAT IT DOES: generates all 2^n situations which are a subset of
		the world where n is the number of propositions.
	"""
	# Reconstruct the language from the world
	language = world["values"].keys()
	#Main stuff
	result=[]
	n=len(language)
	truthtable = itertools.product([True,False], repeat=n)
	for line in truthtable:
		situation={}
		for i in range(n):
			if line[i]:
				situation[language[i]]=world["values"][language[i]]
		result.append(situation)
	return result

def subsitgen(situation):
  	"""
	INPUT: a situation
	OUTPUT: an array of situations
	WHAT IT DOES: generates all 2^m - 1 proper subsituations
		where m is the number of facts in the situation.
	"""
	result=[]
	situation = situation.items() # convert the dictionary to an array
	m=len(situation)
	truthtable = itertools.product([True,False], repeat=m)
	for line in truthtable:
		subsituation={}
		for i in range(m):
			if line[i]:
				subsituation[situation[i][0]]=situation[i][1]
		result.append(subsituation)
	result.pop(0)
	return result


