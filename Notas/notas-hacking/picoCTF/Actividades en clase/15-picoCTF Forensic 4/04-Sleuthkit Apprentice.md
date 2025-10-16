https://play.picoctf.org/practice/challenge/300
## Description
Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/137/disk.flag.img.gz)
## Solution
1. Download the image.
2. Decompress the image.
3. Check its partitions: `mmls disk.flag.img`
4. List the files of the Linux partitions using its offsets (the interesting is the third partition):
```
	fls -o 360448 disk.flag.im
```
5. We found only directories but they look interesting. So we make a recursive listing and grep for the flag:
```
 fls -o 360448 -r disk.flag.img | grep flag
```
6. Then we read the file called "flag.uni.txt" using its offset:
```
	icat -o 360448 disk.flag.img 2371
```
7. And we found the flag: `picoCTF{by73_5urf3r_adac6cb4}`
## Additional notes
## References

