from resources.Common import Common

class LogicalExponentiation(Common):

    def integerExponentiation(self, a, b):
        ''' Method that performs exponentiation of two integers. The result can
        be returned in base 2 (binary), 10 (decimal) or 16 (hexadecimal),
        depending on the self.base value.

        Attributes:
            :a: Exponentiation base.
            :b: Exponentiation power.

        Examples:
            :a ^ b:

                # Standard form:
                le.LogicalExponentiation(base).integerExponentiation(a, b)

                # Base-2 numeral system or binary:
                le.LogicalExponentiation(2).integerExponentiation('00010111', '00010011')
                # Returns 0b11110110111000011100001100100010110110100101111011010111011101111101101010011100000111

                # Base-10 numeral system or ecimal:
                le.LogicalExponentiation(10).integerExponentiation('23', '19')
                # Returns 74615470927590710561908487

                # Base-16 numeral system or hexadecimal:
                le.LogicalExponentiation(16).integerExponentiation('17', '13')
                # Returns 0x3db870c8b697b5ddf6a707
        '''
        return self.baseTransform(pow(int(a, self.base), int(b, self.base)))


    def modularExponentiation(self, a, b, n):
        ''' Method that performs the modular exponentiation of two integers.
        The result can be returned in base 2 (binary), 10 (decimal) or 16
        (hexadecimal), depending on the self.base value.

        Attributes:
            :a: Exponentiation base.
            :b: Exponentiation power.
            :n: Module number.

        Examples:
            :a ^ b mod n:

                # Standard form:
                le.LogicalExponentiation(base).modularExponentiation(a, b, n)

                # Base-2 numeral system or binary:
                le.LogicalExponentiation(2).modularExponentiation(''00010111', '00010011', '01011111')
                # Returns 0b101010

                # Base-10 numeral system or ecimal:
                le.LogicalExponentiation(10).modularExponentiation('23', '19', '95')
                # Returns 42

                # Base-16 numeral system or hexadecimal:
                le.LogicalExponentiation(16).modularExponentiation('17', '13', '5F')
                # Returns 0x2a
        '''
        return self.baseTransform(pow(int(a, self.base), int(b, self.base), int(n, self.base)))