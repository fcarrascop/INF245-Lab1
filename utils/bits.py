from utils.bases import bases

def bits(cantidadBits: int, numero: str) -> str:
	final = ""
	numeroInt = bases[numero]
	for n in range(cantidadBits):
		resto = numeroInt % 2
		final += "1" if resto == 1 else "0"
		numeroInt //= 2

	return final[::-1]


def bitsHexa(numero: str) -> str:
	final = ""
	numeroInt = int(numero)
    
	while numeroInt > 0:
		resto = numeroInt % 2
		final += "1" if resto == 1 else "0"
		numeroInt //= 2

	return final[::-1]
