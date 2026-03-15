# from typing import

def decimal(tipo: str, texto: str) -> str | None
	if tipo == "*":
		return "Binario"
	elif tipo == "&":
		return "Octal"
	elif tipo == "!":
		return "Hexa"
	else:
		return None
