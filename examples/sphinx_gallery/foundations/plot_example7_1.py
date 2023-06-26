
"""
Example 7.1: John, Pedro and Rosita's dice game
===============================================

"""

import numpy as np

#%%
# This function draws a sample from the sample space
#
def sample():
    draws = np.random.randint(low=1, high=7, size=3)
    return draws


#%%
# This function checks if the sample belong to the event
#
def sample_in_event(sample):
    answer = sample[2]==sample[0]+sample[1]
    return answer


#%%
# Below we draw many samples, check if each sample belongs to the event, and
# computes the probability of the event as the frequency of drawn samples
# belonging to the event.

n_samples = 1000000

n_samples_in_event = 0
for i in range(n_samples):
    draws = sample()
    if sample_in_event(sample=draws):
        n_samples_in_event += 1
p_event = n_samples_in_event/n_samples

print(f"probability {p_event}, "
      f"estimated from {n_samples} simulations")

