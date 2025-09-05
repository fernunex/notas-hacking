https://play.picoctf.org/practice/challenge/410
## Descripción
My team has been working very hard on new features for our flag printing program! I wonder how they'll work together? You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/177/challenge.zip)

## Solución
1. Descargamos el zip y lo descomprimimos.
2. Viajamos por cada una de las ramas (feature/part-1 a la 3) y vamos construyendo la flag parte por parte.
```
git checkout feature/part-1
cat flag.py
----> picoCTF{t3@mw0rk_
git checkout feature/part-2
cat flag.py
----> m@k3s_th3_dr3@m_
git checkout feature/part-2
cat flag.py
----> w0rk_7ae8dd33}
```
3. Resultado:
```
picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_7ae8dd33}
```
## Notas adicionales


## Referencias

