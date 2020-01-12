# Software based on SAMCript 1.0 built in Python 3.8
# Original idea: http://www.criptored.upm.es/software/sw_m001t.htm

import resources.LogicalAddition as la
import resources.LogicalSubstraction as ls
import resources.LogicalMultiplication as lm
import resources.LogicalDivision as ld
import resources.LogicalSquareRoot as lsr
import resources.LogicalPrimitiveRoot as lpr
import resources.LogicalXOR as lxor
import resources.LogicalModInverse as lmi
import resources.LogicalExponentiation as le
import resources.LogicalModule as lmod
import resources.LogicalGCD as lgcd
import resources.LogicalLCM as llcm
import resources.LogicalPrimality as lp
import resources.LogicalFactorization as lf
import resources.LogicalDiscreteLogarithm as ldl

# Logical addition, substraction, multiplication and division input data:
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

print(ld.LogicalDivision(2).integerDivision(ba, bb))
print(ld.LogicalDivision(10).integerDivision(a, b))
print(ld.LogicalDivision(16).integerDivision(ha, hb))

# Logical square root input data:
a = '2677959256956917386540306'
ba = '1000110111000101000111011001010011011101100001010110000110001000110111010100010010'
ha = '237147653761586237512'

print(lsr.LogicalSquareRoot(2).integerSquareRoot('110110011001'))
print(lsr.LogicalSquareRoot(10).integerSquareRoot('3481'))
print(lsr.LogicalSquareRoot(16).integerSquareRoot('D99'))

# Logical primitive root input data:
a = '131'
ba = '10000011'
ha = '83'

print(lpr.LogicalPrimitiveRoot(2).integerPrimitiveRoot(ba))
print(lpr.LogicalPrimitiveRoot(10).integerPrimitiveRoot(a))
print(lpr.LogicalPrimitiveRoot(16).integerPrimitiveRoot(ha))

# Logical XOR input data:
a = '291576365716537651973656375212'
b = '918653637516537365126359767263'
ba = '0011101011100010001001010001000110011100001111010000101111010001101110100100011000110110111110101100'
bb = '1011100110000101010001111010100001011101101101100111010101101100000000110110000010110101100011011111'
ha = '3AE225119C3D0BD1BA4636FAC'
hb = 'B98547A85DB6756C0360B58DF'

print(lxor.LogicalXOR(2).xor(ba, bb))
print(lxor.LogicalXOR(10).xor(a, b))
print(lxor.LogicalXOR(16).xor(ha, hb))

# Logical mod inverse input data:
a = '29278875574454292837'
n = '1034257732296675869801674804'
ba = '11001011001010011011101100011010101110110001101011001000101100101'
bn = '110101011110000100100110000000001101100111100101100100010100100011100001010111100000110100'
ha = '19653763576359165'
hn = '35784980367964523857834'

print(lmi.LogicalModInverse(2).modInverse(ba, bn))
print(lmi.LogicalModInverse(10).modInverse(a, n))
print(lmi.LogicalModInverse(16).modInverse(ha, hn))

# Logical exponentiation input data:
a = '546434'
b = '12'
n = '324677263917236527471232'
ba = '10000101011010000010'
bb = '1100'
bn = '1000100110000001100101000101100101101101101101101111011010001101001101010000000'
ha = '85682'
hb = 'C'
hn = '44C0CA2CB6DB7B469A80'

print(le.LogicalExponentiation(2).integerExponentiation(ba, bb))
print(le.LogicalExponentiation(10).integerExponentiation(a, b))
print(le.LogicalExponentiation(16).integerExponentiation(ha, hb))
print(le.LogicalExponentiation(2).modularExponentiation(ba, bb, bn))
print(le.LogicalExponentiation(10).modularExponentiation(a, b, n))
print(le.LogicalExponentiation(16).modularExponentiation(ha, hb, hn))

# Logical module input data:
a = '8793268576239856239652376529837574'
n = '731647642385773654826375962375'
ba = '11011000110001010101001110010011100111100110001001000011111010010101110000110000100000010011000111001111000000110'
bn = '1001001111000001010010111110101110000110110101111011001110111101101010011010100010111101111100000111'
ha = '1B18AA7273CC487D2B86102639E06'
hn = '93C14BEB86D7B3BDA9A8BDF07'

