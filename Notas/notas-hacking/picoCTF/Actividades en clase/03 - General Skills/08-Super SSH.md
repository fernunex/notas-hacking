https://play.picoctf.org/practice/challenge/424
## Descripción
Using a Secure Shell (SSH) is going to be pretty important.

Additional details will be available after launching your challenge instance.

Can you `ssh` as `ctf-player` to `titan.picoctf.net` at port `64945` to get the flag? You'll also need the password `1db87a14`. If asked, accept the fingerprint with `yes`. If your device doesn't have a shell, you can use: [https://webshell.picoctf.org](https://webshell.picoctf.org/) If you're not sure what a shell is, check out our Primer: [https://primer.picoctf.com/#_the_shell](https://primer.picoctf.com/#_the_shell)
## Solución
1. Nos conectamos utilizando las credenciales indicadas y con el comando:
```
ssh ctf-player@titan.picoctf.net -p 64945
```
1. Y nos arroja la flag:
```
picoCTF{s3cur3_c0nn3ct10n_45a48857}
```

## Notas adicionales
Me conecte usando el comando ssh de Ubuntu.
## Referencias

