from pprint import pprint
from genworlds import *
from truthchecker import *

language=['p', 'q', 'r']

worlds=worldgen(language)

print "our worlds:"
pprint(worlds)

formula="(r)&((q)|(~(q)))"
print "where is",formula,"true?"
for world in worlds:
  pprint(world)
  print tiw(world,formula)
