https://play.picoctf.org/practice/challenge/405
## Descripción
Someone's commits seems to be preventing the program from working. Who is it? You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/156/challenge.zip)
## Solución
1. Descomprimimos el zip y nos percatamos que es un archivo py que tiene un "Hello, World" con una falla de sintaxis. También podemos observar que tiene un .git, eso significa que esta versionado.
2. Realizamos un git log para ver su historial de commits y vemos que alguien ha realizado un montón de commits. Utilizamos ```git log | wc -l ```y nos indica que son 3011 líneas, por lo que optamos leerlo de abajo para arriba.
3. Utilizamos ```git log HEAD | tail -50``` para poder leer cuales fueron los primeros commits del repositorio y nos percatamos que ahi se encuentra la flag, en el segundo commit:
```
	picoCTF{@sk_th3_1nt3rn_d2d29f22}
```

## Notas adicionales

- También es posible con ```git shortlog | uniq``` , el primer comando nos agrupa los commits realizados por autor, el segundo nos imprime solo aquellas lineas que son diferentes.
- Finalmente imprimiendo todo en pantalla ```git log | cat ```también es una solución, ya que la flag aparece hasta el final de todos los commits, entonces la veriamos facilmente.

## Referencias

