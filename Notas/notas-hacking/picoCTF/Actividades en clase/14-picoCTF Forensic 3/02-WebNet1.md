https://play.picoctf.org/practice/challenge/42
## Description
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/picopico.key). Recover the flag.
## Solution
1. Download the files.
2. Open the pcap with wireshark and load the key to decrypt the data.
3. Then the flag is in the binary data of the image:
![](../../../images/Pasted%20image%2020251014205252.png)
Flag: `picoCTF{honey.roasted.peanuts}`
## Additional notes
1. Using `ssldump` could be an alternative:
```
ssldump -r capture.pcap -k picopico.key -d | grep pi -A 10
```
## References

