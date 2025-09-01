https://play.picoctf.org/practice/challenge/384
## Descripción
There's an interesting script in the user's home directory

Additional details will be available after launching your challenge instance.

There's an interesting script in the user's home directory The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.

```
Hostname: saturn.picoctf.net
Port:     61488
Username: picoplayer
Password: password
```
## Solución
1. Conectarnos usando ssh y nos firmamos con las credenciales:
```
ssh picoplayer@saturn.picoctf.net -p 61488
```
2. Exploramos el archivo y realiza operaciones básicas. Nos percatamos que idica leer el manual, entonces realizamos:
```
man useless
```
3. La flag se encuentra en el man, al final:
```
picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_3823}
```
## Notas adicionales
## Referencias

