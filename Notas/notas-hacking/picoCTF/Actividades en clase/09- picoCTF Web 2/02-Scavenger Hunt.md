https://play.picoctf.org/practice/challenge/161
## Descripción
There is some interesting information hidden around this site [http://mercury.picoctf.net:44070/](http://mercury.picoctf.net:44070/). Can you find it?
## Solución
1. Vamos a la página que nos indica. Dice que utilizo 3 tecnologías entonces inspeccionamos cada una de ellas con el inspector de firefox y encontramos lo siguiente:
	1. HTML: ```picoCTF{t```
	2. CSS: ```h4ts_4_l0```
	3. JS: nos da la siguiente pista: /* How can I keep Google from indexing my website? */
		1. Buscamos el archivo robots.txt en: http://mercury.picoctf.net:44070/robots.txt
		2. Encontramos la siguiente parte de la flag ```t_0f_pl4c```y la siguiente pista: I think this is an apache server... can you Access the next flag?
		3. Un servidor apache tiene varios archivos por defecto, uno de ellos es: http://mercury.picoctf.net:44070/.htaccess y encontramos otra parte de la flag ```3s_2_lO0k``` y nos da una siguiente pista: I love making websites on my Mac, I can Store a lot of information there.
		4. Accedemos a la ruta: http://mercury.picoctf.net:44070/.DS_Store y nos da la última parte de la flag. ```Part 5: _7a46d25d}```
	4. La flag completa es: ```picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_7a46d25d}```
## Notas adicionales
## Referencias
https://httpd.apache.org/docs/2.4/es/howto/htaccess.html

https://en.wikipedia.org/wiki/.DS_Store

https://www.youtube.com/watch?v=E2gN3AGHirc&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=15