from utils.bits import bits, numeroAbinario
from utils.bases import bases, binarioAOctal
from utils.strings import partirString
from utils.strings import MetodoHorner
from convertion.binario import leerBinario, binario
from utils.printValores import printValores

def leerBinAOctal(binario: list) -> str:
	numFinal = ""
	for grupos in binario:
		numFinal += binarioAOctal[grupos]

	return numFinal

def leerOctal(numero: int) -> int:
    resultado = 0
    potencia = 0

    while numero > 0:

        digito = numero % 10
        resultado = resultado + digito * (8 ** potencia)

        numero = numero // 10
        potencia = potencia + 1
    return resultado

def octal(tipo: str, texto: str, valor: int, mensaje: str) -> str | None:
    if tipo == "&":

        mensaje = mensaje + printValores(valor, tipo, texto, texto, 8)

        valor = valor + 1

        return valor, mensaje

    elif tipo == "*":
        # Binario
        # Agrupación de bits

        lista = partirString(texto, 3)
        final = [ "01234567"[leerBinario(x)] for x in lista]
        caracter = "".join(final)

        mensaje = mensaje + printValores(valor, tipo, texto, caracter.lstrip("0"), 8)

        valor = valor + 1

        return valor, mensaje

    elif tipo == "#":
        # Decimal
        # Variación Método de Horner

        numero = int(texto)
        final = ""

        while numero > 0:
            resto = numero % 8
            final += "01234567"[resto]
            numero //= 8

        mensaje = mensaje + printValores(valor, tipo, texto, final[::-1].lstrip("0"), 8)

        valor = valor + 1

        return valor, mensaje

    elif tipo == "!":

        numeroNuevo = numeroAbinario(texto, 4)
        numFinal = leerBinAOctal(partirString(numeroNuevo, 3))

        mensaje = mensaje + printValores(valor, tipo, texto, numFinal.lstrip("0"), 8)

        valor = valor + 1

        return valor, mensaje
    else:
        return None
