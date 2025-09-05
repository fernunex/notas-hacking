https://play.picoctf.org/practice/challenge/377
## Descripción
Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM) Start your instance to see connection details. `ssh -p 49439 ctf-player@saturn.picoctf.net` The password is `fd7746b4`
## Solución

1. Nos conectamos con las credenciales que nos indicaron.
2. Nos percatamos que tendremos que usar una sintaxis que pueda burlar en como la shell o el script nos esta modificando lo que introduciomos. Para eso checamos esta documentación:
	https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html
	https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html
	https://www.gnu.org/software/bash/manual/html_node/Shell-Parameters.html
3. De esta manera obtuve la bandera, utilizando una sintaxis de asignación (shell parameter expansion) de parámetros, es decir, cuando asignamos un parámetro a una variable por asi decirlo con esta sintaxis lo que nos devuelve es el mismo parámetro y este lo termina ejecutando como un texto normal y como la sintaxis es la correcta de bash entonces si es ejecutado:
```
blargh
Special$ ${otraShell=/bin/bash}
Why go back to an inferior shell?
Special$ ${Listar='ls -la'}
${Listar='ls la's 
sh: 1: Syntax error: Missing '}'
Special$ ${Listar="cat blargh"}  
${Listar="cat blargh"} 
cat: blargh: Is a directory
Special$ ${Listar="ls -la blargh"}         
${Listar="ls la blargh"} 
ls: cannot access 'la': No such file or directory
blargh:
flag.txt
Special$ ${Listar="ls blargh"}                
${Listar="ls blargh"} 
flag.txt
Special$ ${Listar="cat blargh/flag.txt"}
${Listar="cat blargh/flag.txt"} 
picoCTF{5p311ch3ck_15_7h3_w0r57_f578af59}Special$ 


```

Basicamente la idea es asignar un comando a una variable utilizando una sintaxis que pase las transformaciones que realiza esta Shell Special y que al ejecutarse este asignación se expanda y sea corrida por la bash exitosamente.
La asignación ```var=123``` no pasaba pero la asignación ```${var=DEFAULT}```sí.



4. Y la flag es:
```
picoCTF{5p311ch3ck_15_7h3_w0r57_f578af59}
```
## Notas adicionales
## Referencias

