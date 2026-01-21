"""
   Este programa va a pedir al usuario un pin de acceso.
   pin correcto = autenticacion
   pin incorrecto = advertencia y conteo de intentos (3)
   intentos > 3 .: bloqueo y advertencia

"""

PIN_R = "1234"
ATTEMPTS = 3
atts = 0

while atts < ATTEMPTS:
	entry = input("Ingresa tu pin de 4 digitos")
	if entry == PIN_R:
		print("Acceso concedido  ")
		print("")
		break
	else:
		atts += 1
		atts_left = ATTEMPTS - atts
		if atts_left > 0:
			print(f"Pin Incorrecto, te quedan {atts_left} restantes")
		else:
			print("BLOQUEADO")		
 
