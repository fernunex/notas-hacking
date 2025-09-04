
## Descripción
What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.

## Solución
Como habla de bases y al observar la cadena son solo letras y números se puede deducir que es base 64 debido a  que este es usado para codificar de binarios a texto.
Usar el decoder/encoder base64 de Linux.

```
echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d
```

Flag:
```
picoCTF{l3arn_th3_r0p35}
```

## Notas adicionales
* Utilizar un decoder/encoder base 64 de alguna página web.
## Referencias

