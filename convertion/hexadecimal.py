from convertion.octal import leerOctal
from utils.bases import bases, basesHexa, binarioAHex
from utils.bits import bits, bitsHexa, numeroAbinario
from utils.strings import partirString, MetodoHorner
from utils.printValores import printValores

def pasarAHexa(numero: int) -> str:
    hexa = ""
    letras = "0123456789ABCDEF"

    while numero > 0:
        hexa = letras[numero % 16] + hexa
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
	print(binario)
	for grupos in binario:
		numFinal += binarioAHex[grupos]

	return numFinal
	


def hexadecimal(tipo: str, texto: str, valor: int, mensaje: str) -> str | None:

		if tipo == "!":
			return texto
		elif tipo == "*":
			# Binario

			numFinal = leerBinAHexa(partirString(texto, 4))
			
			printValores(valor, mensaje, tipo, texto, numFinal, 16)

			return None

		elif tipo == "&":
			# Octal
			# Conversión de base pasando por decimal

			numeroNuevo = numeroAbinario(texto, 3)
			
			numFinal = leerBinAHexa(partirString(numeroNuevo, 4))

			printValores(valor, mensaje, tipo, texto, numFinal, 16)

			return None

		elif tipo == "#":
			# Decimal
			# ~Expanción posicional~
			# Variación Método de Horner

			numFinal = pasarAHexa(int(texto))

			printValores(valor, mensaje, tipo, texto, str(numFinal), 16)

			return None
		else:
			return ""

hexadecimal("#", "111", 1, "")
#print(numeroAbinario("145", 3))

# Yo (felipe) estuve modificando algunas cosas por acá, por lo que si algo falla, toda la culpa a mi.
