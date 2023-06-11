
"""
Example 7.9
=================================

"""

import sys
import numpy as np

#%%
# This function draws a sample from the sample space
#
def sample(teams=["E1", "E2", "G1", "G2", "I1", "I2", "S1", "S2"]):
    permutation_indices = np.random.permutation(len(teams))
    set_of_matches = [teams[i] for i in permutation_indices]
    return set_of_matches

#%%
# This function checks if the sample belong to the event
#
def sample_in_event(set_of_matches):
    answer = ((set_of_matches[0][0] == set_of_matches[1][0]) and
              (set_of_matches[2][0] == set_of_matches[3][0]) and
              (set_of_matches[4][0] == set_of_matches[5][0]) and
              (set_of_matches[6][0] == set_of_matches[7][0]))
    return answer

#%%
# Below we draw many samples, check if each sample belongs to the event, and
# computes the probability of the event as the frequency of drawn samples
# belonging to the event.
n_samples=10000000

n_samples_in_event = 0
for i in range(n_samples):
    a_sample = sample()
    if sample_in_event(a_sample):
        n_samples_in_event += 1
p_event = n_samples_in_event/n_samples

print(f"probability {p_event}, "
      f"estimated from {n_samples} simulations")
