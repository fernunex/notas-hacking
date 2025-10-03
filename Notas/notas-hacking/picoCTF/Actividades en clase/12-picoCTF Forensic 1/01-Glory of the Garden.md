https://play.picoctf.org/practice/challenge/44
## Descripción
This [garden](https://jupiter.challenges.picoctf.org/static/43c4743b3946f427e883f6b286f47467/garden.jpg) contains more than it seems.
## Solución
1. Save the file in our computer.
2. Find readable strings embedded in the file and filter by the flag:
	```strings garden.jpg | grep picoCTF```
3. The flag is: ```picoCTF{more_than_m33ts_the_3y3657BaB2C}```

## Notas adicionales
* Also, we could use an hexadecimal editor to view its raw data and find it manually.
	![](../../../images/Pasted%20image%2020251002180425.png)
## Referencias

https://en.wikipedia.org/wiki/Hex_editor

