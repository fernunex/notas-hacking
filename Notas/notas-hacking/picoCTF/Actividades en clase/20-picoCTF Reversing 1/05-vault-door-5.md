https://play.picoctf.org/practice/challenge/77
## Description
In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: [VaultDoor5.java](https://challenge-files.picoctf.net/c_fickle_tempest/e0273648f1276c71952d98ee6611263932f766fd288de297c1881a0e4fcd775c/VaultDoor5.java)
## Solution
1. Download the code.
2. Use cyberchef to decode from base64 then decode from URL and we got the flag:
	```picoCTF{c0nv3rt1ng_fr0m_ba5e_64_42c6409b}```

## Additional notes
1. We could also use Python or JS to decode from base 64 and then decode the URL.

## References
https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)URL_Decode(true)&input=SlRZekpUTXdKVFpsSlRjMkpUTXpKVGN5SlRjMEpUTXhKVFpsSlRZM0pUVm1KVFkySlRjeUpUTXdKVFprSlRWbUpUWXlKVFl4SlRNMUpUWTFKVFZtSlRNMkpUTTBKVFZtSlRNMEpUTXlKVFl6SlRNMkpUTTBKVE13SlRNNUpUWXk

