from utils.bases import basesHexa, binarioAHex
from utils.bits import numeroAbinario
from utils.strings import partirString

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
    hexa = ""

    while numero > 0:
        hexa = basesHexa[numero % 16] + hexa
        numero = numero // 16

    return(hexa)

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
	for grupos in binario:
		numFinal += binarioAHex[grupos]

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
        # Agrupación de bits de 3 en 3

        numFinal = leerBinAHexa(partirString(texto, 4))

        return numFinal

    elif tipo == "&":
    	# Octal
    	# Agrupación de bits pasando por binario

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
