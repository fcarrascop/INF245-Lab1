# from typing import
from utils.strings import partirString
from utils.bases import bases

def leerBinario(string: str) -> int:
	arreglo: list[str] = list(string)
	arreglo.reverse()

	suma = 0
	index = 0

	for i in arreglo:
		suma += 1 * (2**index) if i == "1" else 0
		index += 1

	return suma


def binario(tipo: str, texto: str) -> str | None:
	if tipo == "&":
		# Octal
		# 3 bit grouping

		lista = partirString(texto, 3)
		final = [ "01234567"[leerBinario(x)] for x in lista]
		caracter = "".join(final)

		return caracter
	elif tipo == "#":
		# Decimal
		# Método de Horner

		suma = 0
		lista = [ bases[x] for x in texto]
		lista.reverse()
		for x in lista:
			suma = suma * 2 + x

		final = str(suma)

		return final
	elif tipo == "!":
		# Hexadecimal
		# 4 bit grouping

		lista = partirString(texto, 4)
		final = [ "0123456789ABCDEF"[leerBinario(x)] for x in lista]
		caracter = "".join(final)

		return caracter
	else:
		return None
