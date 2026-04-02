# from typing import
from utils.bases import hexABinario
from utils.bits import bits

def leerBinario(string: str) -> int:
	"""
	Convierte un numero en base 2 a decimal.

	Args:
		string (str): Cadena con digitos binarios (0 y 1).

	Returns:
		int:
			Valor decimal equivalente.

	Raises:
		ValueError: Si la cadena contiene caracteres no binarios.

	Example:
		>>> leerBinario("1010")
		10
	"""
	arreglo: list[str] = list(string)
	arreglo.reverse()

	suma = 0
	index = 0

	for i in arreglo:
		suma += 1 * (2**index) if i == "1" else 0
		index += 1

	return suma


def binario(tipo: str, texto: str) -> str:
    """
    Convierte un numero desde una base a binario.

    Args:
    	tipo (str): Prefijo de base de entrada (*, &, #, !).
    	texto (str): Cadena numerica en la base indicada por el prefijo.

    Returns:
    	str:
    		Cadena con el numero convertido a binario.

    Raises:
    	KeyError: Si hay un digito hexadecimal no valido.
    	ValueError: Si el texto no es numerico cuando tipo es #.

    Example:
    	>>> binario("#", "10")
    	"1010"
    """

    if tipo == "*":
        return texto

    elif tipo == "&":
		# Octal
		# 3 bit grouping

        final = ""

        for c in texto:
            final += bits(3, c)

        return final

    elif tipo == "#":
    	# Decimal
    	# Método de Horner
        numero = int(texto)
        final = ""

        while numero > 0:
            resto = numero % 2
            final += "01"[resto]
            numero //= 2

        return final[::-1]

    elif tipo == "!":
        # Hexadecimal
        # 4 bit grouping
        resultado = ""

        textoHex = texto.upper()

        for digito in textoHex:
            resultado += hexABinario[digito]

        return resultado
    else:
        return ""
