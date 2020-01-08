from resources.Common import Common

class LogicalLCM(Common):

    def lcm(self, a, b):
        from math import gcd

        return a * b // gcd(a, b)

    def leastCommonMultiple(self, *args):
        ''' This method returns the least common multiple of all the numbers
        that you pass as argument.

        Attributes:
            :*args: 2 or more numbers.

        Examples:
            :lcm(a, b):

                # Standard form:
                lgcd.LogicalLCM(base).leastCommonMultiple(a, b)

                # Base-2 numeral system or binary:
                lgcd.LogicalLCM(2).leastCommonMultiple('110100011011', '1111011001')
                # Returns 0b101

                # Base-10 numeral system or ecimal:
                lgcd.LogicalLCM(10).leastCommonMultiple('3355', '985')
                # Returns 5

                # Base-16 numeral system or hexadecimal:
                lgcd.LogicalLCM(16).leastCommonMultiple('D1B', '3D9'))
                # Returns 0x5
        '''
        from functools import reduce

        return self.baseTransform(
            reduce(self.lcm, map(lambda n:int(n, self.base), args))
        )
