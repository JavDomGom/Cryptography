class DivisionLogica():
    from resources.common import transformaBase as tb

    def __init__(self, base):
        ''' Constructor de la clase.

        Atributos:
            :base: La base numérica que se empleará en los cálculos de la clase.
        '''
        self.base = base


    def divisionEnteros(self, a, b):
        ''' Método que realiza la división de dos números enteros. El
        resultado se puede devolver en base 2 (binario), 10 (decimal) o 16
        (hexadecimal), dependiendo del valor de la variable self.base.

        Atributos:
            :a: Primer número entero.
            :b: Segundo número entero.

        Ejemplos:
            :89 / 67:

                # Forma estándar:
                sl.DivisionLogica(base).divisionEnteros(a, b)

                # En base 2 o binario:
                sl.DivisionLogica(2).divisionEnteros('01011001', '01000011')
                # Devuelve 0b1011101001011

                # En base 10 o decimal:
                sl.DivisionLogica(10).divisionEnteros('89', '67')
                # Devuelve 5963

                # En base 16 o hexadecimal:
                sl.DivisionLogica(16).divisionEnteros('59', '43')
                # Devuelve 0x174b
        '''
        return self.tb(int(a, self.base)/int(b, self.base), True)
