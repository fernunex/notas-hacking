https://play.picoctf.org/practice/challenge/400
## Description
This service can provide you with a random number, but can it do anything else? Connect to the program with netcat: `$ nc saturn.picoctf.net 56914` The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/514/picker-I.py).

## Solution
1. Download the code.
2. Connect to the service.
3. Enter the name of the function "win()".
4. Convert the hexadecimal characters to unicode and get the flag:
	```picoCTF{4_d14m0nd_1n_7h3_r0ugh_6e04440d}```

## Additional notes

## References

https://www.rapidtables.com/convert/number/hex-to-ascii.html
