name = "hello world"
print(name)

#Built-in method input(argument)
user_name = input("Como te llamas")
edad_txt = input("Cual es tu edad")

#Built-in method type(1 argument) - Nos dice el tipo de variable
print(user_name)
print(type(user_name))

print(edad_txt)
print(type(edad_txt))

#Built-in int(1-argument) - Convierte un string a un numero 
try:
	edad = int(edad_txt)
	print(edad)
	print(type(edad))
except ValueError:
	print("Error: la conversión no se pudo realizar")
	print("Debes ingresar un numero entero")
