https://play.picoctf.org/practice/challenge/363
## Descripción
Can you read files in the root file?

Additional details will be available after launching your challenge instance.
The system admin has provisioned an account for you on the main server: `ssh -p 56907 picoplayer@saturn.picoctf.net` Password: `33qE7mB5BF` Can you login and read the root file?
## Solución
1. Nos conectamos usando las credenciales.
2. Checamos nuestros permisos de root o de sudoer con ```sudo -l ```.
3. Nos percatamos que tenemos permiso de sudo en el binario ```/usr/bin/vi```.
4. Entonces lo corremos somo sudo ```sudo vi texto```.
5. Ya estando dentro nos escapamos obteniendo una shell y ahora estamos como root en el sistema ```:! /bin/bash```.
6. Viajamos hasta el home de root y leemos la flag ```cat .flag.txt``` y esta es la flag: ```picoCTF{uS1ng_v1m_3dit0r_3dd6dcf4}```.

## Notas adicionales

* También es posible obtener la flag sin obtener la shell, pero es mas cómoda que estar desde vi ejecutando comandos.
## Referencias

