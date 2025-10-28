https://play.picoctf.org/practice/challenge/162
## Description
In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/51d68e61bb41207a55f24e753f07c5a3/values)
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

Solution:
* Factorize n using a web like this: https://factordb.com/
```
c = 62324783949134119159408816513334912534343517300880137691662780895409992760262021
p = 1899107986527483535344517113948531328331
q = 674357869540600933870145899564746495319033
tn = (p-1)*(q-1)
e = 65537
d = inverse(e, tn)
from Crypto.Util.number import inverse
d = inverse(e, tn)
m = pow(c, d, p*q)
long_to_bytes(m)
b'picoCTF{sma11_N_n0_g0od_05012767}'
```

And we get the flag: `picoCTF{sma11_N_n0_g0od_05012767}`
## Additional notes
* We could use https://github.com/RsaCtfTool/RsaCtfTool
## References
https://factordb.com/
