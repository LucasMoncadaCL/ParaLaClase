#!/usr/bin/env python3
# prueba.py - Calculadora avanzada en terminal (ES)

import math

def obtener_numero(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Entrada inválida. Introduce un número.")

def mostrar_resultado(res):
    if isinstance(res, float) and res.is_integer():
        print("Resultado:", int(res))
    else:
        print("Resultado:", res)

# Operaciones básicas
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

# Operaciones avanzadas
def raiz_cuadrada(a):
    if a < 0:
        raise ValueError("No se puede sacar raíz cuadrada de un número negativo.")
    return math.sqrt(a)

def raiz_n_esima(a, n):
    if n == 0:
        raise ZeroDivisionError("La raíz de índice 0 no existe.")
    return a ** (1.0 / n)

def log_base10(a):
    if a <= 0:
        raise ValueError("El logaritmo solo acepta valores positivos.")
    return math.log10(a)

def log_natural(a):
    if a <= 0:
        raise ValueError("El logaritmo solo acepta valores positivos.")
    return math.log(a)

def trig_sin(a): return math.sin(math.radians(a))
def trig_cos(a): return math.cos(math.radians(a))
def trig_tan(a): return math.tan(math.radians(a))

def factorial(a):
    if a < 0 or not float(a).is_integer():
        raise ValueError("El factorial solo acepta enteros positivos.")
    return math.factorial(int(a))

def porcentaje(a, b):
    return (a * b) / 100

def redondear(a): return round(a)
def absoluto(a): return abs(a)

def grados_a_radianes(a): return math.radians(a)
def radianes_a_grados(a): return math.degrees(a)

# Modo científico evaluando expresiones
def modo_cientifico():
    print("\n🔬 Modo científico (escribe una expresión, ejemplo: 3*(2+5)/4 )")
    print("Escribe 'salir' para volver.\n")

    while True:
        expr = input(">>> ").strip()
        if expr.lower() in ("salir", "exit", "q"):
            break
        try:
            res = eval(expr, {"__builtins__": None}, math.__dict__)
            mostrar_resultado(res)
        except:
            print("Expresión inválida o no permitida.")

def menu():
    print("\n============================")
    print("     CALCULADORA AVANZADA   ")
    print("============================")
    print("1) Suma (+)")
    print("2) Resta (-)")
    print("3) Multiplicación (*)")
    print("4) División (/)")
    print("5) Potencia (a^b)")
    print("6) Módulo (%)")
    print("7) Raíz cuadrada")
    print("8) Raíz n-ésima")
    print("9) Logaritmo base 10")
    print("10) Logaritmo natural")
    print("11) Seno (grados)")
    print("12) Coseno (grados)")
    print("13) Tangente (grados)")
    print("14) Factorial")
    print("15) Porcentaje (a es b%)")
    print("16) Redondear")
    print("17) Valor absoluto")
    print("18) Grados → Radianes")
    print("19) Radianes → Grados")
    print("20) Modo científico (eval)")
    print("0) Salir")

def main():
    while True:
        menu()
        opcion = input("Elige una opción [0-20]: ").strip()

        if opcion == '0':
            print("Saliendo...")
            break

        try:
            if opcion in ('1','2','3','4','5','6'):
                a = obtener_numero("Introduce el primer número: ")
                b = obtener_numero("Introduce el segundo número: ")

                if opcion == '1': mostrar_resultado(suma(a, b))
                elif opcion == '2': mostrar_resultado(resta(a, b))
                elif opcion == '3': mostrar_resultado(multiplicar(a, b))
                elif opcion == '4': mostrar_resultado(dividir(a, b))
                elif opcion == '5': mostrar_resultado(potencia(a, b))
                elif opcion == '6': mostrar_resultado(modulo(a, b))

            elif opcion == '7':
                a = obtener_numero("Número: ")
                mostrar_resultado(raiz_cuadrada(a))

            elif opcion == '8':
                a = obtener_numero("Número: ")
                n = obtener_numero("Índice de la raíz: ")
                mostrar_resultado(raiz_n_esima(a, n))

            elif opcion == '9':
                a = obtener_numero("Número: ")
                mostrar_resultado(log_base10(a))

            elif opcion == '10':
                a = obtener_numero("Número: ")
                mostrar_resultado(log_natural(a))

            elif opcion == '11':
                a = obtener_numero("Ángulo en grados: ")
                mostrar_resultado(trig_sin(a))

            elif opcion == '12':
                a = obtener_numero("Ángulo en grados: ")
                mostrar_resultado(trig_cos(a))

            elif opcion == '13':
                a = obtener_numero("Ángulo en grados: ")
                mostrar_resultado(trig_tan(a))

            elif opcion == '14':
                a = obtener_numero("Número entero: ")
                mostrar_resultado(factorial(a))

            elif opcion == '15':
                a = obtener_numero("Cantidad: ")
                b = obtener_numero("Porcentaje (%): ")
                mostrar_resultado(porcentaje(a, b))

            elif opcion == '16':
                a = obtener_numero("Número: ")
                mostrar_resultado(redondear(a))

            elif opcion == '17':
                a = obtener_numero("Número: ")
                mostrar_resultado(absoluto(a))

            elif opcion == '18':
                a = obtener_numero("Grados: ")
                mostrar_resultado(grados_a_radianes(a))

            elif opcion == '19':
                a = obtener_numero("Radianes: ")
                mostrar_resultado(radianes_a_grados(a))

            elif opcion == '20':
                modo_cientifico()
                continue

            else:
                print("Opción inválida.")
                continue

        except Exception as e:
            print("Error:", e)

        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
