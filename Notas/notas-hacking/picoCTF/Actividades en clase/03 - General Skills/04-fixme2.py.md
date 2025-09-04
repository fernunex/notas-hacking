https://play.picoctf.org/practice/challenge/241
## Descripción
Fix the syntax error in the Python script to print the flag. [Download Python script](https://artifacts.picoctf.net/c/5/fixme2.py)
## Solución
1. Descargamos el script y lo abrimos con un editor de texto.
2. Nos percatamos que en la linea 22 esta tratando de comparar si la cadena de texto esta vacía pero esta usando un solo "=", y este este asignación, el de comparación debe ser doble "= =": 
```
		if flag = "": ----> if flag == "":
```
1. Corregimos esa parte, ejecutamos y nos arroja la flag:
```
picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}
```


## Notas adicionales
También es posible ejecutar el script, que nos arroje el error y leyendo el traceback poder identificar donde esta el error.
## Referencias

