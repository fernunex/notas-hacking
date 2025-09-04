https://play.picoctf.org/practice/challenge/37
## Descripción
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings) without running it?
## Solución
1. Descargamos el archivo.
2. Imprimimos con strings todos los strings imprimibles de un binario:
```
strings strings | grep pico
```
3. Nos arroja la flag:
```
picoCTF{5tRIng5_1T_d66c7bb7}
```

## Notas adicionales
También es posible convertir el binario a un hexdump y grepear por la flag, en este caso la flag no cabe en una linea por lo cual mostramos las 3 líneas subsecuentes:
```
hexdump -C strings | grep pico -A 3

```
## Referencias

