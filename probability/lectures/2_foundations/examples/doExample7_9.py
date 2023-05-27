
import sys
import argparse
import random
import numpy as np

def sample_one_set_of_matches(teams=["E1", "E2", "G1", "G2", "I1", "I2", "S1",
                                     "S2"]):
    permutation_indices = np.random.permutation(len(teams))
    set_of_matches = [teams[i] for i in permutation_indices]
    return set_of_matches

def in_event_countries_against_each_other(set_of_matches):
    answer = ((set_of_matches[0][0] == set_of_matches[1][0]) &
              (set_of_matches[2][0] == set_of_matches[3][0]) &
              (set_of_matches[4][0] == set_of_matches[5][0]) &
              (set_of_matches[6][0] == set_of_matches[7][0]))
    return answer

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_samples", type=int, default=10000000,
                        help="number of samples")
    args = parser.parse_args()

    n_samples = args.n_samples

    n_event_countries_against_each_other = 0
    for i in range(n_samples):
        set_of_matches = sample_one_set_of_matches()
        if in_event_countries_against_each_other(set_of_matches=set_of_matches):
            n_event_countries_against_each_other += 1
    p_event_countries_against_each_other = \
        n_event_countries_against_each_other/n_samples

    print(f"probability {p_event_countries_against_each_other}, "
          f"estimated from {n_samples} simulations")

if __name__ == "__main__":
   main(sys.argv)
