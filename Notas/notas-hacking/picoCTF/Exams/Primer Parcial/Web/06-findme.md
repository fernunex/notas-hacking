https://play.picoctf.org/practice/challenge/349
## Description
Help us test the form by submiting the username as `test` and password as `test!` The website running [here](http://saturn.picoctf.net:57850/).
## Solution
1. Go to the website.
2. Log in and inspect all requests and responses using Burpsuit. We found part of the flag in this reques, in the id of the page: cGljb0NURntwcm94aWVzX2Fs -> `picoCTF{proxies_al`
	![](../../../../images/Pasted%20image%2020251004152003.png)
3. Then we continue to forwarding GET request and we found the second part of the flag:
		bF90aGVfd2F5XzNkOWUzNjk3fQ== -> `l_the_way_3d9e3697}`
		![](../../../../images/Pasted%20image%2020251004152337.png)


And we found the flag: `picoCTF{proxies_all_the_way_3d9e3697}`
## Additional notes
## References

