
def normalize_name(txt):
	"""
	Esta funcion normaliza strings.
	lo que hace es quitar espacios en blanco al inicio y fin de mi string, 
	elimina espacios en blanco.

	Ej. 
	cArLos     AnTOniO  ->  Carlos Antonio
	
	:params (str): texto de entrada
	:return: texto formateado
	"""

	return " ".join(txt.strip().title().split())

def to_mxn(valor, tasa: float=1.0): #tasa -> optional param
	"""
	Convierte un valor numerico a MXN multiplicando por la tasa
	"""
	return float(valor)*float(tasa)

