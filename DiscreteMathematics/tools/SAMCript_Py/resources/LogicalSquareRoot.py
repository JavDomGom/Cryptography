from resources.Common import Common

class LogicalSquareRoot(Common):

    def integerSquareRoot(self, x):
        ''' This method method returns the square root of x for x > 0. The
        result can be returned in base 2 (binary), 10 (decimal) or 16
        (hexadecimal), depending on the self.base value.

        Attributes:
            :x: Numeric expression.

        Examples:
            :√x:

                # Standard form:
                lsr.LogicalSquareRoot(base).integerSquareRoot(a)

                # Base-2 numeral system or binary:
                lsr.LogicalSquareRoot(2).integerSquareRoot('110110011001')
                # Returns 0b111011

                # Base-10 numeral system or ecimal:
                lsr.LogicalSquareRoot(10).integerSquareRoot('3481')
                # Returns 59

                # Base-16 numeral system or hexadecimal:
                lsr.LogicalSquareRoot(16).integerSquareRoot('D99')
                # Returns 0x3b
        '''
        import math

        return self.baseTransform(int(math.sqrt(int(x, self.base))))
