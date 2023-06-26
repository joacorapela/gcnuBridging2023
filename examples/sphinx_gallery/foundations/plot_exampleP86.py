
"""
Example p86: dice roll and coint tosses
=======================================

"""

import numpy as np

#%%
# This function draws a sample from the sample space
#
def sample():
    dice_roll = np.random.randint(low=1, high=7, size=1)[0]
    coin_tosses = [None] * dice_roll
    for i in range(dice_roll):
        uniform_sample = np.random.uniform()
        if uniform_sample < 0.5:
            coin_tosses[i] = "H"
        else:
            coin_tosses[i] = "T"
    return dice_roll, coin_tosses

#%%
# This function checks if the sample belongs to the event
#
def sample_in_event(dice_coins):
    # no coin toss is a head (H)
    coin_tosses = dice_coins[1]
    for coin_toss in coin_tosses:
        if coin_toss == "H":
            return False
    return True

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
