https://play.picoctf.org/practice/challenge/285
## Description
Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/213/disk.flag.img.gz)
## Solution
1. Download the image.
2. Decompress the image.
3. We list recursively the files in the last partition and we found the flag encrypted:
```
	fls -o 411648 -r disk.flag.img | grep flag
```
4. We check the history commands on the file to check how it was encrypted:
	With the next command we found the offset of the command history which is 1875:
```
	fls -o 411648 -r disk.flag.img | grep history	
```
![](../../../images/Pasted%20image%2020251016104455.png)
5. Save the encrypted flag in a file.
```
	icat -o 411648 disk.flag.img 1782 > flag.txt.enc
```
5. Unencrypt the flag using the password used to encrypt it:
```
	openssl aes256 -salt -d -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
```
5.  And we got the flag: `picoCTF{h4un71ng_p457_5113beab}`
## Additional notes
## References

