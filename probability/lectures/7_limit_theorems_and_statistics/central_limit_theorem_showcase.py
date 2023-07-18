
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
import copy

import scipy.stats

# PMF of Uniform of a fair 6sided die
pmf_uniform = np.array([1/6] * 6)

# PMF of the sum of two dice
pmf_2uniform = np.convolve(pmf_uniform, pmf_uniform)
plt.scatter(np.arange(2, len(pmf_2uniform) + 2), pmf_2uniform)

# But do the convolution manually to see what is going on
# One way (sliding arrays way)
pmf_2uniform = []
pmf_padded = np.zeros(3*len(pmf_uniform))
pmf_padded[len(pmf_uniform):2*len(pmf_uniform)] = pmf_uniform
for i in np.arange(2*len(pmf_uniform) + 1):
    l = np.sum(pmf_uniform * pmf_padded[2*len(pmf_uniform) - i : 3*len(pmf_uniform) - i])
    pmf_2uniform.append(l)
plt.scatter(np.arange(2, len(pmf_2uniform) + 2), pmf_2uniform)

# Another way (following the equation way)
pmf_2uniform = np.zeros(len(pmf_uniform) + len(pmf_uniform) - 1)
for i in np.arange(len(pmf_uniform)):
    for j in np.arange(len(pmf_uniform)):
        pmf_2uniform[i + j] += pmf_uniform[i] * pmf_uniform[j]


# PMF for the sum of 3 dice (because convolution is associative)
pmf_3uniform = np.convolve(pmf_2uniform, pmf_uniform)
plt.scatter(np.arange(3, len(pmf_3uniform) + 3), pmf_3uniform)


# Function of the PMF for the sum of n dice
def pmf_for_sum_of_n_uniforms(pmf, n):
    assert n >= 2, print('You must add at least two RVs')
    temp = copy.copy(pmf)
    for i in np.arange(n - 1):
        temp = np.convolve(pmf, temp)
    return temp


# Test this
n = 30
pmf_conv = pmf_for_sum_of_n_uniforms(pmf_uniform, n)
plt.scatter(np.arange(n, len(pmf_conv) + n), pmf_conv)


# Now do the same with a truncated geometric pmf with p=0.5 and k=8 (after k=8, pmf(k>8)=0)
pmf_geo = []
for k in np.arange(1, 9):
    pmf_geo.append(scipy.stats.geom.pmf(p=0.5, k=k))

# And now check this out
n = 30
pmf_conv = pmf_for_sum_of_n_uniforms(pmf_geo, n)
plt.scatter(np.arange(n, len(pmf_conv) + n), pmf_conv)