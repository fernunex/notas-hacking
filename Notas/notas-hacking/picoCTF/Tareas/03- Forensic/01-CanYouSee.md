https://play.picoctf.org/practice/challenge/408
## Description
How about some hide and seek? Download this file [here](https://artifacts.picoctf.net/c_titan/5/unknown.zip).

## Solution
1. Download the file.
2. Decompress the file and get the image.
3. Check the image's metadata with `exiftool ukn_reality.jpg`
4. Decode in base64 the Attribution URL: 
```
	echo cGljb0NURntNRTc0RDQ3QV9ISUREM05fNGRhYmRkY2J9Cg== | base64 -d
```
5.  And get the flag: 
```
	picoCTF{ME74D47A_HIDD3N_4dabddcb}
```
## Additional notes
## References

