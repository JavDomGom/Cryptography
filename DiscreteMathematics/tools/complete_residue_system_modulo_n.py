from random import randint

Z = range(2, 11+1)

for n in Z:
    CRS1 = {i for i in range(n)}
    CRS2 = []
    for r in CRS1:
        while True:
            k = randint(-99, 99)
            if (k % n) == r:
                CRS2.append(k)
                break

    print(f'CRS1({n}) = {CRS1} = CCR2 = {CRS2}')
