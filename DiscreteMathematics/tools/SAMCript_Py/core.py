# Software basado en SAMCript 1.0 hecho en Python 3.8
# Fuente original: http://www.criptored.upm.es/software/sw_m001t.htm

import resources.DivisionLogica as sl
import resources.RestaLogica as rl
import resources.MultiplicacionLogica as ml
import resources.DivisionLogica as dl

a = '932765972365713265327654732'
b = '327165253763657365736954238'

ba = '110000001110010000111000001010111011010111010100011100111011101101010100001100011101001100'
bb = '10000111010011111111011111111000111010010011000011111000110010000110100001001100101111110'

ha = '30390E0AED751CEED50C74C'
hb = '10E9FEFF1D261F190D0997E'

print(dl.DivisionLogica(10).divisionEnteros(a, b))
