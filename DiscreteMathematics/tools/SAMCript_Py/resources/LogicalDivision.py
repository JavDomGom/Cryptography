from resources.Common import Common

class LogicalDivision(Common):

    def bin2float(self, b):
        ''' Convert binary string to a float.

        Attributes:
            :b: Binary string to transform.
        '''
        from codecs import decode
        import struct

        h = int(b, 2).to_bytes(8, byteorder="big")
        return struct.unpack('>d', h)[0]


    def float2bin(self, f):
        ''' Convert float to 64-bit binary string.

        Attributes:
            :f: Float number to transform.
        '''
        import struct

        [d] = struct.unpack(">Q", struct.pack(">d", f))
        return f'{d:064b}'


    def integerDivision(self, a, b):
        ''' This method divides two integers. The result can be returned in
        base 2 (binary), 10 (decimal) or 16 (hexadecimal), depending on the
        self.base value.

        Attributes:
            :a: First integer.
            :b: Second integer.

        Examples:
            :89 / 67:

                # Standard form:
                ld.LogicalDivision(base).integerDivision(a, b)

                # Base-2 numeral system or binary:
                ld.LogicalDivision(2).integerDivision('01011001', '01000011')
                # Returns 0b1011101001011

                # Base-10 numeral system or decimal:
                ld.LogicalDivision(10).integerDivision('89', '67')
                # Returns 5963

                # Base-16 numeral system or hexadecimal:
                ld.LogicalDivision(16).integerDivision('59', '43')
                # Returns 0x174b
        '''
        return self.baseTransform(int(a, self.base)/int(b, self.base), True)
