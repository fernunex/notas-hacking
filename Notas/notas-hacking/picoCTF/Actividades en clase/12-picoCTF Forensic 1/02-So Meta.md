https://play.picoctf.org/practice/challenge/19
## Descripción
Find the flag in this [picture](https://jupiter.challenges.picoctf.org/static/00efdf2961da1e21470ffc0d496c3cc2/pico_img.png).
## Solución
1. Download the image.
2. Check its metadata:
	![](../../../Pasted%20image%2020251002181334.png)
	Flag: ```picoCTF{s0_m3ta_fec06741}```
## Notas adicionales
1. It's possible to obtain the flag reading its binary data:
	```strings pico_img.png | grep pico```
## Referencias
https://en.wikipedia.org/wiki/Metadata
