https://play.picoctf.org/practice/challenge/411
## Descripción
I accidentally wrote the flag down. Good thing I deleted it! You download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/77/challenge.zip)

## Solución
1. Descargamos el archivo, lo descomprimimos y nos metemos a la carpeta.
2. Le ralizamos un ```cat message.txt ```pero al parecer no tiene la flag.
3. Realizamos un ```git log ```y observamos que el primer commit dice que se creo la flag y en el segundo se removió. Entonces viajamos hasta el primer commit:
```
git checkout 3d5ec8a
cat message.txt

----> picoCTF{s@n1t1z3_30e86d36}
```
## Notas adicionales
## Referencias

