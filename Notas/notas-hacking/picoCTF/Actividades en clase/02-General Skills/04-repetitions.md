https://play.picoctf.org/practice/challenge/371
## Descripción
Can you make sense of this file? Download the file [here](https://artifacts.picoctf.net/c/472/enc_flag).
## Solución
1. Descargamos el archivo y lo leemos con cat. Es fácil percatarnos que es base64 por lo que lo decodificamos con el comando `base64 -d`, pero observamos que queda aún en base64 por lo decodificamos hasta que sea la flag ya que el reto se llama "repetitions":
```
cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
```

2. Y obtenemos la flag:
```
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_73494190}
```

## Notas adicionales
## Referencias

