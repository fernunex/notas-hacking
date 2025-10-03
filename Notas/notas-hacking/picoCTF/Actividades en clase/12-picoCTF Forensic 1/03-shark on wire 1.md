https://play.picoctf.org/practice/challenge/30
## Descripción
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap). Recover the flag.

## Solución
1. Download the pcap file and open it with Wireshark.
2. Filter for each stream udp until we find the flag. In this case we found it in stream 6.
	![](../../../Pasted%20image%2020251002182824.png)
3. The flag is: ```picoCTF{StaT31355_636f6e6e}```
## Notas adicionales
## Referencias
https://en.wikipedia.org/wiki/Pcap

