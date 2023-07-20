#!/bin/csh

foreach n (3 5 10 50 100 1000)
    python doExSubmarine_b_sol.py --n_samples $n
    python doExSubmarine_d_sol.py --n_samples $n
end
