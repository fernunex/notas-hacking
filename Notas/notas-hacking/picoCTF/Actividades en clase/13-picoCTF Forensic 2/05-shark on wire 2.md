https://play.picoctf.org/practice/challenge/84
## Description
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/b506393b6f9d53b94011df000c534759/capture.pcap). Recover the flag that was pilfered from the network.
## Solution
1. Download the file.
2. All the packets of destination port == 22 contain the flag encoded in ascii in the source port of the sender.
3. Use the following exploit to extract them and decode in ascii characters:
```
from scapy.all import *
packets = rdpcap('capture.pcap') 
flag='' 
for p in packets: 
	if UDP in p and p[UDP].dport == 22: 
		if p[UDP].sport > 5000: 
			flag+=chr(p[UDP].sport - 5000) 
			
print(flag)
```

4. We found the flag: `picoCTF{p1LLf3r3d_data_v1a_st3g0}`
## Additional notes
## References
https://scapy.net/

