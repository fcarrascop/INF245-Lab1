# from typing import

def hexa(tipo: str, texto: str) -> str | None:
	if tipo == "*":
		return "Binario"
	elif tipo == "&":
		return "Octal"
	elif tipo == "#":
		return "Decimal"
	elif tipo == "!":
		return "Hexa"
	else:
		return None
