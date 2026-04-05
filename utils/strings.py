from utils.bases import bases
from utils.ascii import ascii

def partirString(string: str, cantidad: int = 3) -> list[str]:
	"""
	Parte una cadena en grupos de largo fijo, rellenando con ceros al inicio.

	Args:
		string (str): Cadena numerica a partir.
		cantidad (int): Largo de cada grupo.

	Returns:
		list[str]: Lista de grupos con el largo solicitado.

	Example:
		>>> partirString("101", 4)
		["0101"]
	"""
	if len(string) % cantidad != 0:
		faltan = cantidad - (len(string) % cantidad)
		string = "0" * faltan + string
	return [string[i:i+cantidad] for i in range(0, len(string), cantidad)]

def numeroAAscii(numero: str, base: int) -> str:
	"""
	Convierte un numero en cierta base a su caracter ASCII si es imprimible.

	Args:
		numero (str): Cadena numerica en la base indicada.
		base (int): Base del numero.

	Returns:
		str:
			Caracter ASCII imprimible, o cadena vacia si esta fuera de rango.

	Example:
		>>> numeroAAscii("65", 10)
		"A"
	"""
	valor = MetodoHorner(numero, base)

	if valor <= 126 and 32 <= valor:
		letraMensaje = chr(valor)
		return letraMensaje

	return ""

def MetodoHorner(numero: str, base: int) -> int:
	"""
	Convierte una cadena numerica a decimal con el metodo de Horner.

	Args:
		numero (str): Cadena numerica en la base indicada.
		base (int): Base del numero.

	Returns:
		int: Valor decimal equivalente.

	Raises:
		KeyError: Si hay un digito no valido para la base.

	Example:
		>>> MetodoHorner("1A", 16)
		26
	"""
	numero.upper()

	valor = 0

	for digito in numero:

		if '0' <= digito <= '9':
			n = ord(digito) - ord('0')
		else:
			n = ord(digito) - ord('A') + 10

		valor = valor * base + n
		
	return valor