print(lmod.LogicalModule(2).module(ba, bn))
print(lmod.LogicalModule(10).module(a, n))
print(lmod.LogicalModule(16).module(ha, hn))

# Logical GCD input data:
a = '12973649172562463257826182'
b = '923675182536754245625680'
c = '9315662357236572365736765'
ba = '101010111011010001101110111001001111010100100100101101110010101100001001001110000110'
bb = '11000011100110001000100000101111110001000101001000000010110011110110011101010000'
bc = '11110110100101010110001000101111011101001000010101110001001000110110100101100111101'
ha = 'ABB46EE4F524B72B09386'
hb = 'C398882FC45202CF6750'
hc = '7B4AB117BA42B891B4B3D'

print(lgcd.LogicalGCD(2).greatestCommonDivisor(ba, bb))
print(lgcd.LogicalGCD(10).greatestCommonDivisor(a, b))
print(lgcd.LogicalGCD(16).greatestCommonDivisor(ha, hb))
print(lgcd.LogicalGCD(2).greatestCommonDivisor(ba, bb, bc))
print(lgcd.LogicalGCD(10).greatestCommonDivisor(a, b, c))
print(lgcd.LogicalGCD(16).greatestCommonDivisor(ha, hb, hc))

# Logical LCM input data:
a = '3796576235726'
b = '263515476235'
c = '65385479823546'
ba = '110111001111110101100100111111000011001110'
bb = '11110101011010101111110001000100001011'
bc = '1110110111011110111110010011000110000010111010'
ha = '373F593F0CE'
hb = '3D5ABF110B'
hc = '3B77BE4C60BA'

print(llcm.LogicalLCM(2).leastCommonMultiple(ba, bb))
print(llcm.LogicalLCM(10).leastCommonMultiple(a, b))
print(llcm.LogicalLCM(16).leastCommonMultiple(ha, hb))
print(llcm.LogicalLCM(2).leastCommonMultiple(ba, bb, bc))
print(llcm.LogicalLCM(10).leastCommonMultiple(a, b, c))
print(llcm.LogicalLCM(16).leastCommonMultiple(ha, hb, hc))

# Logical primality input data:
a = '442499826945303593556473164314770689'
b = '1725367825470892357176235723652'
ba = '10101010011100011101101000001100101001100111001100101110111011111011000000011010101000011100101000010001111110100000001'
bb = '10101110001101111011011010000100100111001101101001010100111011011000010010000100001010000101110000100'
ha = '5538ED0653399777D80D50E508FD01'
hb = '15C6F6D0939B4A9DB090850B84'

print(lp.LogicalPrimality(2).is_prime(ba))
print(lp.LogicalPrimality(2).is_prime(bb))
print(lp.LogicalPrimality(10).is_prime(a))
print(lp.LogicalPrimality(10).is_prime(b))
print(lp.LogicalPrimality(16).is_prime(ha))
print(lp.LogicalPrimality(16).is_prime(hb))

# Logical factorization input data:
a = '23756965471926357236576238546'
ba = '10011001100001101001101000111101101000011110111111101111010000100011011010110010011101111010010'
ha = '4CC34D1ED0F7F7A11B593BD2'

print(lf.LogicalFactorization(2).factorization(ba))
print(lf.LogicalFactorization(10).factorization(a))
print(lf.LogicalFactorization(16).factorization(ha))

# Logical Discrete Logarithmic Problem input data:
a = '2'
y = '9386983767379'
n = '842941143517861'
ba = '10'
by = '10001000100110010011110101010011110101010011'
bn = '10111111101010011010000111011011010000101010100101'
ha = '2'
hy = '88993D53D53'
hn = '2FEA6876D0AA5'

print(ldl.LogicalDiscreteLogarithm(2).discreteLogarithm(ba, by, bn))
print(ldl.LogicalDiscreteLogarithm(10).discreteLogarithm(a, y, n))
print(ldl.LogicalDiscreteLogarithm(16).discreteLogarithm(ha, hy, hn))
