from genworlds import sitgen
from basis import getAllBases,Forceable
from utilities import subset, getWorldByName
from genworlds import sitgen, subsitgen

def retractOnWorld(cogstate,worldname,proposition):
	"""
	INPUT: a triple (cognitive state, worldname, proposition)
	OUTPUT: array of worlds
	WHAT IT DOES: Definition 4 (i)
	"""
	result=[]
	world=getWorldByName(worldname,cogstate)
	for situation in sitgen(world): # s
		if Forceable(situation, proposition, cogstate):
			continue # s may not force P
		adding=False
		for basis in getAllBases(world,cogstate): # s'
			if not subset(situation,basis):
				continue # s is has to be a subset of s'
			Maximal=True
			for t in subsitgen(basis):
				if Forceable(situation, proposition, cogstate):
					continue # t may not force P
				if subset(situation,t):
					if situation != t:
						Maximal=False
			if not Maximal:
				continue # s should be a maximal subset of s'
			adding=True
		if adding:
			result.append(situation)
	return result

def retractOnState(cogstate,proposition):
	"""
	INPUT: a pair (cognitive state, proposition)
	OUTPUT: cognitive state
	WHAT IT DOES: Definition 4 (ii)
	"""
	result=[]
	for world in cogstate:
		newworld={}  # do not shoot ourselves in the foot
		newworld["values"]=dict(world["values"])
		newworld["meta"]=dict(world["meta"])
		addingToFS=False
		if world["meta"]["US"]:
			for biworld in cogstate:
				if biworld["meta"]["FS"]:
					biretract=retractOnWorld(cogstate,biworld["meta"]["name"],proposition)
					for s in biretract:
						if subset(s,world):
							addingToFS=True
		newworld["meta"]["FS"]=addingToFS
		result.append(dict(newworld))
	return result









