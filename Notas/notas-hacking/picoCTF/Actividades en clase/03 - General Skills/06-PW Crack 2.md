https://play.picoctf.org/practice/challenge/246
## Descripción

Can you crack the password to get the flag? Download the password checker [here](https://artifacts.picoctf.net/c/13/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/13/level2.flag.txt.enc) in the same directory too.
## Solución
1. Descargamos el ambos archivos y si ejecutamos el script level2.py nos pide una contraseña, pero ni idea de cual puede ser.
2. Entonces cateamos el archivo para ver su contenido y esta parte resulta interesante:
```
def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36) ):
        print("Welcome back... your flag, user:")

```

3. Según este código podemos observar que esta comparando la cadena que le pasa el usuario con la cadena hardcodeada "0x64+0x65+0x37+0x36" por lo cual esta debe ser la contraseña.
4. Ejecutamos el script y le pasamos la contraseña "de76" que es a lo que equivale en ascii cada valor hexadecimal y obtenemos la flag:
```
picoCTF{tr45h_51ng1ng_489dea9a}
```




## Notas adicionales
1. Podemos transformar esos  hexadecimals a ascii utilizando una página web, el comando xdd, o la tabla de ASCII.
## Referencias

