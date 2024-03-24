"""Ejercicio 8: Crear una función que calcule cuántos litros de nafta gasta un auto que consume 2 litros x 100km,
en un viaje ida y vuelta MdP-Bue si la distancia es de 400km. Luego crear una función que, a partir de esos datos,
devuelva cuánto significa eso en pesos si el litro de nafta está 60$."""

def Calculo_consumo(distancia=int(input("ingresar distancia: ")) ):
    autonomia_x_100km = 2
    km = 100
    return distancia * (autonomia_x_100km / km)


def Canculo_monetario():
    gasolina = Calculo_consumo()
    return f"El gasto monerario seria de {gasolina * 60}"



print(Calculo_consumo())
print(Canculo_monetario())