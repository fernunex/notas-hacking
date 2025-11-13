https://play.picoctf.org/practice/challenge/402
## Description
Can you figure out how this program works to get the flag? Connect to the program with netcat: `$ nc saturn.picoctf.net 49664` The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/524/picker-III.py).
## Solution
1. Download the code.
2. Connect to the service.
3. Change the content of "func_table" by ```"print_table                     read_variable                   write_variable                  win                             "```
4. Then execute the 4th option and get the flag after decoding it from hexadecimal: ```picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_c20f5222}```

## Additional notes

## References

https://www.rapidtables.com/convert/number/hex-to-ascii.html
