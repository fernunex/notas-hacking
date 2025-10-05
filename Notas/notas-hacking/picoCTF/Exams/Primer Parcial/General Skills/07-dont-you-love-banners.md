Can you abuse the banner?

Additional details will be available after launching your challenge instance.
## Description
Can you abuse the banner? The server has been leaking some crucial information on `tethys.picoctf.net 60950`. Use the leaked information to get to the server. To connect to the running application use `nc tethys.picoctf.net 59723`. From the above information abuse the machine and find the flag in the /root directory.
## Solution
1. Process to find the leaked password and enter into the server:
	![](../../../../images/Pasted%20image%2020251003215418.png)
	![](../../../../images/Pasted%20image%2020251003221428.png)
2. Inspecting the script that runs the banner.
	![](../../../../images/Pasted%20image%2020251003221706.png)
3. Creating the link to point to the flag:
	![](../../../../images/Pasted%20image%2020251003221353.png)
4. Relaunch the app or reconnect to the service:
	![](../../../../images/Pasted%20image%2020251003221804.png)
	We get the flag: `picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_218ef5d6}`
## Additional notes
## References

