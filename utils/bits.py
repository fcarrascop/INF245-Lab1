from utils.bases import bases

def bits(cantidadBits: int, numero: str) -> str:
	"""
	Convierte un digito a una cadena binaria con largo fijo.

	Args:
		cantidadBits (int): Cantidad de bits de salida.
		numero (str): Digito en base decimal u octal.

	Returns:
		str: Cadena binaria con padding a la izquierda.

	Raises:
		KeyError: Si el digito no existe en el diccionario bases.

	Example:
		>>> bits(3, "7")
		"111"
	"""
	final = ""
	numeroInt = bases[numero]
	for n in range(cantidadBits):
		resto = numeroInt % 2
		if resto == 1:
			final = final + "1"
		else:
			final = final + "0"
		numeroInt //= 2

	return final[::-1]

def numeroAbinario(numero: str, cantidadBits: int) -> str:
    """
    Convierte una cadena numerica a binario agrupando cada digito.

    Args:
    	numero (str): Cadena numerica en la base indicada por el largo.
    	cantidadBits (int): Bits por digito (3 para octal, 4 para hexa).

    Returns:
    	str: Cadena binaria concatenada.

    Raises:
    	KeyError: Si hay un digito no valido.

    Example:
    	>>> numeroAbinario("17", 3)
    	"001111"
    """
    resultado = ""

    for digito in numero:
        n = bases[digito]

        bits = ""
        for _ in range(cantidadBits):
            resto = n % 2
            bits += "1" if resto == 1 else "0"
            n //= 2

        resultado += bits[::-1]

    return resultado
