# Matemáticas discretas

1. Reducción a módulo.
2. Cálculos inversos.
3. Aditivos.
4. XOR.
5. Multiplicativos.
6. Potencia (exponenciación).
7. Raíces primitivas de un número primo.

## Operaciones modulares

En criptografía clásica y moderna la mayoría de los algoritmos realizan sus operaciones de cifrado y descifrado usando **números dentro de un cuerpo de cifra o módulo, normalmente denominado `n` y expresado como `mod n` si se trata de un número compuesto o `mod p` si el cuerpo de cifra es un número primo.**

| Cuerpo de cifra compuesto | Cuerpo de cifra primo |
| ------------------------- | --------------------- |
| `mod n`                   | `mod p`               |

```python
import string

for n,c in enumerate(string.ascii_uppercase):
    print(f'{c} \u2194 {n:>2}   \u2192   {n:>2} mod 27 = {n%27:>2}')
```

```bash
A ↔  0   →    0 mod 27 =  0
B ↔  1   →    1 mod 27 =  1
C ↔  2   →    2 mod 27 =  2
D ↔  3   →    3 mod 27 =  3
E ↔  4   →    4 mod 27 =  4
F ↔  5   →    5 mod 27 =  5
G ↔  6   →    6 mod 27 =  6
H ↔  7   →    7 mod 27 =  7
I ↔  8   →    8 mod 27 =  8
J ↔  9   →    9 mod 27 =  9
K ↔ 10   →   10 mod 27 = 10
L ↔ 11   →   11 mod 27 = 11
M ↔ 12   →   12 mod 27 = 12
N ↔ 13   →   13 mod 27 = 13
O ↔ 14   →   14 mod 27 = 14
P ↔ 15   →   15 mod 27 = 15
Q ↔ 16   →   16 mod 27 = 16
R ↔ 17   →   17 mod 27 = 17
S ↔ 18   →   18 mod 27 = 18
T ↔ 19   →   19 mod 27 = 19
U ↔ 20   →   20 mod 27 = 20
V ↔ 21   →   21 mod 27 = 21
W ↔ 22   →   22 mod 27 = 22
X ↔ 23   →   23 mod 27 = 23
Y ↔ 24   →   24 mod 27 = 24
Z ↔ 25   →   25 mod 27 = 25
```

```python
cols = 8
rows = 32
hline_u = '{}{}{}'.format(u'\u2554', u'\u2550'*(12*cols-1), u'\u2557')
hline_c = '{}{}{}{}'.format(
    u'\u2560',
    (u'\u2550'*11+u'\u2566'+u'\u2550'*11+u'\u2566')*3,
    u'\u2550'*11+u'\u2566'+u'\u2550'*11,
    u'\u2563'
)
hline_d = '{}{}{}{}'.format(
    u'\u255a',
    (u'\u2550'*11+u'\u2569'+u'\u2550'*11+u'\u2569')*3,
    u'\u2550'*11+u'\u2569'+u'\u2550'*11,
    u'\u255d'
)
header = 'ASCII + extended code table'

print(hline_u)
print('{}{:^{x}}{}'.format(u'\u2551', header, u'\u2551', x=12*cols-1))
print(hline_c)
for i in range(rows):
    row = u'\u2551'.join(f'{n*rows+i:>4} {chr(n*rows+i)!r:6}' for n in range(cols))
    print('{}{}{}'.format(u'\u2551', row, u'\u2551'))
print(hline_d)
```

