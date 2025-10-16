https://play.picoctf.org/practice/challenge/301
## Description
Download the disk image and use `mmls` on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory. [Download disk image](https://artifacts.picoctf.net/c/164/disk.img.gz)

Additional details will be available after launching your challenge instance.
Access checker program: `nc saturn.picoctf.net 60188`
## Solution
1. Download the image.
2. Check the partition info using:
```
	mmls disk.img
```
3. Submit the length: `202752`of the Linux partition and we get the flag: `picoCTF{mm15_f7w!}`
## Additional notes


## References

