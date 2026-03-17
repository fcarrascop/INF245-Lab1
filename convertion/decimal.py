from utils.strings import stringANumero

def decimal(tipo: str, texto: str) -> str | None:
	if tipo == "*":
		# Binario
		# División repetida
		numero = stringANumero(texto)
		final = ""

		while numero > 0:
			resto = numero % 2
			final += "01"[resto]
			numero //= 2

		return final[::-1]
	elif tipo == "&":
		# Octal
		# División repetida
		numero = stringANumero(texto)
		final = ""

		while numero > 0:
			resto = numero % 8
			final += "01234567"[resto]
			numero //= 8

		return final[::-1]
	elif tipo == "!":
		# Hexadecimal
		# División repetida

		numero = stringANumero(texto)
		final = ""

		while numero > 0:
			resto = numero % 16
			final += "0123456789ABCDEF"[resto]
			numero //= 16

		return final[::-1]
	else:
		return None

print(decimal("!", "255"))
