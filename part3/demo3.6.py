"""Ejercicio 6: Crear una función que devuelva por pantalla un mensaje ingresado por parámetro pero en modo Title.
Si el mensaje ya está en modo title, que devuelva por pantalla "El mensaje ya está en modo title: {mensaje}"""

def message_title(message):
    if message.istitle():
        return f"El mensaje ya esta en modo title: {message}"
    else:
        return message.title()
      

print(message_title("probando python"))    