# Software basado en SAMCript 1.0 hecho en Python 3.8
# Fuente original: http://www.criptored.upm.es/software/sw_m001t.htm

# def resta(a, b, n):
#     '''Función que realiza una resta modular.
#     Atributos:
#         :a: Primer número.
#         :b: Segundo número.
#         :n: Número dentro del cuerpo de cifra o módulo.
#     Ejemplo:
#         :a - b mod n: resta(a, b, n)
#     '''
#     return (a-b)%n
#
#
# def producto(a, b, n):
#     '''Función que realiza una multiplicación modular.
#     Atributos:
#         :a: Primer número.
#         :b: Segundo número.
#         :n: Número dentro del cuerpo de cifra o módulo.
#     Ejemplo:
#         :a - b mod n: producto(a, b, n)
#     '''
#     return (a%n*b%n)%n
#
#
# def division():
#     pass
#
#
# def raiz_cuadrada():
#     pass
#
#
# def raiz_primitiva():
#     pass
#
#
# def sumaXOR(a, b):
#     '''Función que realiza una suma modular XOR o mod 2.
#     Atributos:
#         :a: Primer número.
#         :b: Segundo número.
#     Ejemplo:
#         :a XOR b: sumaXOR(a, b)
#     '''
#     return a^b
#
#
# def inverso():
#     pass
#
#
# def potencia(a, b, n):
#     '''Función que realiza una potencia modular.
#     Atributos:
#         :a: Número base.
#         :b: Número exponente.
#         :n: Número dentro del cuerpo de cifra o módulo.
#     Ejemplo:
#         :a^b mod n: potencia(a, b, n)
#     '''
#     import math
#     return (pow(a, b))%n
#
#
# def modulo():
#     pass
#
#
# def maximo_comun_divisor():
#     pass
#
#
# def minimo_comun_multiplo():
#     pass
#
#
# def test_de_primalidad():
#     pass
#
#
# def problema_de_factorizacion_entera():
#     pass
#
#
# def problema_de_logaritmo_discreto():
#     pass

import Suma.SumaLogica as sl

ia = 78615373657236576341
ib = 19736537542254
in = 435765377635373652
ba = '1000100001100000001111010011101000110110100001100000001100001010101'
bb = '100011111001101000101010011110010111001101110'
bn = '11000001100001001100100110101011011010111101101001001010100'

se = sl.SumaLogica(16)
result = se.sumaBinariaModulo(b1, b2, bn)

print(result)
