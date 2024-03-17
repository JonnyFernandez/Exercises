"""Ejercicio 7: Crear un programa que calcule el sueldo bruto de una persona que trabaja de lunes a viernes 8 hs y
  su pago por hora es de 400 pesos. Devolver el sueldo por pantalla."""
  

jornada = int(input("dias trabajados: "))

if jornada == 5:
    print(f"estas re bien, estas trajando {jornada}, y tu sueldo semanal es de {jornada * 8 * 400}")
    print(f"lo que seria al mes: {jornada * 8 * 400 * 4} ")
  