https://play.picoctf.org/practice/challenge/378
## Description
Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most. Please start an instance to test your very own copy of Specialer.

Additional details will be available after launching your challenge instance.
`ssh -p 62653 ctf-player@saturn.picoctf.net`. The password is `fd7746b4`
## Solution
1. We enter into the machine.
2. Here we don't have cat, more, less, ls, etc. Then we use the following commands to:
	1. List directories and files: `echo */**`
	2. Read files we use: `echo "$(< abra/cadabra.txt)"`
	3. The flag is in `echo "$(< ala/kazam.txt)"`and the flag is `picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_38f5cc78}`

![](../../../../images/Pasted%20image%2020251004010006.png)
## Additional notes
## References

