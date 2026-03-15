# from typing import
from octal import leerOctal
from utils.bases import bases
from utils.strings import decimalString

def pasarAHexa(numero: int) -> str:
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
			# Binario
			return "Binario"
		elif tipo == "&":
			# Octal
			# Conversión de base pasando por decimal

			nuevoNumero = leerOctal(numero)
			numeroFinal = pasarAHexa(nuevoNumero)

			return numeroFinal
		elif tipo == "#":
			# Decimal
			# Expanción posicional

			numeroFinal = leerOctal(numero)
			final = decimalString(numeroFinal)

			return final
		else:
			return None

# Yo (felipe) estuve modificando algunas cosas por acá, por lo que si algo falla, toda la culpa a mi.
