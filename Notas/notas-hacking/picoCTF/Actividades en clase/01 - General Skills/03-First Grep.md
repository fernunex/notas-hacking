https://play.picoctf.org/practice/challenge/85
## Descripción
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file)? This would be really tedious to look through manually, something tells me there is a better way.
## Solución
Utilizar un cat  del file con un pipe al grep buscando por la cadena "picoCTF{":
```
cat file | grep picoCTF{
```

Flag:
```
picoCTF{grep_is_good_to_find_things_5af9d829}
```


## Notas adicionales
* Se puede utilizar una alternativa como awk
* Se puede crear un script para leer carácter por carácter hasta que haga match la sentencia.
## Referencias

