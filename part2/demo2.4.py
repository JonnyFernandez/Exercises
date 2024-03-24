"""Ejercicio 4: Ingresar 6 números por teclado, preferentemente enteros,
ordenarlos de manera creciente e imprimirlos por pantalla."""

lista = list()

for x in range(6):
    number = int(input(f"Ingreso {x+1} de 6: "))
    lista.append(number)
lista.sort()

print(lista)    