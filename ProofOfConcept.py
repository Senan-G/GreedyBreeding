data = [[0]*10 for _ in range(10)]

print(data)

for R1 in range(10):
    for C1 in range(10):
        R2 = R1 + 1
        while R2 < 10:
            C2 = C1 + 1
            while C2 < 10:
                print(R1, C1, R2, C2)
                C2 += 1
            R2 += 1