import sys
import math

def main(argv):
    # a
    size_Omega = math.comb(8, 2)*math.comb(6, 2)*math.comb(4, 2)/math.factorial(4)
    size_A = 1
    answer_a = size_A/size_Omega;
    print(f"answer_a = {answer_a}")
    # b
    answer_b = 4.0/math.comb(8, 2)*(2-3.0/math.comb(6, 2))
    print(f"answer_b = {answer_b}")

if __name__ == "__main__":
    main(sys.argv)
