
import sys
import random
import argparse
import numpy as np

def sample():
    sample = np.random.randint(low=1, high=365+1, size=180)
    return sample

def sample_in_event(sample):
    BDs_in_range = sample[sample <= 23]
    answer = len(BDs_in_range) != len(np.unique(BDs_in_range))
    return answer

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_samples", type=int, default=100000,
                        help="number of samples")
    args = parser.parse_args()

    n_samples = args.n_samples

    n_samples_in_event = 0
    for i in range(n_samples):
        print(f"Sample {i}")
        a_sample = sample()
        if sample_in_event(a_sample):
            n_samples_in_event += 1
    p_event = n_samples_in_event / n_samples

    print(f"probability {p_event}, "
          f"estimated from {n_samples} simulations")

if __name__ == "__main__":
   main(sys.argv)
