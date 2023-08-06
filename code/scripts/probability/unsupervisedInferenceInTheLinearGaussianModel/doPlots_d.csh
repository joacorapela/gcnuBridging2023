#!/bin/csh

foreach n (1 2 3 4 5 10 100 1000)
    python doExSubmarine_b_sol.py --n_samples $n
    python doExSubmarine_d_sol.py --n_samples $n
end
