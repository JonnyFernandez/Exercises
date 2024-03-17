"""Ejercicio 9: Crear un programa que pregunte al usuario 5 números enteros
 y devuelva una lista con ellos."""
 
users_num = list()

for x in range(5):
    numero = int(input(f"dame un numero: "))
    users_num.append(numero)

print(users_num)