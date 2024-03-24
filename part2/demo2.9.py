"""Ejercicio 9: Pedirle al usuario que ingrese el monto disponible en su tarjeta de crédito.
 Evaluar si puede realizar una compra de $2500,
si puede indicar cuánto saldo le queda luego de efectuarla.
Si no puede, indicar cuánto dinero le falta para poder realizarla."""

saldo = int(input("Ingresar saldo: "))

if saldo < 2500:
    print(f"No tienes dinero suficiente, te faltan {2500 - saldo}")
elif saldo > 2500:
    print(f"Puedes hacer esta compra, tu salto quedaria en: {saldo-2500}")    