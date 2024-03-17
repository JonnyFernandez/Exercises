"""Ejercicio 8: Crear un programa que almacene en una lista las siguientes materias:
Historia, Matemática, Lengua y Geografía. Luego devolver por
pantalla la última materia almacenada."""

lista1 = list([])
listaMaterias= ["Historia","Matemática", "Lengua","Geografía"]

lista1.extend(listaMaterias)

print(lista1[-1])
