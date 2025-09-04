https://play.picoctf.org/practice/challenge/48
## Descripción
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `jupiter.challenges.picoctf.org 14291`.
## Solución
1. Guardamos el output (escuchamos por un ratito) de la conexión en un archivo:
```
nc jupiter.challenges.picoctf.org 14291 > fileWithFlag.txt
```
2.  Hacemos un grep por la flag:
```
	cat fileWithFlag.txt | grep pico
```

Flag
```
picoCTF{digital_plumb3r_ea8bfec7}
```


## Notas adicionales
## Referencias

