https://play.picoctf.org/practice/challenge/73
## Description
Let's decrypt this: [ciphertext](https://jupiter.challenges.picoctf.org/static/eb5e6df8e14c52873cf88c582a1a4008/ciphertext)? Something seems a bit small.
## Solution
RSA - llave publica - asimetrico
m   - mensaje original o mensaje en texto plano 
c   - mensaje cifrado (ciphertext)
p,q - son dos numeros primos distintos y muy grandes
n   - es el modulo (lo compartes las llaves publica como privada)
tn  - totient n (funcion de euler)
e   - llave public - 65537 (exponente)  2 ^ 16 + 1
d   - llave privada

Calculos
n  = p * q
tn = (p -1) * (q-1)
d = e ^ -1 (mod tn)	- pow(e, -1, tn)

Cifrar  
c = m ^ e (mod n)	- pow(m, e, n)

Decifrars
m = c ^ d (mod n)	- pow(c, d, n)

c = m ^ 3
m = 3 raiz c

* Install gmpy2 for high precision operations
* Install pycryptodome for cryptographic operations


```
'''
Como tu exponente `e` es 3 (muy pequeño), la vulnerabilidad más probable es un **ataque de raíz cúbica** (conocido como _Stereotyped attack_ o _small e attack_).
Este ataque funciona si el mensaje original $m$ fue lo suficientemente pequeño como para que $m^3 < n$. 
Si eso ocurrió, el módulo no tuvo efecto, y por lo tanto $c = m^3$.
c = m ^ e mod n
c = m ^ 3
Para revertirlo, solo necesitamos calcular la raíz cúbica de $c$.
m = raiz3(c)
'''

import gmpy2
from Crypto.Util.number import long_to_bytes
gmpy2.get_context().precision=2048


e = 3
c = 2205316413931134031074603746928247799030155221252519872650080519263755075355825243327515211479747536697517688468095325517209911688684309894900992899707504087647575997847717180766377832435022794675332132906451858990782325436498952049751141

print("Calculando la raíz cúbica de c...")

m, es_exacta = gmpy2.iroot(c, 3)

print(long_to_bytes(m))

if es_exacta:
    print("\n¡Raíz cúbica perfecta encontrada!")
    print(f"Mensaje (entero): {m}")
    flag = bytes.fromhex(hex(m)[2:]).decode()
    print(f"FLAG: {flag.decode()}")
else:
    print("\nNo se encontró una raíz cúbica perfecta.")
    print("Este ataque (small e) no funcionó.")

```
La flag es: `picoCTF{n33d_a_lArg3r_e_d0cd6eae}`
## Additional notes
## References
https://en.wikipedia.org/wiki/RSA_cryptosystem
