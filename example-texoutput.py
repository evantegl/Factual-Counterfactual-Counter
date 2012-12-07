from genworlds import *
from texoutput import texify
from subprocess import call

language=['p', 'q', 'r']

worlds=worldgen(language)

source=texify(worlds,language)

try:
    f = open("example-texoutput.tex", "w")
    try:
        f.write(source) # Write a string to a file
    finally:
        f.close()
except IOError:
    pass

call(["pdflatex", "-interaction=batchmode", "example-texoutput.tex"])
