
import sys
import math

def pB(i):
    assert(0 <= i & i <= 180)
    aux_constant = 23.0 / 365
    answer = math.comb(180, i) * aux_constant**i * (1 - aux_constant)**(180 - i)
    return answer

def main(argv):
    answer = 1.0 - pB(0) - pB(1)
    aux_constant = 1 - 23.0 / 365
    for i in range(2, 23 + 1):
        aux_ratio = 1.0
        for j in range(i):
            aux_ratio *= (23 - j) / 23.0
        answer -= aux_ratio * pB(i)
    print(answer)

if __name__ == "__main__":
   main(sys.argv)
