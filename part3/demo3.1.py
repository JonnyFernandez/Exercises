"""Ejercicio 1: Crear una función que, a partir de un dato de entrada que sea en horas, nos informe cuántos minutos
y cuántos segundos serían esas horas. Imprimir por pantalla dichos valores."""

def hour_minutes_seg(hour = int(input("ingresar hora: "))):
    print(f"{hour}hs en minutos sera: {hour * 60}")
    print(f"{hour}hs en segundos sera: {hour * 3600}")
    
hour_minutes_seg()   