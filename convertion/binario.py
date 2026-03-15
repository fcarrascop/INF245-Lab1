# from typing import
from utils.strings import partirString

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
		final = map(leerBinario, lista)
		caracter = "".join(map(str, final))

		return caracter
	elif tipo == "#":
		return "Decimal"
	elif tipo == "!":
		return "Hexa"
	else:
		return None
