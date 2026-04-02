from utils.strings import numeroAAscii, MetodoHorner

valores = {
	"*": "Binario",
	"&": "Octal",
	"#": "Decimal",
	"!": "Hexadecimal",
}

def printValores(index: int, signo: str, inicial: str, final: str, base: int) -> str:
	"""
	Imprime el valor convertido y devuelve el caracter ASCII si es valido.

	Args:
		index (int): Indice del valor mostrado.
		signo (str): Prefijo de la base original.
		inicial (str): Numero original como texto.
		final (str): Numero convertido a la base solicitada.
		base (int): Base solicitada para la salida.

	Returns:
		str:
			Caracter ASCII si el valor esta en rango, si no cadena vacia.

	Example:
		>>> printValores(1, "#", "84", "54", 16)
		"T"
	"""

	if MetodoHorner(final, base) <= 126 and 32 <= MetodoHorner(final, base):
		print("Valor " + str(index) + ": " + final + " (Original: " + valores[signo] + " " + signo + inicial+ ")")

		nuevo = numeroAAscii(final, base)

		return nuevo

	return ""
