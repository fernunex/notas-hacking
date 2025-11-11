https://play.picoctf.org/practice/challenge/60
## Description
This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://challenge-files.picoctf.net/c_fickle_tempest/856cff883937e1cfe99e7e5b9c2fbbf08232a8135f919b1111615f007a4de03a/VaultDoor3.java)
## Solution
1. Download the code.
2. Run the part of the code that manipulates the input string:
```
var password = "jU5t_a_sna_3lpm11g54e_u_4_m4r042"
var buffer = Array(32);
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }

buffer.join("")
```
1. We got the flag: ```picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_e45012}```
## Additional notes

## References


