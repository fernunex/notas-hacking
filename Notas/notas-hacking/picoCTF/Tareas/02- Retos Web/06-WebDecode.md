https://play.picoctf.org/practice/challenge/427
## Description
Do you know how to use the web inspector?

Additional details will be available after launching your challenge instance.
Start searching [here](http://titan.picoctf.net:51229/) to find the flag
## Solution
1. Go to the website.
2. Inspect all pages, and in the page *about.html* we found the following attribute ***notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMDJjZGNiNTl9"***.
3. Decode it in base 64:
	```echo cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMDJjZGNiNTl9 | base64 -d```
4. And the flag is: ```picoCTF{web_succ3ssfully_d3c0ded_02cdcb59}```
## Additional notes
## References

