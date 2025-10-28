https://play.picoctf.org/practice/challenge/2
## Description
In RSA d is a lot bigger than e, why don't we use d to encrypt instead of e? Connect with `nc jupiter.challenges.picoctf.org 19566`.
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

Sol:
```
c = 21478327562671038644953935153222011513058869890787995837443553461861380137687353721114352340264042360765458650344814365960978707627630295197262522875685005212909482195707254094374561733161783729341965352239767648463033098736294785736665678129618910074012469055129274874757842577500369307491601457096189773467
n = 120273091626170123058594661354206444082825021013781913612140030676685166534384324674362311355376940397831670047684382589329058445411347093334387780462909803613768000979861738394265442115679258282056882154822229117707767738382015469080424342184064507148844160410209489637069581648273168818860694321238679936223
e = 65537
m = pow(c, e, n)
print(long_to_bytes(m))
b'picoCTF{bad_1d3a5_2438125}'
```
The flag is: 
## Additional notes
* We could use https://github.com/RsaCtfTool/RsaCtfTool
## References

