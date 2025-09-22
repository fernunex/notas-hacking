https://play.picoctf.org/practice/challenge/173
## Descripción
Who doesn't love cookies? Try to figure out the best one. [http://mercury.picoctf.net:21485/](http://mercury.picoctf.net:21485/)
## Solución
1. Entramos al link y podemos observar que hay una sección para introducir nombres de cookies.
	1. Introducimos "hola" y se manda una cookie "name:-1", indica que no es una cookie valida.
	2. Introduciomos "snickerdoodle" y se manda una cookie "name:0" pero dice que no es especial.

2. Hacemos request usando varias cookies, es decir, fuerza bruta de name=1, name=2, name=3 hasta que alguna de ellas le guste y nos de la flag (filtramos por pico).
```
for cookieNumber in {1..20}; do curl -s http://mercury.picoctf.net:21485/check -H "Cookie: name=$cookieNumber"; done | grep pico
```
3. Flag: ```picoCTF{3v3ry1_l0v3s_c00k135_94190c8a}```


## Notas adicionales
1. Es posible resolverlo con burpsuite llevando un ataque variando la cookie.
	1. Interceptamos el GET que manda el cookie con redirigiendo la petición a burpsuite usando foxyproxy.
	2. Con el Intruder le realizamos un ataque sniper con un payload numérico desde el 1 hasta el 20 y filtramos por la coincidencia de "picoCTF" en cada una de las respuestas:
		![image](../../../Pasted%20image%2020250921185626.png)
## Referencias

https://www.youtube.com/watch?v=LseQ-XWCXVo&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=13