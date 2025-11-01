https://play.picoctf.org/practice/challenge/100
## Description
I have these 2 images, can you make a flag out of them? [scrambled1.png](https://mercury.picoctf.net/static/6e4afb967ef8c865f79f3a8cd7767cca/scrambled1.png) [scrambled2.png](https://mercury.picoctf.net/static/6e4afb967ef8c865f79f3a8cd7767cca/scrambled2.png)
## Solution
1. Download the images.
2. Download and install stegsolve (link below) and open the tool:
	```java -jar stegsolve.jar```
3. Mix the images using AND and we got the flag: ```picoCTF{0542dc1d}```
	![](../../../images/Pasted%20image%2020251031141242.png)
## Additional notes
1. We could also write a exploit using Pyhton.
2. ![](../../../images/Pasted%20image%2020251031141730.png)

## References
https://en.wikipedia.org/wiki/Visual_cryptography

https://www.youtube.com/watch?v=zWU6MV8dQQ4&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=43

https://github.com/zardus/ctf-tools/blob/master/stegsolve/install
