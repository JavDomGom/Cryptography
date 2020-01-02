class SumaLogica():
    from resources.common import transformaBase as tb

    def __init__(self, base):
        ''' Constructor de la clase.

        Atributos:
            :base: La base numérica que se empleará en los cálculos de la clase.
        '''
        self.base = base


    def sumaEnteros(self, a, b):
        ''' Método que realiza la suma de dos números enteros. El resultado se
        puede devolver en base 2 (binario), 10 (decimal) o 16 (hexadecimal),
        dependiendo del valor de la variable self.base.

        Atributos:
            :a: Primer número entero.
            :b: Segundo número entero.
        Ejemplos:
            :83 + 150:

                # Forma estándar:
                sl.SumaLogica(base).sumaEnteros(a, b)

                # En base 2 o binario:
                sl.SumaLogica(2).sumaEnteros('01010011', '10010110')
                # Devuelve 0b11101001

                # En base 10 o decimal:
                sl.SumaLogica(10).sumaEnteros('83', '150')
                # Devuelve 233

                # En base 16 o hexadecimal:
                sl.SumaLogica(16).sumaEnteros('53', '96')
                # Devuelve 0xe9
        '''
        return self.tb(int(a, self.base)+int(b, self.base))


    def sumaModulo(self, a, b, n):
        ''' Método que realiza la suma modular de dos números enteros. El
        resultado se puede devolver en base 2 (binario), 10 (decimal) o 16
        (hexadecimal) dependiendo del valor de la variable self.base.
        
        Atributos:
            :a: Primer número entero.
            :b: Segundo número entero.
            :n: Número dentro del cuerpo de cifra o módulo.

        Ejemplos:
            :83 + 150 mod 107:

                # Forma estándar:
                sl.SumaLogica(base).sumaModulo(a, b, n)

                # En base 2 o binario:
                sl.SumaLogica(2).sumaModulo('01010011', '10010110', '1101011')
                # Devuelve 0b10010

                # En base 10 o decimal:
                sl.SumaLogica(10).sumaModulo('83', '150', '107')
                # Devuelve 19

                # En base 16 o hexadecimal:
                sl.SumaLogica(16).sumaModulo('53', '96', '6B')
                # Devuelve 0x13
        '''
        return self.tb((int(a, self.base)+int(b, self.base))%int(n, self.base))
