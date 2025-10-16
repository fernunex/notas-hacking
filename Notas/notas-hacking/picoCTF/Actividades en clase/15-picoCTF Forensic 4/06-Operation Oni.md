https://play.picoctf.org/practice/challenge/284
## Description
Download this disk image, find the key and log into the remote machine. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

Additional details will be available after launching your challenge instance.
Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download disk image](https://artifacts.picoctf.net/c/70/disk.img.gz)
- Remote machine: `ssh -i key_file -p 61533 ctf-player@saturn.picoctf.net`
## Solution
1. Download the image.
2. Decompress the image.
3. Check the partition to know what are the offset:
```
	mmls disk.img
```
4. List directories and files until we found the key "id_ed25519" file:
```
fls -o 206848 disk.img
fls -o 206848 disk.img 470
fls -o 206848 disk.img 3916
```
5. Then save the key in a file:
```
icat -o 206848 disk.img 2345 > keysh
```
6. Log in using the key:
```
ssh -i key_file -p 56443 ctf-player@saturn.picoctf.net
```
7. And we found the flag:
```
picoCTF{k3y_5l3u7h_b5066e83}
```
## Additional notes
## References

