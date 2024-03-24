"""Ejercicio 2: Crear una función que devuelva una lista con todos los
 números pares del 0 al 100 inclusive. Imprimir esa lista por pantalla."""
 
def numerador_par():
    lista = list()
    for x in range(101):
        if x%2 ==0:
            lista.append(x)
    print(lista)  

numerador_par()        