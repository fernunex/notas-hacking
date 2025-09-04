https://play.picoctf.org/practice/challenge/163
## Descripción
Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/static)? This [BASH script](https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/ltdis.sh) might help!
## Solución
1. Descargamos ambos archivos.
2. Le pasamos el static al script de bash:
```
bash ltdis.sh static
```
3. Después grepeamos por la flag en el archivo que nos indica el script que contiene las strings:
```
cat static.ltdis.strings.txt | grep pico
```

La flag es: 
```
picoCTF{d15a5m_t34s3r_1e6a7731}
```

## Notas adicionales

También es posible convertir el binario a un hexdump y grepear por la flag, en este caso la flag no cabe en una linea por lo cual mostramos las 3 líneas subsecuentes:
```
hexdump -C static | grep pico -A 3
```
## Referencias

