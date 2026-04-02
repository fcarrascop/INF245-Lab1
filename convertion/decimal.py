from utils.bases import bases
from utils.strings import MetodoHorner

def decimal(tipo: str, texto: str) -> str:
    """
    Convierte un numero desde una base a decimal (base 10).

    Args:
    	tipo (str): Prefijo de base de entrada (*, &, #, !).
    	texto (str): Cadena numerica en la base indicada por el prefijo.

    Returns:
    	str:
    		Cadena con el numero convertido a decimal, o "" si el prefijo no es valido.

    Raises:
    	KeyError: Si hay un digito fuera de la base en el texto.

    Example:
    	>>> decimal("!", "1A")
    	"26"
    """

    if tipo == "#":
        return texto
    elif tipo == "*":
    	# Binario
    	# División repetida
        suma = 0

        for x in texto:
            suma = suma * 2 + bases[x]

        return str(suma)

    elif tipo == "&":
    	# Octal
    	# División repetida
        suma = 0
        lista = [ bases[x] for x in texto]
        for x in lista:
            suma = suma * 8 + x

        final = str(suma)

        return final

    elif tipo == "!":
    	# Hexadecimal
    	# División repetida

        return str(MetodoHorner(texto, 16))
    else:
    	return ""
