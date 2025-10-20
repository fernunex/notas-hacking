https://play.picoctf.org/practice/challenge/460
## Description
RED, RED, RED, RED Download the image: [red.png](https://challenge-files.picoctf.net/c_verbal_sleep/831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png)
## Solution
1. Download the image.
2. Use an analyzer of stenography to search for a hidden flag:
```
			zsteg red.png
```
3. We found a base64 string. We decode the string:
```
	echo cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ== | base64 -d
```
3. We found the flag:
```
	picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
```
## Additional notes
## References

