"""Ejercicio 3: Crear una función que, a partir de un mensaje, nos devuelva una lista con todos los números,
si los hay, que aparecen en dicho mensaje."""

def numeros_en_mensaje(mensaje=input("ingresa tu mensaje: ")):
    lista = list()
    for num in mensaje:
        if num.isdigit():
             lista.append(int(num))
    print(lista)       

numeros_en_mensaje()   