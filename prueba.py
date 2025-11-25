#!/usr/bin/env python3
# prueba.py - Calculadora básica en terminal (ES)

def obtener_numero(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Entrada inválida. Introduce un número.")

def mostrar_resultado(res):
    # Muestra como entero si no hay decimales
    if isinstance(res, float) and res.is_integer():
        print("Resultado:", int(res))
    else:
        print("Resultado:", res)

def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero")
    return a / b
def potencia(a, b): return a ** b
def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("Módulo por cero")
    return a % b

def menu():
    print("\nCalculadora básica")
    print("1) Suma (+)")
    print("2) Resta (-)")
    print("3) Multiplicación (*)")
    print("4) División (/)")
    print("5) Potencia (a^b)")
    print("6) Módulo (%)")
    print("0) Salir")

def main():
    while True:
        menu()
        opcion = input("Elige una opción [0-6]: ").strip()

        if opcion == '0' or opcion.lower() in ('salir', 'q', 'quit'):
            print("Saliendo...")
            break

        if opcion not in ('1','2','3','4','5','6'):
            print("Opción inválida.")
            continue

        a = obtener_numero("Introduce el primer número: ")
        b = obtener_numero("Introduce el segundo número: ")

        try:
            if opcion == '1':
                mostrar_resultado(suma(a, b))
            elif opcion == '2':
                mostrar_resultado(resta(a, b))
            elif opcion == '3':
                mostrar_resultado(multiplicar(a, b))
            elif opcion == '4':
                mostrar_resultado(dividir(a, b))
            elif opcion == '5':
                mostrar_resultado(potencia(a, b))
            elif opcion == '6':
                mostrar_resultado(modulo(a, b))
        except ZeroDivisionError as e:
            print("Error:", e)

        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()