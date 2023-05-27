
import sys
import math

def main(argv):
    answer = 179
    for i in range(2, 181):
        print(f"i={i}")
        aux_ratio = 1.0
        for j in range(i):
            print(f"j={i}")
            aux_ratio *= 23-i / 365.0
        # answer -= (math.comb(180, i) * math.comb(23, i)**2 * math.factorial(i)**2 1.0/(23 * 365)**i * (1- 23.0/365)**(180-i))
        answer -= math.comb(180, i) * math.comb(23, i)**2 * math.factorial(i)**2 * 1.0 / (23 * 365)**i * (1- 23.0/365)**(180-i)
    print(answer)

if __name__ == "__main__":
   main(sys.argv)
