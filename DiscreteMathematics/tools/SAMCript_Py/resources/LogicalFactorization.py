from resources.Common import Common

class LogicalFactorization(Common):

    def factorization(self, n):
        
        from math import gcd

        n = int(n, self.base)

        def get_factor(n):
            x_fixed = 2
            x = 2
            cycle_size = 2
            factor = 1

            while factor == 1:
                for count in range(cycle_size):
                    if factor > 1: break
                    x = (x * x + 1) % n
                    factor = gcd(x - x_fixed, n)

                cycle_size *= 2
                x_fixed = x

            return factor

        factors = []
        while n > 1:
            next = get_factor(n)
            factors.append(self.baseTransform(next))
            n //= next
        return sorted(factors)
