https://play.picoctf.org/practice/challenge/129
## Description
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/5eb456e480e485183c9c1b16952c6eda/dolls.jpg)
## Solution
1. Download the image.
2. Extract the files embedded in the image using binwalk:
```
	binwalk -e dolls.jpg
	binwalk -e 2_c.jpg
	binwalk -e 3_c.jpg
	binwalk -e 4_c.jpg
	
```
3. Then we will get a file named flag.txt that contains the flag: `picoCTF{336cf6d51c9d9774fd37196c1d7320ff}`

## Additional notes
## References

