https://play.picoctf.org/practice/challenge/130
## Description
I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/c0da20f29337e87ffb58ea987d8c596e/Forensics%20is%20fun.pptm)

## Solution
1. Download the file.
2. Extract all the contents:
```
	7z x Forensics\ is\ fun.pptm
```
3.  Explore all files and in one folder we found a file named "hiden".
4. Open the file and decode the flag:
```
	echo 'Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q' | tr -d " " | base64 -d
```

```
picoCTF{D1d_u_kn0w_ppts_r_z1p5}
```

## Additional notes
## References
https://www.reviversoft.com/en/file-extensions/pptm
