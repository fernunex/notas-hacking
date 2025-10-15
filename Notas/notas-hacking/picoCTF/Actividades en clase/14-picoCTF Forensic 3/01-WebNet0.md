https://play.picoctf.org/practice/challenge/32
## Description
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/picopico.key). Recover the flag.
## Solution
1. Download the pcap and the key.
2. Abrimos el archivo con wireshark:
	`wireshark capture.pcap &2>/dev/null disown`
3. Cargamos la llave en Edit y Preferencias. En el protocolo TLS.
4. Buscamos una coincidencia "picoCTF" en la información de todos los paquetes:
![](../../../images/Pasted%20image%2020251013200429.png)

Encontramos la flag: `picoCTF{nongshim.shrimp.crackers}`


## Additional notes
## References
https://en.wikipedia.org/wiki/Transport_Layer_Security
