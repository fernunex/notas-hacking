https://play.picoctf.org/practice/challenge/113
## Description
Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: [dds1-alpine.flag.img.gz](https://mercury.picoctf.net/static/2f998eee12730cf5766624681212a441/dds1-alpine.flag.img.gz)
## Solution
1. Download the image.
2. Decompress the file:
	`7z x dds1-alpine.flag.img.gz`
3. Search for strings inside the disk image:
```
	srch_strings dds1-alpine.flag.img | grep pico
```
4. We found the flag: `picoCTF{f0r3ns1c4t0r_n30phyt3_267e38f6}`
## Additional notes


## References

