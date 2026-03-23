from utils.bits import bits
from utils.bases import bases
from utils.strings import partirString
from utils.strings import MetodoHorner

def octal(tipo: str, texto: str) -> str | None:
    if tipo == "&":
        return texto
    elif tipo == "*":
        # Binario
        # Agrupación de bits
        final = ""

        for c in texto:
            final += bits(3, c)

        return final
    elif tipo == "#":
        # Decimal
        # Variación Método de Horner

        """suma = 0
        lista = [ bases[x] for x in texto]
        for x in lista:
            suma = suma * 8 + x

        final = str(suma)"""
        final = MetodoHorner(texto, 8)
        print(final)

        return final
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