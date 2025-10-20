https://play.picoctf.org/practice/challenge/418
## Description
Can you get the real meaning from this file. Download the file [here](https://artifacts.picoctf.net/c_titan/3/enc_flag).
## Solution
1. Download the file.
2. Decode in base64 the text two times.
3. Apply Cesar Cipher with a shif of 19 and get the flag: `picoCTF{caesar_d3cr9pt3d_b204adc6}`
## Additional notes
## References

https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,19)&input=d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