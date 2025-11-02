https://play.picoctf.org/practice/challenge/470
## Description
This service provides you an encrypted flag. Can you decrypt it with just N & e?

Additional details will be available after launching your challenge instance.
Connect to the program with netcat: `$ nc verbal-sleep.picoctf.net 61910` The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_verbal_sleep/2b0f68c54cfcb2dafd4ca90c4abcbe73c208f09edf65af336fc7023e1c1314ca/encrypt.py).
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


We factor n using https://factordb.com/index.php

```
>>> from Crypto.Util.number import inverse
>>> from Crypto.Util.number import long_to_bytes
>>> p = 2
>>> q = 12244909212687444824614413492207105163157191928713273867060445396337793570833017576317038444653918377877370234499972996280528616968262719793443132245617467
>>> m = p * q
>>> m
24489818425374889649228826984414210326314383857426547734120890792675587141666035152634076889307836755754740468999945992561057233936525439586886264491234934
>>> tn = (p -1) * (q-1)
>>> e = 65537
>>> d = pow(e, -1, tn)
>>> c = 14804206601038987713872201403802499940539894655625415088626050969203059516352110458979560533457544333028177386823118725971976749137366458236907302588264257
>>> m = pow(c, d, n)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined. Did you mean: 'tn'?
>>> n = m
>>> m = pow(c, d, n)
>>> long_to_bytes(m)
b'picoCTF{tw0_1$_pr!m31c9046c4}'
```
The flag is ```picoCTF{tw0_1$_pr!m31c9046c4}```
## Additional notes

## References


