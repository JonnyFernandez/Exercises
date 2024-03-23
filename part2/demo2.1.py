"""Ejercicio 1: Pedir al usuario que ingrese un mensaje cualquiera, si el mensaje tiene
más de 100 caracteres imprimirlo por pantalla, si tiene entre 50 y 100 caracteres imprimirlo al revés,
si no se cumple ninguna de las opciones anteriores,
por pantalla devolver un mensaje que diga "su mensaje es demasiado corto"."""

info = input("Escribe tu texto: ")


if len(info) >= 100 :
    print(f"tu mensaje es: \n {info}")
elif 50 < len(info) < 100:
        print(f"resultado \n {info[::-1]}" )
elif len(info) < 50:
    print("Mensaje muy corto")
else:
    print("esbribe algo")
print(len(info))        