"""Ejercicio 9: Crear un diccionario con 10 estudiantes y sus respectivas notas. Luego crear una función que nos
 informe los estudiantes aprobados (nota >= 7), los estudiantes desaprobados (4 <= nota < 7) y
  los estudiantes aplazados (0 <= nota < 4)."""

alumnos = dict()  
  
for x in range(5):
    nombre = input(f"Estudiante {x+1} de 5")
    nota = int(input("ingresar nota"))
    alumnos[nombre] = nota
   
def boletin():
    aprobados = dict()   
    desaprobados = dict()   
    aplazados = dict()   
    
    for nombre, nota in alumnos.items():
        if nota >= 7:
            aprobados[nombre] = nota
        elif 4 <= nota < 7:
            desaprobados[nombre] = nota
        elif 0 <= nota < 4:
            aplazados[nombre] = nota        
    return f"Los aprobados son: {aprobados} \n Los desaprobados son: {desaprobados} \n Los apazados son: {aplazados}"

print(boletin()) 