```
╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
║                                  ASCII + extended code table                                  ║
╠═══════════╦═══════════╦═══════════╦═══════════╦═══════════╦═══════════╦═══════════╦═══════════╣
║   0 '\x00'║  32 ' '   ║  64 '@'   ║  96 '`'   ║ 128 '\x80'║ 160 '\xa0'║ 192 'À'   ║ 224 'à'   ║
║   1 '\x01'║  33 '!'   ║  65 'A'   ║  97 'a'   ║ 129 '\x81'║ 161 '¡'   ║ 193 'Á'   ║ 225 'á'   ║
║   2 '\x02'║  34 '"'   ║  66 'B'   ║  98 'b'   ║ 130 '\x82'║ 162 '¢'   ║ 194 'Â'   ║ 226 'â'   ║
║   3 '\x03'║  35 '#'   ║  67 'C'   ║  99 'c'   ║ 131 '\x83'║ 163 '£'   ║ 195 'Ã'   ║ 227 'ã'   ║
║   4 '\x04'║  36 '$'   ║  68 'D'   ║ 100 'd'   ║ 132 '\x84'║ 164 '¤'   ║ 196 'Ä'   ║ 228 'ä'   ║
║   5 '\x05'║  37 '%'   ║  69 'E'   ║ 101 'e'   ║ 133 '\x85'║ 165 '¥'   ║ 197 'Å'   ║ 229 'å'   ║
║   6 '\x06'║  38 '&'   ║  70 'F'   ║ 102 'f'   ║ 134 '\x86'║ 166 '¦'   ║ 198 'Æ'   ║ 230 'æ'   ║
║   7 '\x07'║  39 "'"   ║  71 'G'   ║ 103 'g'   ║ 135 '\x87'║ 167 '§'   ║ 199 'Ç'   ║ 231 'ç'   ║
║   8 '\x08'║  40 '('   ║  72 'H'   ║ 104 'h'   ║ 136 '\x88'║ 168 '¨'   ║ 200 'È'   ║ 232 'è'   ║
║   9 '\t'  ║  41 ')'   ║  73 'I'   ║ 105 'i'   ║ 137 '\x89'║ 169 '©'   ║ 201 'É'   ║ 233 'é'   ║
║  10 '\n'  ║  42 '*'   ║  74 'J'   ║ 106 'j'   ║ 138 '\x8a'║ 170 'ª'   ║ 202 'Ê'   ║ 234 'ê'   ║
║  11 '\x0b'║  43 '+'   ║  75 'K'   ║ 107 'k'   ║ 139 '\x8b'║ 171 '«'   ║ 203 'Ë'   ║ 235 'ë'   ║
║  12 '\x0c'║  44 ','   ║  76 'L'   ║ 108 'l'   ║ 140 '\x8c'║ 172 '¬'   ║ 204 'Ì'   ║ 236 'ì'   ║
║  13 '\r'  ║  45 '-'   ║  77 'M'   ║ 109 'm'   ║ 141 '\x8d'║ 173 '\xad'║ 205 'Í'   ║ 237 'í'   ║
║  14 '\x0e'║  46 '.'   ║  78 'N'   ║ 110 'n'   ║ 142 '\x8e'║ 174 '®'   ║ 206 'Î'   ║ 238 'î'   ║
║  15 '\x0f'║  47 '/'   ║  79 'O'   ║ 111 'o'   ║ 143 '\x8f'║ 175 '¯'   ║ 207 'Ï'   ║ 239 'ï'   ║
║  16 '\x10'║  48 '0'   ║  80 'P'   ║ 112 'p'   ║ 144 '\x90'║ 176 '°'   ║ 208 'Ð'   ║ 240 'ð'   ║
║  17 '\x11'║  49 '1'   ║  81 'Q'   ║ 113 'q'   ║ 145 '\x91'║ 177 '±'   ║ 209 'Ñ'   ║ 241 'ñ'   ║
║  18 '\x12'║  50 '2'   ║  82 'R'   ║ 114 'r'   ║ 146 '\x92'║ 178 '²'   ║ 210 'Ò'   ║ 242 'ò'   ║
║  19 '\x13'║  51 '3'   ║  83 'S'   ║ 115 's'   ║ 147 '\x93'║ 179 '³'   ║ 211 'Ó'   ║ 243 'ó'   ║
║  20 '\x14'║  52 '4'   ║  84 'T'   ║ 116 't'   ║ 148 '\x94'║ 180 '´'   ║ 212 'Ô'   ║ 244 'ô'   ║
║  21 '\x15'║  53 '5'   ║  85 'U'   ║ 117 'u'   ║ 149 '\x95'║ 181 'µ'   ║ 213 'Õ'   ║ 245 'õ'   ║
║  22 '\x16'║  54 '6'   ║  86 'V'   ║ 118 'v'   ║ 150 '\x96'║ 182 '¶'   ║ 214 'Ö'   ║ 246 'ö'   ║
║  23 '\x17'║  55 '7'   ║  87 'W'   ║ 119 'w'   ║ 151 '\x97'║ 183 '·'   ║ 215 '×'   ║ 247 '÷'   ║
║  24 '\x18'║  56 '8'   ║  88 'X'   ║ 120 'x'   ║ 152 '\x98'║ 184 '¸'   ║ 216 'Ø'   ║ 248 'ø'   ║
║  25 '\x19'║  57 '9'   ║  89 'Y'   ║ 121 'y'   ║ 153 '\x99'║ 185 '¹'   ║ 217 'Ù'   ║ 249 'ù'   ║
║  26 '\x1a'║  58 ':'   ║  90 'Z'   ║ 122 'z'   ║ 154 '\x9a'║ 186 'º'   ║ 218 'Ú'   ║ 250 'ú'   ║
║  27 '\x1b'║  59 ';'   ║  91 '['   ║ 123 '{'   ║ 155 '\x9b'║ 187 '»'   ║ 219 'Û'   ║ 251 'û'   ║
║  28 '\x1c'║  60 '<'   ║  92 '\\'  ║ 124 '|'   ║ 156 '\x9c'║ 188 '¼'   ║ 220 'Ü'   ║ 252 'ü'   ║
║  29 '\x1d'║  61 '='   ║  93 ']'   ║ 125 '}'   ║ 157 '\x9d'║ 189 '½'   ║ 221 'Ý'   ║ 253 'ý'   ║
║  30 '\x1e'║  62 '>'   ║  94 '^'   ║ 126 '~'   ║ 158 '\x9e'║ 190 '¾'   ║ 222 'Þ'   ║ 254 'þ'   ║
║  31 '\x1f'║  63 '?'   ║  95 '_'   ║ 127 '\x7f'║ 159 '\x9f'║ 191 '¿'   ║ 223 'ß'   ║ 255 'ÿ'   ║
╚═══════════╩═══════════╩═══════════╩═══════════╩═══════════╩═══════════╩═══════════╩═══════════╝
```

### Reducción a módulo

**a mod b** = "resto de dividir **a** entre **b**"

```python
n = 27
print(f' 12 mod {n} = {12%n}')
print(f' 31 mod {n} = {31%n}')
print(f' 54 mod {n} = {54%n}')
print(f'-10 mod {n} = {-10%n}')
```

```
 12 mod 27 = 12
 31 mod 27 = 4
 54 mod 27 = 0
