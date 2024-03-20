"""Ejercicio 12: Crear un programa que almacene los vectores (1,2,3) y (-1,0,2)
en dos listas y muestre por pantalla su producto escalar."""

vector1= [1,2,3]
vector2=[-1,0,2]
listaescalar=[]

for x in range(len(vector1)):
    listaescalar.append(vector1[x]*vector2[x])
print(listaescalar)    