"""Ejercicio 10: Crear una función decoradora para una función matemática cualquiera."""

def decorador(funcion):
    def wrapper(x,y):
        print("Antes de llamar a la función")
        funcion(x,y)  # Llama a la función original
        print("Después de llamar a la función")
    return wrapper



@decorador
def suma(x,y):
    print(f"Suma de parametros: {x + y}")


@decorador
def resta(x,y):
     print(f"Resta de parametros: {x - y}")

@decorador
def producto(x,y):
     print(f"Producto de parametros: {x * y}")

@decorador
def cociente(x,y):
     print(f"Cociente de parametros: {x / y}")

# Llamada a la función decorada
cociente(4,5)
