from genworlds import *
from pprint import pprint

language = ['p','q','r']

cogstate = worldgen(language)

print "generating all situations which are subset of a world:"

pprint(cogstate[2])

situationlist=sitgen(cogstate[2],language)

pprint(situationlist)

print "generating all proper subsituations of a situation:"

sit = {'p': 0, 'q': 1, 'r': 0}

pprint(sit)

pprint(subsitgen(sit))