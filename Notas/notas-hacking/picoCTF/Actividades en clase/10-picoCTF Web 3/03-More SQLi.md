- [ ] https://play.picoctf.org/practice/challenge/358
## Descripción
Can you find the flag on this website.

Additional details will be available after launching your challenge instance.

Can you find the flag on this website. Try to find the flag [here](http://saturn.picoctf.net:54983/).
## Solución
1. Vamos a la página y nos damos cuenta que es de login. Probamos unas contraseñas y usarios por defecto como admin:admin, etc. Esto nos arroja la salida de una comprobación que realizó usando SQLi: SQL query: SELECT id FROM users WHERE password = 'adnimn' AND username = 'admin'
2. Le pasamos una inyección básica: en password: ```' or 1=1;```y en usuario cualquier cosa, igual la sentencia sql se evalua a true y nos deja entrar.
3. Para poder realizar queries necesitamos que los datos que nos arroje esten en conformidad con el display de la información, en este caso, en una tabla de 3 columnas. Realizamos las siguientes queries a la BD para averiguar mas información y obtener la flag.
	1. Ver la version: ```' union select sqlite_version(), 2, 3;``` -> Versión:3.31.1
	2. Ver la estructura de las tablas: ```' union select sql, 2, 3 from sqlite_master;```
	3. Nos encontramos la tabla con la siguiente estructura "CREATE TABLE more_table (id INTEGER NOT NULL PRIMARY KEY, flag TEXT)" entonces le extraemos las flag, ya que tiene una columna llamada flag: ```' union select id,flag,3 from more_table;```
4. Y encontramos la flag:
		```picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_c8b7cc2a}```
## Notas adicionales
1. Aunque al hacer el bypass del login nos arroja la flag, solo es necesario capturar todo el tráfico con Burpsuite para que no nos aplique la redirección y puedamos ver la bandera sin necesidad de hacer las demas consultas SQL
## Referencias
https://www.sqlite.org/docs.html


https://www.youtube.com/watch?v=clMe4yqL6yU&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=63