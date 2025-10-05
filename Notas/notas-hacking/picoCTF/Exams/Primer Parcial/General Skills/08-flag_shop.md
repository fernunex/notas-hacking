https://play.picoctf.org/practice/challenge/49
## Description
There's a flag shop selling stuff, can you buy a flag? [Source](https://jupiter.challenges.picoctf.org/static/dd28f0987f28c894f35d5d48564c3402/store.c). Connect with `nc jupiter.challenges.picoctf.org 44566`.
## Solution
1. We download the code.
2. Inspect the code and we found this vulnerability:
	![](../../../../images/Pasted%20image%2020251003231454.png)
3. Using this flow we can increase our balance and buy the flag.
	![](../../../../images/Pasted%20image%2020251003230954.png)
The flag is `picoCTF{m0n3y_bag5_68d16363}`



picoCTF{m0n3y_bag5_68d16363}
## Additional notes
## References

