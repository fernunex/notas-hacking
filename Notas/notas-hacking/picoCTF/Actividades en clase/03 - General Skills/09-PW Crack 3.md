https://play.picoctf.org/practice/challenge/247
## Descripción
Can you crack the password to get the flag? Download the password checker [here](https://artifacts.picoctf.net/c/18/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/18/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/18/level3.hash.bin) in the same directory too. There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.


## Solución

1. Descargamos los archivos y los guardamos en un mismo directorio.
2. Le realizamos un cat a level3.py para checar su código fuente y nos podemos percatar que contiene estos comentarios:
```
# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]
```
3. Podemos deducir que debemos de encontrar la contraseña mediante fuerza bruta, es decir, probar todas las posibilidades hasta que una nos arroje la flag. En mi caso fue la contraseña "2295":
```
picoCTF{m45h_fl1ng1ng_6f98a49f}
```

## Notas adicionales


## Referencias

