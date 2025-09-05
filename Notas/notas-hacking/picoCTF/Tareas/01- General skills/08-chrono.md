https://play.picoctf.org/practice/challenge/347
## Descripción
How to automate tasks to run at intervals on linux servers?

Additional details will be available after launching your challenge instance.

How to automate tasks to run at intervals on linux servers? Use ssh to connect to this server:

```
Server: saturn.picoctf.net
Port: 60968
Username: picoplayer 
Password: bLgSMmbY6X
```
## Solución
1. Nos conectamos utilizando las credenciales que nos indica:
	```
	ssh picoplayer@saturn.picoctf.net -p 60968
	```
2. Como habla del cron, sabemos que hay archivos de configuración de cron en el directorio /etc. Para asegurarnos de que archivos hay ahí sobre cron realizamos un:
```
picoplayer@challenge:~$ ls -l /etc/ | grep cron
drwxr-xr-x 1 root   root       26 Aug  4  2023 cron.d
drwxr-xr-x 1 root   root       26 Aug  4  2023 cron.daily
drwxr-xr-x 2 root   root       26 Aug  4  2023 cron.hourly
drwxr-xr-x 2 root   root       26 Aug  4  2023 cron.monthly
drwxr-xr-x 2 root   root       26 Aug  4  2023 cron.weekly
-rw-r--r-- 1 root   root       43 Aug  4  2023 crontab
```
3. Podemos observar que hay archivos, entonces leemos todos, tiene que haber algo:
```
picoplayer@challenge:~$ cat /etc/cron*
cat: /etc/cron.d: Is a directory
cat: /etc/cron.daily: Is a directory
cat: /etc/cron.hourly: Is a directory
cat: /etc/cron.monthly: Is a directory
cat: /etc/cron.weekly: Is a directory
# picoCTF{Sch3DUL7NG_T45K3_L1NUX_1b4d8744}
```
4.  Y ahí esta la flag (realicé uno por uno y esta en /etc/crontab):
```
	picoCTF{Sch3DUL7NG_T45K3_L1NUX_1b4d8744}
```
## Notas adicionales
## Referencias

