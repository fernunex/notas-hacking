https://play.picoctf.org/practice/challenge/356
## Descripción
How about trying to match a regular expression The website is running [here](http://saturn.picoctf.net:50235/).
## Solución
1. Vamos a la página y nos indica que insertemos un input que haga match con la expresión regular que encontramos al inspeccionar el código fuente: ```^p.....F!?```
2. Esta expresión regular hace match por con una cadena que
	1. Comience con la letra "p"
	2. Tenga 5 carácteres cualesquiera
	3. La letra "F"
	4. y opcional el signo de "!"

3. Utilizamos "picoCTF" y nos arroja la flag: ```picoCTF{succ3ssfully_matchtheregex_08c310c6}```



## Notas adicionales

## Referencias
https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Regular_expressions

https://www.youtube.com/watch?v=YZemkSTN50U&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=64

