https://play.picoctf.org/practice/challenge/46
## Descripción

The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? `https://jupiter.challenges.picoctf.org/problem/13594/` ([link](https://jupiter.challenges.picoctf.org/problem/13594/)) or http://jupiter.challenges.picoctf.org:13594
## Solución
1. Accedemos al link. Y vemos que solo se verifica el password del usuario Joe. Entonces probamos con el usuario "pedro" y de contraseña "holiwis" y nos permite entrar.
2. Examinamos las cookies y vemos que esta parte es interesante (Admin):
![[Pasted image 20250916170249.png]]
3. Modificamos el valor de la cookie de admin:Value:False a True (utilizando un editor de cookies add-on de firefox), que es para indicar si somos o no admins, entonces nos permite ver la flag:
```
picoCTF{th3_c0nsp1r4cy_l1v3s_d1c24fef}
```


## Notas adicionales

1. Se puede obtener la flag si le mandamos igualmente la cookie usando el comado ```curl```

## Referencias

https://www.youtube.com/watch?v=P2njyHWhu1U&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=3

https://en.wikipedia.org/wiki/HTTP_cookie
https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies


