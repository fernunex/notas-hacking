https://play.picoctf.org/practice/challenge/53
## Description
We found this [file](https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery). Recover the flag.
## Solution
1. Download the file.
2. Fix its magic numbers with: 89 50 4e 47 0d 0a 1a 0a
3. Fix the first chunk, the critical chunk, it must say: IHDR.
	Correct these chunks:
		Use `pngcheck -v mystery`to check the integrity of the image.
	![](../../../images/Pasted%20image%2020251006185503.png)

4. Open the image and found the flag:`picoCTF{c0rrupt10n_1847995}`
![](../../../images/Pasted%20image%2020251006185723.png)
## Additional notes
## References
https://en.wikipedia.org/wiki/PNG
