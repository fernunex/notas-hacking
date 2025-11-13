https://play.picoctf.org/practice/challenge/403
## Description
Can you figure out how this program works to get the flag? Connect to the program with netcat: `$ nc saturn.picoctf.net 49827` The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/527/picker-IV.c). The binary can be downloaded [here](https://artifacts.picoctf.net/c/527/picker-IV).
## Solution
1. Download the code and the binary.
2. We found out that we need to enter the memory direction of the "win()" function.
3. Use ```gdb picker-IV```to use the gnu debugger on the executable file, then list the info about functions with ```info functions``` and we that win is at "0x040129e"
	![](../../../Pasted%20image%2020251112213412.png)
4. Enter the direction ```040129e```and get the flag ```picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_01672a61}```
## Additional notes

## References


