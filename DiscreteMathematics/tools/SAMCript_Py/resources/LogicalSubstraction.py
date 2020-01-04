class RestaLogica():
    from resources.common import baseTransform as bt

    def __init__(self, base):
        ''' Constructor de la clase.

        Atributos:
            :base: La base numérica que se empleará en los cálculos de la clase.
        '''
        self.base = base


    def restaEnteros(self, a, b):
        ''' Método que realiza la resta de dos números enteros. El resultado se
        puede devolver en base 2 (binario), 10 (decimal) o 16 (hexadecimal),
        dependiendo del valor de la variable self.base.

        Atributos:
            :a: Primer número entero.
            :b: Segundo número entero.

        Ejemplos:
            :83 - 150:

                # Forma estándar:
                sl.RestaLogica(base).restaEnteros(a, b)

                # En base 2 o binario:
                sl.RestaLogica(2).restaEnteros('01010011', '10010110')
                # Devuelve 0b1001110

                # En base 10 o decimal:
                sl.RestaLogica(10).restaEnteros('83', '150')
                # Devuelve 78

                # En base 16 o hexadecimal:
                sl.RestaLogica(16).restaEnteros('53', '96')
                # Devuelve 0x4e
        '''
        return self.bt(int(a, self.base)-int(b, self.base))


    def restaModulo(self, a, b, n):
        ''' Método que realiza la resta modular de dos números enteros. El
        resultado se puede devolver en base 2 (binario), 10 (decimal) o 16
        (hexadecimal) dependiendo del valor de la variable self.base.

        Atributos:
            :a: Primer número entero.
            :b: Segundo número entero.
            :n: Número dentro del cuerpo de cifra o módulo.

        Ejemplos:
            :83 - 150 mod 107:

                # Forma estándar:
                sl.RestaLogica(base).restaModulo(a, b, n)

                # En base 2 o binario:
                sl.RestaLogica(2).restaModulo('01010011', '10010110', '1101011')
                # Devuelve 0b1

                # En base 10 o decimal:
                sl.RestaLogica(10).restaModulo('83', '150', '107')
                # Devuelve 1

                # En base 16 o hexadecimal:
                sl.RestaLogica(16).restaModulo('53', '96', '6B')
                # Devuelve 0x1
        '''
        return self.bt((int(a, self.base)-int(b, self.base))%int(n, self.base))
