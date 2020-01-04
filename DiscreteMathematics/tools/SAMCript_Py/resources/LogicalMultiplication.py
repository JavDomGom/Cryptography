class MultiplicacionLogica():
    from resources.common import baseTransform as bt

    def __init__(self, base):
        ''' Class constructor.

         Attributes:
             :base: The numerical base to be used in class calculations.
        '''
        self.base = base


    def multiplicacionEnteros(self, a, b):
        ''' Método que realiza la multiplicación de dos números enteros. El
        resultado se puede devolver en base 2 (binario), 10 (decimal) o 16
        (hexadecimal), dependiendo del valor de la variable self.base.

        Atributos:
            :a: Primer número entero.
            :b: Segundo número entero.

        Ejemplos:
            :89 * 67:

                # Forma estándar:
                ml.MultiplicacionLogica(base).multiplicacionEnteros(a, b)

                # En base 2 o binario:
                ml.MultiplicacionLogica(2).multiplicacionEnteros('01011001', '01000011')
                # Devuelve 0b1011101001011

                # En base 10 o decimal:
                ml.MultiplicacionLogica(10).multiplicacionEnteros('89', '67')
                # Devuelve 5963

                # En base 16 o hexadecimal:
                ml.MultiplicacionLogica(16).multiplicacionEnteros('59', '43')
                # Devuelve 0x174b
        '''
        return self.bt(int(a, self.base)*int(b, self.base))


    def multiplicacionModulo(self, a, b, n):
        ''' Método que realiza la multiplicación modular de dos números
        enteros. El resultado se puede devolver en base 2 (binario), 10
        (decimal) o 16 (hexadecimal) dependiendo del valor de la variable self.base.

        Atributos:
            :a: Primer número entero.
            :b: Segundo número entero.
            :n: Número dentro del cuerpo de cifra o módulo.

        Ejemplos:
            :89 * 67 mod 121:

                # Forma estándar:
                ml.MultiplicacionLogica(base).multiplicacionModulo(a, b, n)

                # En base 2 o binario:
                ml.MultiplicacionLogica(2).multiplicacionModulo('01011001', '01000011', '01111001')
                # Devuelve 0b100010

                # En base 10 o decimal:
                ml.MultiplicacionLogica(10).multiplicacionModulo('89', '67', '121')
                # Devuelve 34

                # En base 16 o hexadecimal:
                ml.MultiplicacionLogica(16).multiplicacionModulo('59', '43', '79')
                # Devuelve 0x22
        '''
        return self.bt((int(a, self.base)*int(b, self.base))%int(n, self.base))
