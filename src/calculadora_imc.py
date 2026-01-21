weight_txt = input("Peso (kg): ")
height_txt = input("Altura (m): ")

try:
    weight = float(weight_txt)
    height = float(height_txt)
    imc = weight/height**2
    print(f"Tu IMC es de: {imc}")
except (ValueError, ZeroDivisionError):
    print("Datos invalidos. Ej.: peso 70.5, altura 1.75")
except ZeroDivisionError:
    print("Error. No esta permitida la division por cero")
except Exception as err:
    print(err)
#print(f"")
