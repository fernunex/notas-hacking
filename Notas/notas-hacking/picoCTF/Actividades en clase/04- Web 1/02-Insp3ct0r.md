https://play.picoctf.org/practice/challenge/18
## Descripción
Kishor Balan tipped us off that the following code may need inspection: `https://jupiter.challenges.picoctf.org/problem/44924/` ([link](https://jupiter.challenges.picoctf.org/problem/44924/)) or http://jupiter.challenges.picoctf.org:44924

## Solución
1. Entramos la página web usando el link. Nos dice que usó tres tecnologías: HTML, CSS, JS. Como nos pide que la inspeccionemos entonces abrimos cada uno de los archivos con el inspector.
2. En el HTML encontramos: ```picoCTF{tru3_d3```. En la parte de Inspector.
3. En el JSS encontramos: ```t3ct1ve_0r_ju5t```. En la parte de Style Editor.
4. En el JS encontramos: ```_lucky?f10be399}```. En la parte de Debugger.
```picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?f10be399}```

## Notas adicionales
## Referencias
https://www.youtube.com/watch?v=f1infpFomIM&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=1

