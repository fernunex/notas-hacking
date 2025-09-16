https://play.picoctf.org/practice/challenge/9
## Descripción
This website can be rendered only by **picobrowser**, go and catch the flag! `https://jupiter.challenges.picoctf.org/problem/28921/` ([link](https://jupiter.challenges.picoctf.org/problem/28921/)) or http://jupiter.challenges.picoctf.org:28921
## Solución
1. Accedemos a la página y le damos click en Flag. Nos indica que solo desde "picobrowser" nos pertmitirá acceder, no desde firefox.
2. Para modificar el encabezado del User-Agent, es decir, el que indica cual navegador somos, utilizaremos el comando curl con el flag -H activado y le indicamos el browser que si fuciona:
``` 
curl -H "User-Agent: picobrowser" https://jupiter.challenges.picoctf.org/problem/28921/flag | grep pico
```

3. Nos permite pasar y nos arroja la flag:
```
picoCTF{p1c0_s3cr3t_ag3nt_84f9c865}
```
## Notas adicionales
1. Desde el inspector podemos modificar el request que le hacemos al servidor web, solo cambiandole el User-Agent y nos deja acceder.


## Referencias

https://www.youtube.com/watch?v=9d6-N0oJwOk&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=6


