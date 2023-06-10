
"""
Example 7.7
=================================

"""

import sys
import numpy as np

#%%
# This function draws a sample from the sample space
#
def sample(n_draws):
    draws = np.random.randint(low=1, high=7, size=n_draws)
    return draws


#%%
# This function checks if the sample belong to the event
#
def sample_in_event(sample):
    index_six = np.where(sample==6)[0]
    if len(index_six)==0:
        return False
    return True


#%%
# Below we draw many samples, check if each sample belongs to the event, and
# computes the probability of the event as the frequency of drawn samples
# belong to the event.

n_samples = 10000
n_draws = 4

n_samples_in_event = 0
for i in range(n_samples):
    draws = sample(n_draws=n_draws)
    if sample_in_event(sample=draws):
        n_samples_in_event += 1
p_event = n_samples_in_event/n_samples

print(f"probability {p_event}, "
      f"estimated from {n_samples} simulations")

