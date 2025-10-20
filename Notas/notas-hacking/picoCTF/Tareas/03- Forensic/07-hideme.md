https://play.picoctf.org/practice/challenge/350
## Description
Every file gets a flag. The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/259/flag.png).
## Solution
1. Download the image.
2. Extract the embedded file with the following command:
```
binwalk -e flag.png
```
3. And we get the flag in the second image.
```
	picoCTF{Hiddinng_An_imag3_within_@n_ima9e_cda72af0}
```
## Additional notes
## References

