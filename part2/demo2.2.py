"""Ejercicio 2: Crear una lista con 10 números enteros cualquiera. Indicar cuál es el número mayor y cuál es el número menor.
 Si al menos hay 3 números mayores a 100, imprimir esos números, si no,
 imprimir los números menores a 50 que formen parte de la lista."""
 
lista = [1,2,3,4,5,6,7,8,9,0,111,123,124]
mayores = list()
menores = list()

for x in lista:
    if x > 100:
        mayores.append(x)
    elif x < 50:
        menores.append(x)

if len(mayores) >= 3:     
    print(f"numero menores que 100: {mayores}")
else:    
    print(f"numero manores que 50: {menores}")

print(f"numero mayor: {max(lista)}")
print(f"numero menor: {min(lista)}")