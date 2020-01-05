from resources.Common import Common

class LogicalSubstraction(Common):

    def integerSubtraction(self, a, b):
        ''' This method substract two integers. The result can be returned in
        base 2 (binary), 10 (decimal) or 16 (hexadecimal), depending on the
        self.base value.

        Attributes:
            :a: First integer.
            :b: Second integer.

        Examples:
            :83 - 150:

                # Standard form:
                ls.LogicalSubstraction(base).integerSubtraction(a, b)

                # Base-2 numeral system or binary:
                ls.LogicalSubstraction(2).integerSubtraction('01010011', '10010110')
                # Returns 0b1001110

                # Base-10 numeral system or ecimal:
                ls.LogicalSubstraction(10).integerSubtraction('83', '150')
                # Returns 78

                # Base-16 numeral system or hexadecimal:
                ls.LogicalSubstraction(16).integerSubtraction('53', '96')
                # Returns 0x4e
        '''
        return self.baseTransform(int(a, self.base)-int(b, self.base))


    def modularSubstraction(self, a, b, n):
        ''' Method that performs the modular substraction of two integers.
        The result can be returned in base 2 (binary), 10 (decimal) or 16
        (hexadecimal), depending on the self.base value.

        Attributes:
            :a: First integer.
            :b: Second integer.
            :n: Module number.

        Examples:
            :83 - 150 mod 107:

                # Standard form:
                ls.LogicalSubstraction(base).modularSubstraction(a, b, n)

                # Base-2 numeral system or binary:
                ls.LogicalSubstraction(2).modularSubstraction('01010011', '10010110', '1101011')
                # Returns 0b1

                # Base-10 numeral system or ecimal:
                ls.LogicalSubstraction(10).modularSubstraction('83', '150', '107')
                # Returns 1

                # Base-16 numeral system or hexadecimal:
                ls.LogicalSubstraction(16).modularSubstraction('53', '96', '6B')
                # Returns 0x1
        '''
        return self.baseTransform((int(a, self.base)-int(b, self.base))%int(n, self.base))
