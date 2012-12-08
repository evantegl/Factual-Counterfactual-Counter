# from python
from subprocess import call
# our libraries
from genworlds import *
from texoutput import *
from updates import *

out=texheader("Hansson's Hamburger puzzle","The factual counterfactual checker")

out+="Let $p$, $q$ and $r$ stand for the facts that we saw the man with the \
hamburger, snackbar A is open and snackbar B is open, respectively."
language=['p','q','r']

out+="\n\n0. The neutral cognitive state:\\\\"
s0=worldgen(language)
out+=texify(s0,language)

out+="\n\n1. We update with the fact $ r $:\\\\"
s1=updateFormula(s0, "r")
out+=texify(s1,language)

out+="\n\n2. We update with the law that hamburgers must have been bought somewhere:"
out+="$ r \\to ( p \\lor q ) $:\\\\"
s2=updateLaw(s0, "(r)>((p)|(q))")
out+=texify(s2,language)

out+=texfooter()

try:
    f = open("example-texoutput.tex", "w")
    try:
        f.write(out) # Write a string to a file
    finally:
        f.close()
except IOError:
    pass

call(["pdflatex", "-interaction=batchmode", "example-texoutput.tex"])
