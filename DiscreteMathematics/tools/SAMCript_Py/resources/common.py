def baseTransform(self, x, isDivision=False):
    ''' Method that receives a int() number, and depending on the self.base
     value transforms it to bin(), int() or hex().

    Attributes:
        :x: int() number to transform.
    '''
    if self.base == 2:
        return bin(x)
    elif self.base == 10 and isDivision:
        return float(x)
    elif self.base == 10:
        return int(x)
    elif self.base == 16:
        return hex(x)
