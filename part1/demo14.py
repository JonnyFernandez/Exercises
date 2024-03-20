"""Ejercicio 14: Crear un programa que pregunte al usuario su nombre, edad, dirección y teléfono
 y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje.
"""


nombre = input("Cual es tu nombre? ")
edad = input("Edad: ")
dirección = input("Dirección: ")
teléfono = input("Telefono")

# diccionario = dict()
# diccionario["name"] = nombre
# diccionario["edad"] = edad
# diccionario["dirección"] = dirección
# diccionario["teléfono"] = teléfono

diccionario = {"nombre": nombre, "edad":edad, "dirección":dirección,"teléfono":teléfono}

print(diccionario)