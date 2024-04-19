# IMC = peso (kg)/ [estatura*estatura]

nombre = input("Introduce tu nombre: ")
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura: "))

print(nombre ,"tu IMC es de:", round((peso/(altura*altura)),2))