-10 mod 27 = 17
```

### Suma

```python
n = 27
print(f'35 + 61 mod {n} \u2192 96 mod {n} = {(35+61)%n}')
print('o bien')
print(f'35 + 61 mod {n} → (35 mod {n} + 61 mod {n}) mod {n} →')
print(f'8 + 7 mod {n} → 15 mod {n} = {(35%n+61%n)%n}')
```

```
35 + 61 mod 27 → 96 mod 27 = 15
o bien
35 + 61 mod 27 → (35 mod 27 + 61 mod 27) mod 27 →
8 + 7 mod 27 → 15 mod 27 = 15
```

### Suma XOR (o mod 2)

Tabla de la verdad XOR:

```
p q | p ⊕ q
-----------
0 0 |   0
0 1 |   1
1 0 |   1
1 1 |   0
```

```python
p = 14
q = 9
print(f'{p} = {bin(p)}')
print(f'{q} = {bin(q)}')
print(f'{bin(p)} XOR {bin(q)} = {p^q}')
```

```
14 = 0b1110
 9 = 0b1001
0b1110 XOR 0b1001 = 7
```

### Resta

```python
n = 27
print(f'43 - 52 mod {n} → -9 mod {n} = {(43-52)%n}')
print('o bien')
print(f'43 - 52 mod {n} → (43 mod {n} - 52 mod {n}) mod {n} →')
print(f'16 - 25 mod {n} → -9 mod {n} = {(43%n-52%n)%n}')
```

```
43 - 52 mod 27 → -9 mod 27 = 18
o bien
43 - 52 mod 27 → (43 mod 27 - 52 mod 27) mod 27 →
16 - 25 mod 27 → -9 mod 27 = 18
```

### Producto

```python
n = 27
print(f'100 * 30 mod {n} → 3000 mod {n} = {(100*30)%n}')
print('o bien')
print(f'100 * 30 mod {n} → (100 mod {n} * 30 mod {n}) mod {n} →')
print(f'19 * 3 mod {n} → 57 mod {n} = {(100%n*30%n)%n}')
```

```
100 * 30 mod 27 → 3000 mod 27 = 3
o bien
100 * 30 mod 27 → (100 mod 27 * 30 mod 27) mod 27 →
19 * 3 mod 27 → 57 mod 27 = 3
```

### Potencia

```python
import math

