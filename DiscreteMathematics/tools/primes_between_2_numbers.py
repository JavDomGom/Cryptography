import math


def per_diff(a, b):
    return round((b*100)/a, 2)


for i in range(5, 12+1):
    x = pow(2, i)
    lnx = round(math.log(x), 2)
    y = round(x/lnx, 2)
    print(
        f'[2, 2^{i:<2}] = {x:<4}\tx/ln x = {x}/{lnx} = {y} \t{per_diff(x, y)}%'
    )
