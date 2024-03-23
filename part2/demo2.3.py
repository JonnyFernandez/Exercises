"""Ejercicio 3: Pedir al usuario que ingrese por teclado 2 números,
 si el primero es menor que el segundo imprimir la resta entre el segundo y el primero,
si el primero es mayor que el segundo imprimir la suma de ambos, y si son iguales imprimir su producto."""

lista = list()

for x in range(2):
    numeros = int(input(f"ingresar {x+1}° numero: "))
    lista.append(numeros)

if lista[0] < lista[1]:
    print(f"La resta entre el segundo y el primero: {lista[1] - lista[0]}")    
elif  lista[0] > lista[1]:
    print(f"La suma entre el segundo y el primero: {lista[1] + lista[0]}")   
elif  lista[0] == lista[1]:    
    print(f"La producto entre el segundo y el primero: {lista[1] * lista[0]}")    