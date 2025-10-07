https://play.picoctf.org/practice/challenge/51
## Description
I stopped using YellowPages and moved onto WhitePages... but [the page they gave me](https://jupiter.challenges.picoctf.org/static/95be9526e162185c741259a75dffa0ab/whitepages.txt) is all blank!
## Solution
1. Download the file.
2. Install pwntools in python: `python3 -m pip install pwntools`
3. We change the bytes xe2, x80, x83 by 0, and x20 by 1. Then we convert it to ascii (every 8 bits is an ascii character) with this script:
	```
	from pwn import *
	file = open('whitepages.txt', 'rb')
	data = bytearray(file.read())
	data = data.replace(b'\xe2\x80\x83', b'0')
	data = data.replace(b'\x20', b'1')
	data = data.decode('ascii')
	data = unbits(data)
	print(data)
	```
4. And we found the flag: `picoCTF{not_all_spaces_are_created_equal_7100860b0fa779a5bd8ce29f24f586dc}`
## Additional notes
1. Or we can use sed:
	```sed 's/\xe2\x80\x83/0/g' whitepages.txt | sed 's/\x20/1/g'```
## References

https://en.wikipedia.org/wiki/Unicode
https://en.wikipedia.org/wiki/UTF-8