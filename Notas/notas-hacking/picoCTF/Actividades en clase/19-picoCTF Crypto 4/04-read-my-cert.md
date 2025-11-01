https://play.picoctf.org/practice/challenge/367
## Description
How about we take you on an adventure on exploring certificate signing requests Take a look at this CSR file [here](https://artifacts.picoctf.net/c/426/readmycert.csr).
## Solution
1. Download the CSR file.
2. Read the certificate:
	```openssl req -in readmycert.csr -noout -text```
3. Get the flag: ```picoCTF{read_mycert_41d1c74c}```
## Additional notes
## References

https://en.wikipedia.org/wiki/Certificate_signing_request