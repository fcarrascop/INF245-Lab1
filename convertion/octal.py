# from typing import

def octal(tipo: str, texto: str) -> str | None:
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
	
def potencia8(numero):
    resultado = 0
    potencia = 0

    while numero > 0:

        digito = numero % 10
        resultado = resultado + digito * (8 ** potencia)

        numero = numero // 10
        potencia = potencia + 1
    return(resultado)
