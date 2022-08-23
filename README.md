# 100-prisoners-problem

If you happen to be unfamiliar with the 100 prisoners problem:

- Veritasium has made a thorough Youtube video presenting
and explaining the problem as well as the solution demonstrated in this code: <br>
https://www.youtube.com/watch?v=iSNsgj1OCLA <br>
- and here's the Wikipedia article for a dry overview:<br>
https://en.wikipedia.org/wiki/100_prisoners_problem

The bottom line is, the chance of winning taking a random approach would equate to <br>
(1/2)^100 ≈ 8e-33 % <br>
vs. the proposed solution resulting in a chance of roughly a third.

The enormous difference between the two probabilities seems unreasonably large, 
and the chance of success at a third superficially seems dubious at best, 
since the chance for only two people choosing randomly would already be lower at (1/2)^2. = 1/4.

Therefore I wanted to test it out and see if things add up
and figured other people may be interested in seeing it for themselves.

### The code:
There are two main files, one Jupyter Notebook, one normal Python file, but both are essentially identical.
I personally find the notebook easier and more enjoyable to work and play around with.

The probability of success can be computed using the function

    compute_pbb(repeats, n_total)

where **repeats** is the number of times the experiment is run and **n_total** the number of prisoners.

- Any natural number can be chosen for **repeats**, while a higher number of runs will result in a more accurate probability for the given test.
- **n_total** can be assigned to any positive even number, so the problem can be tested with for example a thousand prisoners or only fifty, 
while the allowed number of boxes each prisoner may choose remains at half of the number of prisoners.