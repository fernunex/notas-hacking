https://play.picoctf.org/practice/challenge/25
## Descripción
Check the admin scratchpad! `https://jupiter.challenges.picoctf.org/problem/61864/` or http://jupiter.challenges.picoctf.org:61864
## Solución
1. Nos logeamos con nuestro usuario "Fer" ya que con admin no nos permitio porque no somos especiales.
2. Obtenemos nuestro JWT: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiRmVyIn0.Tc1upnxq3dY3L5ZvqDHvXBdwUE01YgfupF4ILGBOslA"
3. Es necesario que encuentremos la palabra que genero el hash de la firma, para esto realizamos un ataque de diccionario (rockyou.txt) al hash con :
```
john token -w=rockyou.txt
```
		La palabra secreta es: ilovepico
4. Le colocamos el nuevo JWT con "admin" y agregandole la clave secreta "ilovepico", generamos el JWT y lo agregamos en la cookie y finalmente recargamos la página utilizando ese JWT y nos arroja la flag: ```picoCTF{jawt_was_just_what_you_thought_1ca14548}```

## Notas adicionales
## Referencias
https://en.wikipedia.org/wiki/JSON

https://www.jwt.io/
https://www.youtube.com/watch?v=iaKbvrbcSko&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=10



