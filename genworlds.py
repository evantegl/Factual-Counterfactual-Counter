import itertools

truthvalues=[1,0]

def worldgen(lang): # generate all possible worlds for some propositions
    result=[]
    worldname=0
    truthtable = itertools.product(truthvalues, repeat=len(lang))
    for line in truthtable:
	worldname=worldname+1
	world={}
	world["meta"]={}
	world["values"]={}
	world["meta"]["NAME"]=worldname
	world["meta"]["US"]=True
	world["meta"]["FS"]=True
	for j in range(len(lang)):
	    world["values"][lang[j]]=line[j]
	result.append(world)
    return result
