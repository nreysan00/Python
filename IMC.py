# Solicitamos la edad

edad = int(input("Por favor, ingrese su edad: "))

# Verificamos la edad

'''
if edad < 18:
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")
'''

# Realizamos la calculadora

if edad >= 18:
    nombre = str(input("Introduzca tu nombre: "))
    confirmacion = str(input("Su nombre es correcto? S/N: "))
    confirmacion = confirmacion.upper()
    altura = float(input("Introduce tu altura en metros: "))
    peso = float(input("Introduce tu peso en kg: "))

    IMC = peso / (altura**2)

    print(nombre, "tu IMC es de: ", IMC)

    if IMC <= 15.99:
        print("Delgadez severa")
    elif 16.0 <= IMC <= 16.99:
        print("Delgadez moderada")
    elif 17.0 <= IMC <= 18.49:
        print("Delgadez leve")
    elif 18.50 <= IMC <= 24.99:
        print("Normal")
    elif 25.0 <= IMC <= 29.99:
        print("Sobrepeso")
    elif 30.0 <= IMC <= 34.99:
        print("Obesidad leve")
    elif 35.0 <= IMC <= 39.0:
        print("Obesidad")
    elif IMC >= 40:
        print("Obesidad morbida")
else:
    print("Usted es menor de edad")
