# from typing import
from utils.strings import partirString
from utils.bases import bases, hexABinario
from utils.bits import bits
from utils.printValores import printValores

def leerBinario(string: str) -> int:
	arreglo: list[str] = list(string)
	arreglo.reverse()

	suma = 0
	index = 0

	for i in arreglo:
		suma += 1 * (2**index) if i == "1" else 0
		index += 1

	return suma


def binario(tipo: str, texto: str, valor: int, mensaje: str) -> str | None:

    if tipo == "*":

        mensaje = mensaje + printValores(valor, tipo, texto, texto, 2)
			
        valor = valor + 1

        return valor, mensaje
    
    elif tipo == "&":
		# Octal
		# 3 bit grouping

        final = ""

        for c in texto:
            final += bits(3, c)
        
        mensaje = mensaje + printValores(valor, tipo, texto, final, 2)

        valor = valor + 1

        return valor, mensaje
    
    elif tipo == "#":
    	# Decimal
    	# Método de Horner
        numero = int(texto)
        final = ""

        while numero > 0:
            resto = numero % 2
            final += "01"[resto]
            numero //= 2

        mensaje = mensaje + printValores(valor, tipo, texto, final[::-1], 2)

        valor = valor + 1

        return valor, mensaje

    elif tipo == "!":
        # Hexadecimal
        # 4 bit grouping
        resultado = ""

        textoHex = texto.upper()

        for digito in textoHex:
            resultado += hexABinario[digito]

        mensaje = mensaje + printValores(valor, tipo, texto, resultado, 2)

        valor = valor + 1

        return valor, mensaje


