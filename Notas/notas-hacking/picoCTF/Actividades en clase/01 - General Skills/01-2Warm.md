https://play.picoctf.org/practice/challenge/86
## Descripción
Can you convert the number 42 (base 10) to binary (base 2)?
## Solución
 Solucion manual:
 32 = 2⁵ = bin(10000)
 8 = 2³ = bin(100)
 2 = 2¹ = bin(10)
32+8+2 = 42 = 101010

picoCTF{101010}
## Notas adicionales
* Se puede usar  bc (binary calculator in bash):
```
echo "obase=2; ibase=10; 42" | bc
```

* La calculadora de un Linux en modo programador o alguna página en internet.
## Referencias

