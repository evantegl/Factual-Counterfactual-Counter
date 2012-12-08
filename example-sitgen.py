from genworlds import *
from pprint import pprint

language = ['p','q','r']

cogstate = worldgen(language)

pprint(cogstate[2])

situationlist=sitgen(cogstate[2],language)

pprint(situationlist)
