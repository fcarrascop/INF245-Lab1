from utils.bits import numeroAbinario
from utils.bases import binarioAOctal
from utils.strings import partirString
from convertion.binario import leerBinario
from utils.strings import MetodoHorner

def leerBinAOctal(binario: list) -> str:
    """
    Convierte una lista de grupos binarios a octal.

    Args:
    	binario (list): Lista de strings con grupos de 3 bits.

    Returns:
    	str:
    		Cadena octal equivalente.

    Raises:
    	KeyError: Si algun grupo no existe en el mapeo.

    Example:
    	>>> leerBinAOctal(["000", "111"])
    	"07"
    """

    numFinal = ""

    for grupo in binario:
        valor = MetodoHorner(grupo, 2)
        numFinal += chr(valor + ord('0'))

    return numFinal

def pasarAOctal(numero: int) -> int:
    """
    Convierte un numero en base 8 a decimal.

    Args:
    	numero (int): Numero en base 8.

    Returns:
    	int:
    		Valor decimal equivalente.

    Raises:
    	ValueError: Si el numero contiene digitos no octales.

    Example:
    	>>> leerOctal(17)
    	15
    """
    if numero == 0:
        return "0"

    resultado = ""

    while numero > 0:
        resto = numero % 8
        resultado = chr(resto + ord('0')) + resultado
        numero //= 8

    return resultado

def octal(tipo: str, texto: str) -> str:
    """
    Convierte un numero desde una base a octal.

    Args:
    	tipo (str): Prefijo de base de entrada (*, &, #, !).
    	texto (str): Cadena numerica en la base indicada por el prefijo.

    Returns:
    	str:
    		Cadena con el numero convertido a octal.

    Raises:
    	KeyError: Si hay un digito no valido en el texto.
    	ValueError: Si el texto no es numerico cuando tipo es #.

    Example:
    	>>> octal("#", "10")
    	"12"
    """

    if tipo == "&":
        return texto
    elif tipo == "*":
        # Binario
        # Agrupación de bits

        numFinal = leerBinAOctal(partirString(texto, 3))

        return numFinal
    
    elif tipo == "#":
        # Decimal
        # Variación Método de Horner

        numFinal = pasarAOctal(int(texto))

        return numFinal

    elif tipo == "!":

        numeroNuevo = numeroAbinario(texto, 4)
        numFinal = leerBinAOctal(partirString(numeroNuevo, 3))

        return numFinal
    else:
        return ""
