from updates import *

w0 = {
	'meta': {
		'name': "w0",
		'FS': True,
		'US': True
	},
	'values': {
		'p': True,
		'q': True,
		'r': True
	}
}
w1 = {
	'meta': {
		'name': "w1",
		'FS': True,
		'US': True
	},
	'values': {
		'p': True,
		'q': True,
		'r': True
	}
}
cogstate = [w0, w0, w1, w0, w0, w0]

print formulaIsConsistent(cogstate,"q")

newcogstate = updateFormula(cogstate, "p")
pprint(newcogstate)