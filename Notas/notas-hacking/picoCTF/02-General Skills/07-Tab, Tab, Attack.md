https://play.picoctf.org/practice/challenge/176
## Descripción
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/9689f2b453ad5daeb73ca7534e4d1521/Addadshashanammu.zip)
## Solución
1. Descargamos el comprimido y lo descomprimimos.
2. Buscamos todos aquellos archivos con find:
```
find Addadshashanammu -type f
```
1. Al ser un binario, le leemos todos los strings legibles con strings y grepeamos por la flag:
```
find Addadshashanammu -type f | xargs strings | grep pico
```
1. Y obtenemos la flag:
```
picoCTF{l3v3l_up!_t4k3_4_r35t!_2bcfb2ab}
```

## Notas adicionales
## Referencias

