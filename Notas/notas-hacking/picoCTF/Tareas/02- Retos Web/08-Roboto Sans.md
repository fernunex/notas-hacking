https://play.picoctf.org/practice/challenge/291
## Description
The flag is somewhere on this web application not necessarily on the website. Find it.
Check [this](http://saturn.picoctf.net:58523/) out.
## Solution
1. Go to the website.
2. Check the *\robots.txt* path, then decode the base64 string "anMvbXlmaWxlLnR4dA\=="
3. This send us to */js/myfile.txt* here we find the flag: ```picoCTF{Who_D03sN7_L1k5_90B0T5_032f1c2b}```
## Additional notes
## References

