# Calculadora con Input, Condicionales y Funciones

# Definimos la funcionalidades

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre 0"

#Mostramos las opciones de la calculadora

print("Bienvenido a la calculadora de python.")
print("Elija un número asociado a una operación para continuar: ")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Selección de operación

opcion = int(input("Elija una opción"))

# Selección de números

numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))

# Lógica

if opcion == 1:
    resultado = suma(numero1, numero2)
elif opcion == 2:
    resultado = resta(numero1, numero2)
elif opcion == 3:
    resultado = multiplicacion(numero1, numero2)
elif opcion == 4:
    resultado = division(numero1, numero2)
else:
    resultado = "Opción no válida"

#Mostramos el resultado

print("El resultado de su operación es: ", resultado)