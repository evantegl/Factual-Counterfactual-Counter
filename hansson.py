# imports
from pprint import pprint
from genworlds import worldgen
from updates import updateFormula, updateLaw
from counterfactual import ifItHadBeenTheCase
from subprocess import call
from texoutput import *

# Start the tex file
out = texheader("Hansson's Hamburger puzzle", "The Factual Counterfactual Counter")

# Need propositional letters for "seeing a man walking with a hamburger",
# "snackbar A is open" and "snackbar B is open".
alphabet = ["p", "q", "r"]

# Now we generate the universe
W = worldgen(alphabet)
out += texify(W)

# Update with the fact that we see the man
W = updateFormula(W, "r")
out += texify(W)

# Update with the law that if we see a man with a hamburger, he must have
# got it at one of the snackbars
W = updateLaw(W, "(r)>((p)|(q))")
out += texify(W)

# Update since we see A is open
W = updateFormula(W, "p")
out += texify(W)

# Compute the counterfactual
W = ifItHadBeenTheCase(W, "~(p)")
out += texify(W)

# Finish the tex file
out += texfooter()
try:
	 f = open("hansson.tex", "w")
	 try:
		  f.write(out) # Write a string to a file
	 finally:
		  f.close()
except IOError:
	 pass

call(["pdflatex", "-interaction=batchmode", "hansson.tex"])