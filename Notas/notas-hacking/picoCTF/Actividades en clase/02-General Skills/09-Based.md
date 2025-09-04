https://play.picoctf.org/practice/challenge/35
## Descripción

To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 29221`.
## Solución
1. Nos conectamos como indica la descripción.
2. Realizamos las codificaciones de binario, octal, y hexadecimal a texto utilizando las siguientes páginas:
		https://www.rapidtables.com/convert/number/binary-to-ascii.html
		https://onlinetexttools.com/convert-octal-to-text
		https://www.rapidtables.com/convert/number/hex-to-ascii.html
3. Obtenemos la flag:
```
picoCTF{learning_about_converting_values_00a975ff}
```
## Notas adicionales
* Podemos utilizar otras herramientas de linux como awk o xxd, pero sería mas laborioso y lento para estas 3 palabras que nos da el servicio, esto convendría en un script si fueran cientos de líneas.
## Referencias

