https://play.picoctf.org/practice/challenge/240
## Descripción
Fix the syntax error in this Python script to print the flag. [Download Python script](https://artifacts.picoctf.net/c/27/fixme1.py)
## Solución
1. Descargamos el archivo y lo abrimos con un editor de texto, yo utilice sublime, y me percate de esto al final del código:
```
flag = str_xor(flag_enc, 'enkidu')
  print('That is correct! Here\'s your flag: ' + flag)
```
1. Entonces lo idente bien, es decir, la ultima linea del print tiene con tab o un espacio de mas, entonces se la quite y lo corri:
```
flag = str_xor(flag_enc, 'enkidu')
print('That is correct! Here\'s your flag: ' + flag)
```
1. Y me arrojo la flag:
```
picoCTF{1nd3nt1ty_cr1515_182342f7}
```


## Notas adicionales
También es posible ejecutar el script y leer el traceback del error y entonces si identificarlo mas fácil, pero como yo me se la sintaxis de python entonces me fui directo a buscar el error.
## Referencias

