from utils.bits import bits
from utils.bases import bases
from utils.strings import partirString
from utils.strings import MetodoHorner
from convertion.binario import leerBinario

def octal(tipo: str, texto: str) -> str | None:
    if tipo == "&":
        return texto
    elif tipo == "*":
        # Binario
        # Agrupación de bits
        lista = partirString(texto, 3)
        final = [ "01234567"[leerBinario(x)] for x in lista]
        caracter = "".join(final)

        return caracter
    
    elif tipo == "#":
        # Decimal
        # Variación Método de Horner
        numero = int(texto)
        final = ""

        while numero > 0:
            resto = numero % 8
            final += "01234567"[resto]
            numero //= 8

        return final[::-1]
    
    elif tipo == "!":
        return "Hexa"
    else:
        return None

def leerOctal(numero: int) -> int:
    resultado = 0
    potencia = 0

    while numero > 0:

        digito = numero % 10
        resultado = resultado + digito * (8 ** potencia)

        numero = numero // 10
        potencia = potencia + 1
    return resultado

octal("#", "176")