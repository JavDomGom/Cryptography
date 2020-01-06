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
            :159 - 77:

                # Standard form:
                ls.LogicalSubstraction(base).integerSubtraction(a, b)

                # Base-2 numeral system or binary:
                ls.LogicalSubstraction(2).integerSubtraction('10011111', '01001101')
                # Returns 0b1010010

                # Base-10 numeral system or ecimal:
                ls.LogicalSubstraction(10).integerSubtraction('159', '77')
                # Returns 82

                # Base-16 numeral system or hexadecimal:
                ls.LogicalSubstraction(16).integerSubtraction('9F', '4D')
                # Returns 0x52
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
            :159 - 77 mod 33:

                # Standard form:
                ls.LogicalSubstraction(base).modularSubstraction(a, b, n)

                # Base-2 numeral system or binary:
                ls.LogicalSubstraction(2).modularSubstraction('01010011', '10010110', '100001')
                # Returns 0b10000

                # Base-10 numeral system or decimal:
                ls.LogicalSubstraction(10).modularSubstraction('83', '150', '33')
                # Returns 16

                # Base-16 numeral system or hexadecimal:
                ls.LogicalSubstraction(16).modularSubstraction('53', '96', '21')
                # Returns 0x10
        '''
        return self.baseTransform((int(a, self.base)-int(b, self.base))%int(n, self.base))