n = 27
print(f'30⁵ mod {n} → 24.300.000 mod {n} = {(pow(30, 5))%n}')
print('o bien')
print(f'30⁵ mod {n} → [(30² mod {n}) * (30² mod {n}) * 30 mod {n}] mod {n}')
print(f'[(900 mod {n}) * (900 mod {n}) * 30 mod {n}] mod {n} → 9 * 9 * 3 mod {n}')
print(f'243 mod {n} = {((900%n)*(900%n)*30%n)%n}')
```

```
30⁵ mod 27 → 24.300.000 mod 27 = 0
o bien
30⁵ mod 27 → [(30² mod 27) * (30² mod 27) * 30 mod 27] mod 27
[(900 mod 27) * (900 mod 27) * 30 mod 27] mod 27 → 9 * 9 * 3 mod 27
243 mod 27 = 0
```

En aritmética modular en general no está permitida la división, en su lugar se usa **el clálculo de inversos**. Esto es debido a que dentro del módulo o cuerpo los resultados deben ser siempre números enteros.

## Números primos y números compuestos

Las operaciones modulares en criptografía se realizarán dentro de un cuerpo o módulo de cifra cuyo número puede ser primo `p` o compuesto `n`.

Existe una gran cantidad de tipos de primos, como por ejemplo, primos gemelos, primos seguros, primos fuertes, primos de Fermat, primos de Mersenne, primos de Sophie Germain, primos sexy, etc.

Los primos seguros tendrán utilidad en ciertos algoritmos de cifra como por ejemplo RSA. Un número primo es seguro si:

```
p = 2 * p' + 1 (con p' también primo)
```

Por ejemplo:

```
Si p' = 11, luego p = 2 * 11 + 1 = 23 (es primo y seguro)
```

Dicho de otra manera, cualquier número primo multiplicado por `2` y sumándole `1` da como resultado un primo seguro.

Por el teorema de los números primos, se tiene que la probabilidad de encontrar números primos a medida que estos se hacen más grandes es menor. En el intevalo `[2, x]` habrá `(x/ln(x))` números primos. A continuación un sencillo [programa Python](https://github.com/JavDomGom/Cryptography/blob/master/DiscreteMathematics/tools/primes_between_2_numbers.py) en el que se obtiene el porcentaje de números primos en el intervalo `[5, 12]` para `n`:

```python
import math


def per_diff(a, b):
    return round((b*100)/a, 2)


for i in range(5, 12+1):
    x = pow(2, i)
    lnx = round(math.log(x), 2)
    y = round(x/lnx, 2)
    print(
        f'[2, 2^{i:<2}] = {x:<4}\tx/ln x = {x}/{lnx} = {y} \t{per_diff(x, y)}%'
    )
