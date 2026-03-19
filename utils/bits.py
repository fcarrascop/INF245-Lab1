from utils.bases import bases, bases, basesHexa

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


def numeroAbinario(numero: str, cantidadBits: int) -> str:
    resultado = ""

    for digito in numero:
        n = bases[digito] 

        bits = ""
        for _ in range(cantidadBits):
            resto = n % 2
            bits += "1" if resto == 1 else "0"
            n //= 2

        resultado += bits[::-1]

    return resultado