https://play.picoctf.org/practice/challenge/459
## Description
A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag. To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder! Find the PCAP file here [Network Traffic PCAP file](https://challenge-files.picoctf.net/c_verbal_sleep/3fe089c41615b9413666bedca922e07bf6ad8894a3dabd2737735143ad2396cf/myNetworkTraffic.pcap) and try to get the flag.
## Solution
1. Open the pcap file with wireshark.
2. Decode in base64 the string of the load of this packets, the packets with 52 bytes of length.
	![](../../../images/Pasted%20image%2020251020165449.png)

We get the flag: picoCTF{1t_w4snt_th4t_34sy_tbh_4r_966d0bfb}



## Additional notes
## References

