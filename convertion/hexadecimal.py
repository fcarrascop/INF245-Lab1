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
	print(binario)
	for grupos in binario:
		numFinal += binarioAHex[grupos]

	return numFinal

def dividir_octal_por_20(numero_octal):
    cociente = ""
    resto = 0

    for digito in numero_octal:
        # convertir carácter a número (sin usar int)
        valor = int(digito)

        # acumulación en base 8 (simula la división larga)
        acumulado = resto * 8 + valor

        # dividir entre 20₈ (equivale a 16)
        digito_cociente = acumulado // 16
        resto = acumulado % 16

        # evitar ceros a la izquierda
        if cociente != "" or digito_cociente != 0:
            cociente += chr(digito_cociente + ord('0'))

    if cociente == "":
        cociente = "0"

    return cociente, resto


def octal_a_hex(octal):
    resultado = ""

    while octal != "0":
        cociente, resto = dividir_octal_por_20(octal)

        # agregar el dígito hexadecimal correspondiente
        resultado = basesHexa[resto] + resultado

        # continuar con el cociente
        octal = cociente

    return resultado



def hexadecimal(tipo: str, texto: str, valor: int = 0, mensaje: str = "") -> str | None:

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

			# printValores(valor, mensaje, tipo, texto, numFinal, 16)

			return numFinal

		elif tipo == "#":
			# Decimal
			# ~Expanción posicional~
			# Variación Método de Horner

			numFinal = pasarAHexa(int(texto))

			printValores(valor, mensaje, tipo, texto, str(numFinal), 16)

			return None
		else:
			return ""

# Yo (felipe) estuve modificando algunas cosas por acá, por lo que si algo falla, toda la culpa a mi.
