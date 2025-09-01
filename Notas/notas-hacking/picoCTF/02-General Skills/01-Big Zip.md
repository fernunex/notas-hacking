https://play.picoctf.org/practice/challenge/322
## Descripción
Unzip this archive and find the flag.

- [Download zip file](https://artifacts.picoctf.net/c/503/big-zip-files.zip)
## Solución
1. Descargamos el archivo.
2. Extraer el zip
```
7z x big-zip-files.zip
```
3. Listamos todos los .txt, despues con xargs le pasamos cada argumento al cat para leerle su contenido y finalmente le grepeamos por la flag:
```
find . -type f -name "*.txt" | xargs cat | grep pico
```
3. La flag nos aparece al final del grep.
```
picoCTF{gr3p_15_m4g1c_ef8790dc}
```
## Notas adicionales
* Tal vez con un awk también se puede filtrar.
## Referencias