```

```
[2, 2^5 ] = 32    x/ln x = 32/3.47 = 9.22       28.81%
[2, 2^6 ] = 64    x/ln x = 64/4.16 = 15.38      24.03%
[2, 2^7 ] = 128   x/ln x = 128/4.85 = 26.39     20.62%
[2, 2^8 ] = 256   x/ln x = 256/5.55 = 46.13     18.02%
[2, 2^9 ] = 512   x/ln x = 512/6.24 = 82.05     16.03%
[2, 2^10] = 1024  x/ln x = 1024/6.93 = 147.76   14.43%
[2, 2^11] = 2048  x/ln x = 2048/7.62 = 268.77   13.12%
[2, 2^12] = 4096  x/ln x = 4096/8.32 = 492.31   12.02%
```

## Conjunto Completo de Restos (CCR)

El CCR de un número entero `n` es el número de estados que tiene `n` desde `0` hasta `n-1`.

```
CCR(n) = {0, 1, ... n-2, n-1}
```

Es decir:

![equation](https://latex.codecogs.com/png.latex?\forall&space;&space;a&space;\in&space;\mathbb{Z}&space;\quad&space;\exists!r_{i}&space;\in&space;\text{CCR}/a&space;\equiv&space;r_{i}&space;\bmod&space;n)

Por ejemplo:

```
CCR(11) = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
CCR(6)  = {0, 1, 2, 3, 4, 5} = {12, -5, 20, 9, 16, 35}
```

En el segundo conjunto de restos `{12, -5, 20, 9, 16, 35}` en `n = 6` es equivalente al primer conjunto de restos `{0, 1, 2, 3, 4, 5}` porque:

- `12` es equivalente a `0` porque `12 mod 6 = 0`.
- `-5` es equivalente a `1` porque `-5 mod 6 = 1`.
- `20` es equivalente a `2` porque `20 mod 6 = 2`, etc.

A continuación un sencillo [programa Python](https://github.com/JavDomGom/Cryptography/blob/master/DiscreteMathematics/tools/complete_residue_system_modulo_n.py) en el que se obtienen diferentes restos equivalentes en el intervalo `[2, 11]` para `n`.

```python
from random import randint

Z = range(2, 11+1)

for n in Z:
    CRS1 = {i for i in range(n)}
    CRS2 = []
    for r in CRS1:
        while True:
            k = randint(-99, 99)
            if (k % n) == r:
                CRS2.append(k)
                break

    print(f'CRS1({n}) = {CRS1} = CCR2 = {CRS2}')
```

```
CRS1(2) = {0, 1} = CCR2 = [58, -81]
CRS1(3) = {0, 1, 2} = CCR2 = [-54, -20, 71]
CRS1(4) = {0, 1, 2, 3} = CCR2 = [44, 89, -2, -69]
CRS1(5) = {0, 1, 2, 3, 4} = CCR2 = [-70, -19, 62, 98, 79]
CRS1(6) = {0, 1, 2, 3, 4, 5} = CCR2 = [-84, 7, -82, -33, -44, 95]
CRS1(7) = {0, 1, 2, 3, 4, 5, 6} = CCR2 = [70, 78, 37, -74, 32, 61, -29]
CRS1(8) = {0, 1, 2, 3, 4, 5, 6, 7} = CCR2 = [-88, -55, -6, -53, 60, 37, 86, -57]
CRS1(9) = {0, 1, 2, 3, 4, 5, 6, 7, 8} = CCR2 = [-81, -8, -7, -96, 31, -85, -84, -92, -1]
CRS1(10) = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} = CCR2 = [80, -69, 12, 3, -16, -35, -54, -73, -12, 59]
CRS1(11) = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10} = CCR2 = [0, -65, -42, 58, 92, -72, -38, -59, -14, 86, -56]
```

## Conjunto Reducido de Restos (CRR)

## Función de Euler

## Propiedades de las operaciones en Zn

## Homomorfismo de los enteros

## Inversos en un cuerpo

## Algoritmo extendido de Euclides (AEE)

## Producto y potencia dentro de un módulo

## Algoritmo de exponenciación rápida (AER)

## Anillos en un cuerpo

## Raíces primitivas o generadores

## Exponenciación modular

## Cálculos en campos de Galois

## Curvas elípticas en criptografía
