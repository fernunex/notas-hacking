https://play.picoctf.org/practice/challenge/12
## Description
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://jupiter.challenges.picoctf.org/static/ff2585f7afd21b81f69d2fbe37c081ae/VaultDoor1.java)
## Solution
1. Download the code.
2. Read the code and extract this part in another file:
	![](../../../Pasted%20image%2020251110205505.png)
	with the following command: ```tail VaultDoor1.java -n 34 | head -n 32 > flag.txt```

3. Make all digits of two digits number (1 -> 01).
4. With the following command we select the 3rd column, eliminate the single quote character (') and the new line character (\n):
		```sort flag.txt | awk '{print($3)}' | tr -d "'" | tr -d "\n"```
And we get the flag:
	```picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}```


## Additional notes

## References

https://www.youtube.com/watch?v=QZ1ttEjyKxY&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=48
