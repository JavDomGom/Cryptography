from resources.Common import Common

class LogicalAddition(Common):

    def integerAddition(self, a, b):
        ''' This method adds two integers. The result can be returned in
        base 2 (binary), 10 (decimal) or 16 (hexadecimal), depending on the
        self.base value.

        Attributes:
            :a: First integer.
            :b: Second integer.

        Examples:
            :83 + 150:

                # Standard form:
                la.LogicalAddition(base).integerAddition(a, b)

                # Base-2 numeral system or binary:
                la.LogicalAddition(2).integerAddition('01010011', '10010110')
                # Returns 0b11101001

                # Base-10 numeral system or ecimal:
                la.LogicalAddition(10).integerAddition('83', '150')
                # Returns 233

                # Base-16 numeral system or hexadecimal:
                la.LogicalAddition(16).integerAddition('53', '96')
                # Returns 0xe9
        '''
        return self.baseTransform(int(a, self.base)+int(b, self.base))


    def modularAddition(self, a, b, n):
        ''' Method that performs the modular addition of two integers.
        The result can be returned in base 2 (binary), 10 (decimal) or 16
        (hexadecimal), depending on the self.base value.

        Attributes:
            :a: First integer.
            :b: Second integer.
            :n: Module number.

        Examples:
            :83 + 150 mod 107:

                # Standard form:
                la.LogicalAddition(base).modularAddition(a, b, n)

                # Base-2 numeral system or binary:
                la.LogicalAddition(2).modularAddition('01010011', '10010110', '1101011')
                # Returns 0b10010

                # Base-10 numeral system or ecimal:
                la.LogicalAddition(10).modularAddition('83', '150', '107')
                # Returns 19

                # Base-16 numeral system or hexadecimal:
                la.LogicalAddition(16).modularAddition('53', '96', '6B')
                # Returns 0x13
        '''
        return self.baseTransform((int(a, self.base)+int(b, self.base))%int(n, self.base))