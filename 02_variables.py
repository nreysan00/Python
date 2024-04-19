# Variables

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 34
print(my_int_variable)

my_bool_variable = False
print(type(my_bool_variable))

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenación de variables

print(my_string_variable, my_int_variable, my_bool_variable)
print("Mi edad es:",my_int_variable, "años")

#Vamos a ver la funcion len

print(len(my_string_variable))
print(len(my_int_to_str_variable))

# Variables de una linea

name, surname, age = ("Juan", "Ortega", 65)
print(name, surname, age)
print("Me llamo", name, surname, "y tengo", age, "años")

name1, email, password = ("Ana", "jimenez@gmail.com", "1234567")
print("Hola", name1, "tu email", email, "y tu contraseña", password, "son correctos?")

# Inputs

name2 = input("¿Cual es tu nombre?")
age2 = input("¿Que edad tienes?")


# IMC = peso (kg)/ [estatura*estatura]

