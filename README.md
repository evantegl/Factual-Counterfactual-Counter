Counting counterfactuals, factually.
====================================

Taken from [Making Counterfactual Assumptions](http://staff.science.uva.nl/~veltman/papers/FVeltman-mca.pdf) by Frank Veltman.

USAGE
-----

Following [MCA](http://staff.science.uva.nl/~veltman/papers/FVeltman-mca.pdf), alphabets are defined as lists of single-character strings.

You can use the `worldgen` function from `genworlds.py` to automatically generate the truth table corresponding to your chosen alphabet.

Formulas use a simple syntax; logical symbols are `~, |, &, >, (, )` corresponding to negation, disjunction, conjunction, implication and parentheses, respectively. Everything must be enclosed by parentheses per the usual rules, **except the main connective**. Thus `(~(p))|(q)` is correct, but `((p)>(q))` is not.

Formula updates on states are done using the `updateFormula` function from `updates.py` and law updates are done using `updateLaw`.

Counterfactual assumptions are done using `ifItHadBeenTheCase` from `counterfactual.py`.