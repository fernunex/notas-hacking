https://play.picoctf.org/practice/challenge/351
## Description
How about some hide and seek heh? Look at this image [here](https://artifacts.picoctf.net/c/237/atbash.jpg).
## Solution
1. Download the image.
2. Extract the hidden information with:
	```steghide extract -sf atbash.jpg```
3. We got the next encrypted text:
	```krxlXGU{zgyzhs_xizxp_05y2z65z}```
4. Use Cyberchef atBash cipher to unchiper:
	```picoCTF{atbash_crack_05b2a65a}```
## Additional notes
## References

https://gchq.github.io/CyberChef/#recipe=Atbash_Cipher()&input=a3J4bFhHVXt6Z3l6aHNfeGl6eHBfMDV5Mno2NXp9

