# Matemáticas discretas

1. Reducción a módulo.
2. Cálculos inversos.
  1. Aditivos.
  2. XOR.
  3. Multiplicativos.
3. Potencia (exponenciación).
4. Raíces primitivas de un número primo.

## Operaciones modulares.
En criptografía clásica y moderna la mayoría de los algoritmos realizan sus operaciones de cifrado y descifrado usando **números dentro de un cuerpo de cifra o módulo, normalmente denominado `n` y expresado como `mod n` si se trata de un número compuesto o `mod p` si el cuerpo de cifra es un número primo.**

|Cuerpo de cifra compuesto|Cuerpo de cifra primo|
|-|-|
|`mod n`|`mod p`|

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
hline = f'{"+".ljust(12, "-")*cols}+'
header = 'ASCII + extended code table'

print(hline)
print(f'|{header:^{cols*12-1}}|')
print(hline)
for i in range(rows):
    row = '|'.join(f'{n*rows+i:>4} {chr(n*rows+i)!r:6}' for n in range(cols))
    print(f'|{row}|')
print(hline)
```

## Conjunto completo y reducido de restos.
## Función de Euler.
## Propiedades de las operaciones en Zn.
## Homomorfismo de los enteros.
## Inversos en un cuerpo.
## Algoritmo extendido de Euclides (AEE).
## Producto y potencia dentro de un módulo.
## Algoritmo de exponenciación rápida (AER).
## Anillos en un cuerpo.
## Raíces primitivas o generadores.
## Exponenciación modular.
## Cálculos en campos de Galois.
## Curvas elípticas en criptografía.
