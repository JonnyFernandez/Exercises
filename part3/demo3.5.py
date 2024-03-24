"""Ejercicio 5: Crear una función que devuelva True si los parámetros ingresados son todos números,
False si hay al menos uno de los parámetros ingresados que no es un número,
y None si ninguno de los parámetros ingresados es un número. Imprimir resultado por pantalla."""

def Booleand_item(*data):
    lista = list()
    for item in data:
        if type(item) == int or type(item) == float or type(item) == complex:
            lista.append(item)
    if len(data) == len(lista):
        return True
    elif len(lista) != 0:
        return False
    else:
        return None        
         
print(Booleand_item(3j,2,5))    
    