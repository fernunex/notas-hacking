https://play.picoctf.org/practice/challenge/189
## Descripción
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `481e7b14`

Additional details will be available after launching your challenge instance.

|     |                                             |
| --- | ------------------------------------------- |
| SSH | `ssh ctf-player@venus.picoctf.net -p 55114` |
|     |                                             |
## Solución
1. Nos conectamos mediante ssh utilizando las credenciales que nos indican.
2. Leemos todo con:
```
cat *
```
3. Encontramos parte de la flag "picoCTF{xxsh_" y seguimos las instrucciones.
4. Leemos  todos los txt con:
```
cat *.txt
```
5. Encontramos "0ut_0f_\/\/4t3r_" y seguimos las instrucciones.
6. Leemos el último archivo con:
```
cat *.txt
```
7. Encontramos "1118a9a4}" y formamos la flag de cada parte:
```
picoCTF{xxsh_0ut_0f_\/\/4t3r_1118a9a4}
```

## Notas adicionales
## Referencias

