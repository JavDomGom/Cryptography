def transformaBase(self, x, division=False):
    ''' Método que recibe un número entero de tipo int() y dependiendo del
    valor de la variable self.base lo transforma en un número de tipo bin(),
    int() o hex().

    Atributos:
        :x: Número entero de tipo int() a transformar.
    '''
    if self.base == 2:
        return bin(x)
    elif self.base == 10 and division:
        return float(x)
    elif self.base == 10:
        return int(x)
    elif self.base == 16:
        return hex(x)
