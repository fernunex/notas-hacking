
## Descripción
There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 35652`, but it doesn't speak English...
## Solución
1. Conectarnos al hosy y puerto que nos indican.
2. Guardamos el output en un archivo: `nc mercury.picoctf.net 35652 > notEnglish.txt`
3. Leemos linea por linea y lo convertimos a su representación en ASCII usando awk (parecido al lenguaje C en su forma de imprimir):
```
	while IFS= read -r linea; do
	echo $linea | awk '{ printf "%c", $1 }'
	done < notEnglish.txt
```

Flag:
```
picoCTF{g00d_k1tty!_n1c3_k1tty!_9b3b7392}
```

## Notas adicionales
* Checar la tabla ASCII y convertirla manualmente.
* Usar una página web para convertir, por ejemplo, rapidtables.com
## Referencias
https://linuxize.com/post/how-to-read-a-file-line-by-line-in-bash/
