# Software basado en SAMCript 1.0 hecho en Python 3.8
# Fuente original: http://www.criptored.upm.es/software/sw_m001t.htm

import resources.SumaLogica as sl
import resources.RestaLogica as rl
import resources.MultiplicacionLogica as ml

a = '78615373657236576341'
b = '19736537542254'
n = '435765377635373652'

ba = '1000100001100000001111010011101000110110100001100000001100001010101'
bb = '100011111001101000101010011110010111001101110'
bn = '11000001100001001100100110101011011010111101101001001010100'

ha = '44301E9D1B4301855'
hb = '11F3454F2E6E'
hn = '60C264D5B5ED254'

print(sl.SumaLogica(2).sumaEnteros(ba, bb))
print(sl.SumaLogica(10).sumaEnteros(a, b))
print(sl.SumaLogica(16).sumaEnteros(ha, hb))
print()
print(sl.SumaLogica(2).sumaModulo(ba, bb, bn))
print(sl.SumaLogica(10).sumaModulo(a, b, n))
print(sl.SumaLogica(16).sumaModulo(ha, hb, hn))
