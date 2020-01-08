from resources.Common import Common

class LogicalMultiplication(Common):

    def integerMultiplication(self, a, b):
        ''' This method multiplies two integers. The result can be returned in
        base 2 (binary), 10 (decimal) or 16 (hexadecimal), depending on the
        self.base value.

        Attributes:
            :a: First integer.
            :b: Second integer.

        Examples:
            :a * b:

                # Standard form:
                lm.LogicalMultiplication(base).integerMultiplication(a, b)

                # Base-2 numeral system or binary:
                lm.LogicalMultiplication(2).integerMultiplication('01011001', '01000011')
                # Returns 0b1011101001011

                # Base-10 numeral system or decimal:
                lm.LogicalMultiplication(10).integerMultiplication('89', '67')
                # Returns 5963

                # Base-16 numeral system or hexadecimal:
                lm.LogicalMultiplication(16).integerMultiplication('59', '43')
                # Returns 0x174b
        '''
        return self.baseTransform(int(a, self.base)*int(b, self.base))


    def modularMultiplication(self, a, b, n):
        ''' Method that performs the modular multiplication of two integers.
        The result can be returned in base 2 (binary), 10 (decimal) or 16
        (hexadecimal), depending on the self.base value.

        Attributes:
            :a: First integer.
            :b: Second integer.
            :n: Module number.

        Examples:
            :a * b mod n:

                # Standard form:
                lm.LogicalMultiplication(base).modularMultiplication(a, b, n)

                # Base-2 numeral system or binary:
                lm.LogicalMultiplication(2).modularMultiplication('01011001', '01000011', '01111001')
                # Returns 0b100010

                # Base-10 numeral system or decimal:
                lm.LogicalMultiplication(10).modularMultiplication('89', '67', '121')
                # Returns 34

                # Base-16 numeral system or hexadecimal:
                lm.LogicalMultiplication(16).modularMultiplication('59', '43', '79')
                # Returns 0x22
        '''
        return self.baseTransform((int(a, self.base)*int(b, self.base))%int(n, self.base))
