https://play.picoctf.org/practice/challenge/261
## Description
We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it? Download the leak [here](https://artifacts.picoctf.net/c/151/leak.tar). The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.
## Solution
1. Download the files.
2. Find the number line of the user "cultiris": ```grep -n cult usernames.txt```-> 378
3. Find his password: ```head passwords.txt -n 378 | tail -1```-> cvpbPGS{P7e1S_54I35_71Z3}
4. Rot-13 the password and found the flag: ```picoCTF{C7r1F_54V35_71M3}```

## Additional notes
## References
https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)&input=Y3ZwYlBHU3tQN2UxU181NEkzNV83MVozfQ

