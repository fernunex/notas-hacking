https://play.picoctf.org/practice/challenge/170
## Descripción
Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm) has extraordinarily helpful information...
## Solución
1. Descargamos el archivo.
2. Sé que la solución era ejecutar el binario otorgandole permisos de ejecución y haciendo un
```
./warm -h
```
1. Pero opte por el siguiente comando, ya que me dio miedo ejecutarlo y que fuera un virus jaja:
```
strings warm | grep pico
```
1. La flag es:
```
picoCTF{b1scu1ts_4nd_gr4vy_616f7182}
```
## Notas adicionales
## Referencias

