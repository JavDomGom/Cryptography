# Software basado en SAMCript 1.0 hecho en Python 3.8
# Fuente original: http://www.criptored.upm.es/software/sw_m001t.htm

def suma(a, b, n):
    '''Función que realiza una suma modular.
    Atributos:
        :a: Primer número.
        :b: Segundo número.
        :n: Número dentro del cuerpo de cifra o módulo.
    Ejemplo:
        :a + b mod n: suma(a, b, n)
    '''
    return (a+b)%n


def sumaXOR(a, b):
    '''Función que realiza una suma modular XOR o mod 2.
    Atributos:
        :a: Primer número.
        :b: Segundo número.
    Ejemplo:
        :a XOR b: sumaXOR(a, b)
    '''
    return a^b


def resta(a, b, n):
    '''Función que realiza una resta modular.
    Atributos:
        :a: Primer número.
        :b: Segundo número.
        :n: Número dentro del cuerpo de cifra o módulo.
    Ejemplo:
        :a - b mod n: resta(a, b, n)
    '''
    return (a-b)%n


def producto(a, b, n):
    '''Función que realiza una multiplicación modular.
    Atributos:
        :a: Primer número.
        :b: Segundo número.
        :n: Número dentro del cuerpo de cifra o módulo.
    Ejemplo:
        :a - b mod n: producto(a, b, n)
    '''
    return (a%n*b%n)%n


def potencia(a, b, n):
    '''Función que realiza una potencia modular.
    Atributos:
        :a: Número base.
        :b: Número exponente.
        :n: Número dentro del cuerpo de cifra o módulo.
    Ejemplo:
        :a^b mod n: potencia(a, b, n)
    '''
    import math
    return (pow(a, b))%n
