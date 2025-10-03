https://play.picoctf.org/practice/challenge/296
## Description
We have several pages hidden. Can you find the one with the flag?
The website is running [here](http://saturn.picoctf.net:58903/).
## Solution
1. Go to the website.
2. Inspect the about.html page and we found there is a route: http://saturn.picoctf.net:61232/secret/. We access it and then that opens a new page.
3. We inspect the page and we discover there is route to: http://saturn.picoctf.net:61232/secret/hidden/. We access and inspect it and we discover is another page.
4. http://saturn.picoctf.net:61232/secret/hidden/superhidden/ here we found the flag inspecting its HTML.
	 ```picoCTF{succ3ss_@h3n1c@10n_39849bcf}```
## Additional notes
## References

