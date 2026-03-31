from utils.bases import basesHexa, binarioAHex
from utils.bits import numeroAbinario
from utils.strings import partirString, MetodoHorner
from utils.printValores import printValores

def pasarAHexa(numero: int) -> str:
    hexa = ""

    while numero > 0:
        hexa = basesHexa[numero % 16] + hexa
        numero = numero // 16

    return(hexa)

def hexaString(numero: int) -> str:
	if (numero == 0):
		return "0"

	texto = []
	while numero > 0:
		digito = numero % 10
		texto.append(basesHexa[digito])
		numero //= 10

	texto.reverse()
	final = "".join(texto)
	return final

def leerBinAHexa(binario: list) -> str:
	numFinal = ""
	for grupos in binario:
		numFinal += binarioAHex[grupos]

	return numFinal


def hexadecimal(tipo: str, texto: str, valor: int, mensaje: str):
		if tipo == "!":

			mensaje = mensaje + printValores(valor, tipo, texto, texto, 16)

			valor = valor + 1

			return valor, mensaje
		
		elif tipo == "*":
			# Binario

			numFinal = leerBinAHexa(partirString(texto, 4))

			mensaje = mensaje + printValores(valor, tipo, texto, numFinal.lstrip("0"), 16)

			valor = valor + 1

			return valor, mensaje

		elif tipo == "&":
			# Octal
			# Conversión de base pasando por decimal

			numeroNuevo = numeroAbinario(texto, 3)
			numFinal = leerBinAHexa(partirString(numeroNuevo, 4))

			mensaje = mensaje + printValores(valor, tipo, texto, numFinal.lstrip("0"), 16)

			valor = valor + 1

			return valor, mensaje

		elif tipo == "#":
			# Decimal
			# ~Expanción posicional~
			# Variación Método de Horner

			numFinal = pasarAHexa(int(texto))

			mensaje = mensaje + printValores(valor, tipo, texto, str(numFinal).lstrip("0"), 16)

			valor = valor + 1

			return valor, mensaje
		else:
			return ""

# Yo (felipe) estuve modificando algunas cosas por acá, por lo que si algo falla, toda la culpa a mi.

