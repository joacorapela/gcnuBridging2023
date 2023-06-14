
"""
Example 8.3: stranded tourists
==============================

"""

import numpy as np

#%%
# This function draws a sample from the sample space
#
def sample():
    n_guests_hotel_A = np.random.randint(low=0, high=16, size=1)
    n_guests_hotel_B = np.random.randint(low=0, high=16-n_guests_hotel_A, size=1)
    n_guests_hotel_C = np.random.randint(
        low=0, high=16-(n_guests_hotel_A+n_guests_hotel_B), size=1)
    n_guests_hotel_D = 15-(n_guests_hotel_A+n_guests_hotel_B+n_guests_hotel_C)
    answer = (n_guests_hotel_A, n_guests_hotel_B, n_guests_hotel_C,
              n_guests_hotel_D)
    return answer

#%%
# This function checks if the sample belongs to the event
#
def sample_in_event(assignments):
    # is any of the two dice equal to six?
    answer = (assignments[0] > 0 and assignments[1] > 0 and 
              assignments[2] > 0 and assignments[3] > 0)
    return answer

#%%
# Below we draw many samples, check if each sample belongs to the event, and
# computes the probability of the event as the frequency of drawn samples
# belonging to the event.
n_samples=100000

n_samples_in_event = 0
for i in range(n_samples):
    a_sample = sample()
    if sample_in_event(a_sample):
        n_samples_in_event += 1
p_event = n_samples_in_event/n_samples

print(f"probability {p_event}, "
      f"estimated from {n_samples} simulations")
