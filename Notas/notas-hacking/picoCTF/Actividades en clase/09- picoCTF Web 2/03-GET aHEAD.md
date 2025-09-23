https://play.picoctf.org/practice/challenge/132
## Descripción
Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:34561/](http://mercury.picoctf.net:34561/)
## Solución
1. Entramos a la página y podemos observar que hay dos botones para cambiar de color. Lo realiza mediante métodos POST y GET.
2. Entonces le mandamos una petición de tipo HEAD para ver que sucede. Esto nos devuelve la bandera.
	1. Utilizando el Inpector de páginas.
		![](../../../images/Pasted%20image%2020250922192627.png)
		Flag: ```picoCTF{r3j3ct_th3_du4l1ty_8f878508}```

	2. Utilizando el comado desde consola y su respuesta contiene la bandera:
		```
		curl -I HEAD http://mercury.picoctf.net:34561/index.php
		```
## Notas adicionales
1. También es posible realizarlo con un Proxy y Burpsuite.
	1. Redirigir la petición utilizando FoxyProxy a Burpsuite y ahi la interceptamos, modificamos y mandamos. Sucede lo mismo que en el inspector de Firefox, en la respuesta nos da la bandera.
## Referencias

https://www.youtube.com/watch?v=oiZk0tIkR48&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=11