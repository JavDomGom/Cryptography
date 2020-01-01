class SumaLogica():

    def __init__(self, base):
        self.base = base


    def resultado(self, op):
        if self.base == 2:
            return bin(op)
        elif self.base == 10:
            return int(op)
        elif self.base == 16:
            return hex(op)


    def suma(self, a, b):
        '''Función que realiza la suma de dos números.
        Atributos:
            :a: Primer número.
            :b: Segundo número.
        Ejemplo:
            :a + b: suma(a, b)
        '''
        return self.resultado(a+b)



    def sumaModulo(self, a, b, n):
        '''Función que realiza la suma modular de dos números.
        Atributos:
            :a: Primer número.
            :b: Segundo número.
            :n: Número dentro del cuerpo de cifra o módulo.
        Ejemplo:
            :a + b mod n: suma(a, b, n)
        '''
        return self.resultado((a+b)%n)


    def sumaBinaria(self, a, b):
        '''Función que realiza la suma de dos números binarios.
        Atributos:
            :a: Primer número binario. Parémtero de tipo str().
            :b: Segundo número binario.. Parémtero de tipo str().
        Ejemplo:
            :a + b: suma(a, b)
        '''
        return self.resultado(int(a,2)+int(b,2))


    def sumaBinariaModulo(self, a, b, n):
        '''Función que realiza la suma de dos números binarios.
        Atributos:
            :a: Primer número binario. Parémtero de tipo str().
            :b: Segundo número binario.. Parémtero de tipo str().
        Ejemplo:
            :a + b: suma(a, b)
        '''
        return self.resultado((int(a,2)+int(b,2))%int(n,2))
