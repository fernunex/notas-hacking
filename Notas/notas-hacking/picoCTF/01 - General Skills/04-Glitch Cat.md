https://play.picoctf.org/practice/challenge/242
## Descripción
Our flag printing service has started glitching!

Additional details will be available after launching your challenge instance.


Our flag printing service has started glitching! 
`$ nc saturn.picoctf.net 65186`

## Solución

1. Nos conectamos con el comando que nos da y recibimos esto:

'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'

2. Parece que la cadena esta glitcheada y debemos de averiguar la representación en ASCII de los códigos en hexadecimal (los hexadecimales empiezan con el prefijo 0x) "chr(0x39)"
3. Pegamos estos códigos en la siguiente web: https://www.rapidtables.com/convert/number/hex-to-ascii.html
4.  Obtenemos la cadena "9c42a45d" y completamos la flag.

Flag 
```
picoCTF{gl17ch_m3_n07_9c42a45d}
```

## Notas adicionales
Tambien es posible usar:
`echo "0x39 0x63 0x34 0x32 0x61 0x34 0x35 0x64" | xxd -r`

xxd es un comando para convertir a hexdump y con el flag -r lo reverseamos.
## Referencias

