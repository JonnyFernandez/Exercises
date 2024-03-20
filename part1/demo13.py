"""Ejercicio 13: Crear un programa que guarde en una variable el diccionario
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte
al usuario por una divisa y muestre su símbolo o un mensaje de aviso si
la divisa no está en el diccionario."""

diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥', "ARS": '$$'}

divisa = input("cual es tu divisa?: ")


if diccionario.get(divisa) != None:
    print(f"EL logo de tu moneda es: {diccionario.get(divisa)}")
else:
    print(f"No hay logo para: {divisa}")
    
