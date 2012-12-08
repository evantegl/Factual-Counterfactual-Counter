from pprint import pprint
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
		#print ""
		#pprint(situation)
		if Forceable(situation, proposition, cogstate):
			#print "BAD: does force the proposition"
			continue # s may not force P
		#print "NICE: does not force the proposition"
		adding=False
		for basis in getAllBases(world,cogstate): # s'
			#print "  checking this basis:"
			#pprint(basis)
			if not subset(situation,basis):
				continue # s is has to be a subset of s'
			#print "  it is a subset!"
			Maximal=True
			for t in subsitgen(basis):
				if Forceable(situation, proposition, cogstate):
					continue # t may not force P
				if subset(situation,t):
					if situation != t:
						Maximal=False
			if not Maximal:
				#print "  but it is not maximal!"
				continue # s should be a maximal subset of s'
			#print "  and it is maximal!"
			adding=True
		if adding:
			result.append(situation)
		#print "added."
	#print ""
	return result

def retractOnState(cogstate,proposition):
	return False