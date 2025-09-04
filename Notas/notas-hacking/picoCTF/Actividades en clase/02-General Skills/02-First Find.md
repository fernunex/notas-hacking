https://play.picoctf.org/practice/challenge/320
## Descripción
Unzip this archive and find the file named 'uber-secret.txt'

- [Download zip file](https://artifacts.picoctf.net/c/501/files.zip)
## Solución
1. Descargamos el archivo y lo extraemos:
```
7z x files.zip
```
2. Buscamos utilizando find y le pasamos con xargs al cat para listar lo que contiene:
```
find files -type f -name "uber-secret.txt" | xargs cat
```
Flag:
```
picoCTF{f1nd_15_f457_ab443fd1}
```
## Notas adicionales
* Una opcion seria listar todo recursivamente y utilizar un grep para encontrarlo.
## Referencias

