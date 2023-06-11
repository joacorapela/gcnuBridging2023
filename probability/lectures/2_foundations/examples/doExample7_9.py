
import math
import scipy.special

answer_a = math.factorial(4)/(scipy.special.binom(8,2)*scipy.special.binom(6,2)*scipy.special.binom(4,2))
print("(a) {:f}".format(answer_a))
pB_E = ((scipy.special.binom(6,2)*scipy.special.binom(4,2))/math.factorial(3))*(math.factorial(4)/(scipy.special.binom(8,2)*scipy.special.binom(6,2)*scipy.special.binom(4,2)))
pB_E_B_G = ((scipy.special.binom(4,2))/math.factorial(2))*(math.factorial(4)/(scipy.special.binom(8,2)*scipy.special.binom(6,2)*scipy.special.binom(4,2)))
print("(b) pB_E={:f}".format(pB_E))
print("(b) pB_E_B_G={:f}".format(pB_E_B_G))
print("(a) {:f}".format(2*pB_E-pB_E_B_G))
