# from typing import
from utils.strings import partirString
from utils.bases import bases, hexABinario
from utils.bits import bits

def leerBinario(string: str) -> int:
	arreglo: list[str] = list(string)
	arreglo.reverse()

	suma = 0
	index = 0

	for i in arreglo:
		suma += 1 * (2**index) if i == "1" else 0
		index += 1

	return suma


def binario(tipo: str, texto: str, valor: int, mensaje: str) -> str | None:

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

# print(binario("!", "AF3"))
