"""Ejercicio 16: Crear un programa que cree un diccionario vacío y
lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo,
teléfono, correo electrónico, etc.) que se le pida al usuario.
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario."""


claves_usuario=["nombre","edad","sexo","telefono","correo electronico","domicilio","color favorito"]

diccionario = dict()

for clave in claves_usuario:
    valor = input(f"ingrese su {clave}: ")
    diccionario[clave] = valor
    print(diccionario)
print(f"informacion de usuario: {diccionario}")    