# Software based on SAMCript 1.0 built in Python 3.8
# Original idea: http://www.criptored.upm.es/software/sw_m001t.htm

import resources.LogicalAddition as la
import resources.LogicalSubstraction as ls
import resources.LogicalMultiplication as lm
import resources.LogicalDivision as ld

a = '932765972365713265327654732'
b = '327165253763657365736954238'
n = '435765377635373652'

ba = '110000001110010000111000001010111011010111010100011100111011101101010100001100011101001100'
bb = '10000111010011111111011111111000111010010011000011111000110010000110100001001100101111110'
bn = '11000001100001001100100110101011011010111101101001001010100'

ha = '30390E0AED751CEED50C74C'
hb = '10E9FEFF1D261F190D0997E'
hn = '60C264D5B5ED254'

print(la.LogicalAddition(2).integerAddition(ba, bb))
print(la.LogicalAddition(10).integerAddition(a, b))
print(la.LogicalAddition(16).integerAddition(ha, hb))
print(la.LogicalAddition(2).modularAddition(ba, bb, bn))
print(la.LogicalAddition(10).modularAddition(a, b, n))
print(la.LogicalAddition(16).modularAddition(ha, hb, hn))

print(ls.LogicalSubstraction(2).integerSubtraction(ba, bb))
print(ls.LogicalSubstraction(10).integerSubtraction(a, b))
print(ls.LogicalSubstraction(16).integerSubtraction(ha, hb))
print(ls.LogicalSubstraction(2).modularSubstraction(ba, bb, bn))
print(ls.LogicalSubstraction(10).modularSubstraction(a, b, n))
print(ls.LogicalSubstraction(16).modularSubstraction(ha, hb, hn))

print(lm.LogicalMultiplication(2).integerMultiplication(ba, bb))
print(lm.LogicalMultiplication(10).integerMultiplication(a, b))
print(lm.LogicalMultiplication(16).integerMultiplication(ha, hb))
print(lm.LogicalMultiplication(2).modularMultiplication(ba, bb, bn))
print(lm.LogicalMultiplication(10).modularMultiplication(a, b, n))
print(lm.LogicalMultiplication(16).modularMultiplication(ha, hb, hn))
