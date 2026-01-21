print("Este programa captura importes")
info = """ 
	CALCULA TU SUMA
	
	Este programa lleva el conteo de cuantos importes ha
	introducido un usuario.

	Va acumulando todos los importes que el usuario ingresa.

	Si el usuario desea terminar el programa puede escribir
		cualquier momento la palabra exit, quit, terminar.

			Elaborado por Daniel Ruiz.

"""

print(info)
conteo = 0
suma = 0.0
minimo = None
maximo = None

while True:
	user_message = """

		Ingresa tu importe (MXN)
		Si quieres dejar de capturar importes
		puedes ingresar en cualquier momento
			exit, quit, terminar.
 		"""
	line = input("Ingresa tu importe (MXN)")
	if line  == "exit" or  line == "quit"  or line == "terminar":
	    	break
	try:
		value = float(line)
	except ValueError:
		print("Valor invalido. Intenta de nuevo (ej. 125.5)")
		continue
	conteo += 1
	suma += value

	if minimo is None or value < minimo:
		minimo = value

	if maximo is None or value > maximo:
		maximo = value

if conteo == 0:
	print("No se capturaron importes")
else: 
	print("=" *32)
	print(f"La cantidad de numeros ingresados es: {conteo}")
	print(f"La sumatoria total de los numeros ingresados es: {suma}")
	print(f"El valor maximo es: {maximo}")
	print(f"El valor minimo es: {minimo}")	
	print("programa finalizado") 


