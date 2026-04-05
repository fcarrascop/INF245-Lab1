from utils.bases import basesHexa, binarioAHex
from utils.bits import numeroAbinario
from utils.strings import partirString, MetodoHorner

def pasarAHexa(numero: int) -> str:
    """
    Convierte un numero decimal a hexadecimal.

    Args:
    	numero (int): Valor decimal.

    Returns:
    	str:
    		Cadena hexadecimal equivalente.

    Example:
    	>>> pasarAHexa(26)
    	"1A"
    """
    if numero == 0:
        return "0"

    resultado = ""

    while numero > 0:
        resto = numero % 16

        if resto < 10:
            resultado = chr(resto + ord('0')) + resultado
        else:
            resultado = chr(resto - 10 + ord('A')) + resultado

        numero //= 16

    return resultado

def leerBinAHexa(binario: list) -> str:
	"""
	Convierte una lista de grupos binarios a hexadecimal.

	Args:
		binario (list): Lista de strings con grupos de 4 bits.

	Returns:
		str:
			Cadena hexadecimal equivalente.

	Raises:
		KeyError: Si algun grupo no existe en el mapeo.

	Example:
		>>> leerBinAHexa(["0001", "1010"])
		"1A"
	"""
	numFinal = ""

	for grupo in binario:
        
		valor = MetodoHorner(grupo, 2)

		if valor < 10:
			numFinal += chr(valor + ord('0'))
		else:
			numFinal += chr(valor - 10 + ord('A'))

	return numFinal


def hexadecimal(tipo: str, texto: str) -> str:
    """
    Convierte un numero desde una base a hexadecimal.

    Args:
    	tipo (str): Prefijo de base de entrada (*, &, #, !).
    	texto (str): Cadena numerica en la base indicada por el prefijo.

    Returns:
    	str:
    		Cadena con el numero convertido a hexadecimal.

    Raises:
    	KeyError: Si hay un digito no valido en el texto.
    	ValueError: Si el texto no es numerico cuando tipo es #.

    Example:
    	>>> hexadecimal("#", "26")
    	"1A"
    """
    if tipo == "!":
        return texto

    elif tipo == "*":
    	# Binario
        numFinal = leerBinAHexa(partirString(texto, 4))

        return numFinal

    elif tipo == "&":
    	# Octal
    	# Conversión de base pasando por decimal

        numeroNuevo = numeroAbinario(texto, 3)
        numFinal = leerBinAHexa(partirString(numeroNuevo, 4))

        return numFinal

    elif tipo == "#":
    	# Decimal
    	# ~Expanción posicional~
    	# Variación Método de Horner

        numFinal = pasarAHexa(int(texto))

        return numFinal
    else:
    	return ""

# Yo (felipe) estuve modificando algunas cosas por acá, por lo que si algo falla, toda la culpa a mi.
