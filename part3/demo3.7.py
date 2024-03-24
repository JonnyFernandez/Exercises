"""Ejercicio 7: Crear una función que verifique si una palabra es un palíndromo o no. En caso de que lo sea devolver por pantalla
 "La palabra es un palíndromo", en caso contrario, devolver "La palabra no es un palíndromo"."""
 
def Polindromo(word):
    if word == word[::-1]:
        return f"la palabra {word}, es polimbroma"
    else:
        return f"la palabras {word}, no es pilimdroma"

print(Polindromo("reconocer"))    
 
 