https://play.picoctf.org/practice/challenge/66
## Descripción
Can you break into this super secure portal? `https://jupiter.challenges.picoctf.org/problem/29835/` ([link](https://jupiter.challenges.picoctf.org/problem/29835/)) or http://jupiter.challenges.picoctf.org:29835

---
## Solución
1. Accedemos a la liga y nos damos cuenta que nos pide una contraseña. Es difícil saber cual es por lo tanto vamos a seguir explorando.
2. Con el inspector inspeccionamos la página y nos damos cuenta que la password esta siendo validada del lado del cliente y no esta encriptada:
```
function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {----------------------> 1st
      if (checkpass.substring(split*6, split*7) == '723c') { -----------> 7th
        if (checkpass.substring(split, split*2) == 'CTF{') { -----------> 2nd
         if (checkpass.substring(split*4, split*5) == 'ts_p') { --------> 5th
          if (checkpass.substring(split*3, split*4) == 'lien') {--------> 4th
            if (checkpass.substring(split*5, split*6) == 'lz_7') {------> 6th
              if (checkpass.substring(split*2, split*3) == 'no_c') {----> 3rd
                if (checkpass.substring(split*7, split*8) == 'e}') {----> 8th
                  alert("Password Verified")
                  }
                }
              }
      
            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }
    
  }
```
3. Entendiendo el código y viendo como es el orden de las substrings nos damos cuenta que la flag es:
```
picoCTF{no_clients_plz_7723ce}
```

---


## Notas adicionales
## Referencias
https://www.youtube.com/watch?v=19Hkmb1Guzk&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=4&pp=iAQB


