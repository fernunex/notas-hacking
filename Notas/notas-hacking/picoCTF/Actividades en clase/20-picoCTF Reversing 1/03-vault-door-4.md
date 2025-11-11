https://play.picoctf.org/practice/challenge/71
## Description
This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://challenge-files.picoctf.net/c_fickle_tempest/dfb236ca8b03fc1044ad906ce94fd2ed85beb1d1118f09234607b5f79d4b72fc/VaultDoor4.java)

## Solution
1. Download the code.
2. Convert with JS the char codes to string, and append the ascii characters:
```
String.fromCharCode(106 , 85 , 53 , 116 , 95 , 52 , 95 , 98 , 0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f, 0142, 0131, 0164, 063 , 0163, 0137, 066 , 064)
```
3. We got the flag: ```picoCTF{jU5t_4_bUnCh_0f_bYt3s_64e13d00b2}```
## Additional notes

## References


