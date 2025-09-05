https://play.picoctf.org/practice/challenge/442
## Descripción
Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses. Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools! You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_atlas/6/challenge.zip)

Additional details will be available after launching your challenge instance.

## Solución

1. Nos conectamos con las credenciales que nos dio.
2. Después aplicamos el algoritmo de busqueda binaria, yo lo aplique manual con la calculadora de mi télefono, este fue el resultado:
```
		Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500
Lower! Try again.
Enter your guess: 250
Lower! Try again.
Enter your guess: 125
Higher! Try again.
Enter your guess: 187
Higher! Try again.
Enter your guess: 218
Lower! Try again.
Enter your guess: 202
Lower! Try again.
Enter your guess: 194
Higher! Try again.
Enter your guess: 198
Lower! Try again.
Enter your guess: 196
Congratulations! You guessed the correct number: 196
```
4. El algoritmo de búsqueda binaria es:
	![[Pasted image 20250905092239.png]]

5. Nos arrojo la flag: ```picoCTF{g00d_gu355_de9570b0}```
## Notas adicionales


## Referencias
https://en.wikipedia.org/wiki/Binary_search
