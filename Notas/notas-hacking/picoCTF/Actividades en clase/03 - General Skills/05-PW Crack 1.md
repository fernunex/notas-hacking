https://play.picoctf.org/practice/challenge/245
## Descripción
Can you crack the password to get the flag? Download the password checker [here](https://artifacts.picoctf.net/c/12/level1.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/12/level1.flag.txt.enc) in the same directory too.
## Solución
1. Descargamos el ambos archivos y si ejecutamos el script level1.py nos pide una contraseña, pero ni idea de cual puede ser.
2. Entonces cateamos el archivo para ver su contenido y esta parte resulta interesante:
```
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "8713"):
        print("Welcome back... your flag, user:")
```

3. Según este código podemos observar que esta comparando la cadena que le pasa el usuario con la cadena hardcodeada "8713" por lo cual esta debe ser la contraseña.
4. Ejecutamos el script y le pasamos la contraseña "8713" y obtenemos la flag:
```
picoCTF{545h_r1ng1ng_1b2fd683}
```

## Notas adicionales
## Referencias

