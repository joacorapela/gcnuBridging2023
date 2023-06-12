
"""
Example 8.1
===========

"""

import numpy as np

#%%
# This function draws a sample from the sample space
#
def sample():
    two_dice = np.random.randint(low=1, high=7, size=2)
    return two_dice

#%%
# This function checks if the sample belong to the unconditioned event
#
def sample_in_unconditioned_event(two_dice):
    # is any of the two dice equal to six?
    answer = two_dice[0] == 6 or two_dice[1] == 6
    return answer

#%%
# This function checks if the sample belong to the conditioned event
#
def sample_in_conditioned_event(two_dice):
    answer = two_dice[0] == 6 and two_dice[1] == 6
    return answer

#%%
# Below we draw many samples, check if each sample belongs to the event, and
# computes the probability of the event as the frequency of drawn samples
# belonging to the event.
n_samples=1000000

n_samples_in_unconditioned_event = 0
n_samples_in_conditioned_event = 0
for i in range(n_samples):
    a_sample = sample()
    if sample_in_unconditioned_event(a_sample):
        n_samples_in_unconditioned_event += 1
    if sample_in_conditioned_event(a_sample):
        n_samples_in_conditioned_event += 1
p_event = n_samples_in_conditioned_event/n_samples_in_unconditioned_event

print(f"probability {p_event}, "
      f"estimated from {n_samples} simulations")
