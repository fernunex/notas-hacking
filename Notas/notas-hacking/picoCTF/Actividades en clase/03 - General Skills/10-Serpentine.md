https://play.picoctf.org/practice/challenge/251
## Descripción
Find the flag in the Python script! [Download Python script](https://artifacts.picoctf.net/c/35/serpentine.py)
## Solución
1. Descargamos el script.
2. Corremos el script y ejecutamos todas las opciones, la opción que nos debería imprimir la flag dice que pusieron la función equivocada. Entonces la corregimos y en la opción b) colocamos lo siguiente:
```
if choice == 'a':
      print_encouragement()
      
    elif choice == 'b':
     print_flag() 
    elif choice == 'c':
      sys.exit(0)
      
    else:
      print('\nI did not understand "' + choice + '", input only "a", "b" or "c"\n\n')
```
3. Corremos nuevamente el scrip y ahora cuando eligamos la opción b) obtendremos la flag:
```
picoCTF{7h3_r04d_l355_7r4v3l3d_ae0b80bd}
```


## Notas adicionales

## Referencias

