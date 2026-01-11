texto = input("Ingresa un número: ").strip()

try:
    numero = float(texto)
    print("El doble es:", numero * 2)
except ValueError:
    print("Error: no ingresaste un número válido.")
