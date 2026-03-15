# from typing import
from octal import potencia8
from utils.bases import bases

def pasarAHexa(numero):
    hexa = ""
    letras = "0123456789ABCDEF"
    while numero > 0:
        hexa = letras[numero % 16] + hexa
        numero = numero // 16
    return(hexa)

def hexa(tipo: str, texto: str) -> str | None:
		numero = 0
		u = 0
		while u < len(texto):
			numero = numero * 10 + bases[texto[u]]
			u = u + 1 
		if tipo == "*":
			return "Binario"
		elif tipo == "&":
			nuevoNumero = potencia8(numero)
			print(nuevoNumero)
			numeroFinal = pasarAHexa(nuevoNumero)
			return numeroFinal
		elif tipo == "#":
			numeroFinal = potencia8(numero)
			return numeroFinal
		elif tipo == "!":
			return texto
		else:
			return None