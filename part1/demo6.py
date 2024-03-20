"""Ejercicio 6: Crear un programa que calcule cuánto dinero tendré al cabo de un mes
si deposito hoy 2000 en el banco y el interés mensual es de 5%, y luego devuelva por pantalla ese valor.
"""

deposito = float(input('monto: '))
porcentaje = 0.05
res = (deposito*porcentaje) + deposito
res2 = deposito*porcentaje
print(f"con el monto de {deposito}, tendras una ganacia de {res2}, que sumado a tu capital seria {res}")


