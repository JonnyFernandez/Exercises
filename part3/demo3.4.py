"""Ejercicio 4: Crear una función que, a partir de 4 números,
 devuelva el mayor producto de dos de ellos. Imprimir resultado por pantalla."""


def Mayor_prod(*x):
   lista = list(x)
   lista.sort()
   print(lista[-1]*lista[-2])
   


Mayor_prod(2,3,4,5,7)    