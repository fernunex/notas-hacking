https://play.picoctf.org/practice/challenge/186
## Description
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/a614a27d4cb251d04c7d2f3f3f76a965/cat.jpg)

## Solution
1. Download the image.
2. Check the image's metadata with `exiftool cat.jpg`
3. Decode in base64 the License: 
```
	echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d
```
5.  And get the flag: 
```
	picoCTF{the_m3tadata_1s_modified}
```

## Additional notes
## References

