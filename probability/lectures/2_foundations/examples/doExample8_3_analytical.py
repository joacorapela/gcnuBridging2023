
P_E = 0
for i in range(1, 13):
    for j in range(1, 14-i):
        for k in range(1, 15-(i+j)):
            P_E += 1.0/(16 * (16-i) * (16-(i+j)))
print(f"P(E)={P_E}")
