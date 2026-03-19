from convertion.octal import leerOctal
from utils.bases import bases, basesHexa
from utils.bits import bits, bitsHexa
from utils.strings import partirString

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


def hexadecimal(tipo: str, texto: str, valor: int, mensaje: str) -> str | None:

		if tipo == "*":
			# Binario

			final = ""

			for c in texto:
				final += bits(4, c)

			return final

		elif tipo == "&":
			# Octal
			# Conversión de base pasando por decimal

			

			"""nuevoNumero = leerOctal(numero)
			numeroFinal = pasarAHexa(nuevoNumero)

			print("Valor "+ numeroAString(valor) + ": "+ numeroFinal + " (Original: Octal &"+ numeroAString(numero)+ ")")
			valor += 1

			# todo: eliminar esto
			if nuevoNumero <= 126 and 32 <= nuevoNumero:
				mensaje = mensaje + numeroAAscii(nuevoNumero)
				print(mensaje)
			return numeroFinal"""

		elif tipo == "#":
			# Decimal
			# ~Expanción posicional~
			# Variación Método de Horner

			"""
			numeroFinal = pasarAHexa(numero)
			final = stringANumero(numeroFinal)
			print("Valor "+ numeroAString(valor) + ": "+ numeroFinal + " (Original: Octal &"+ numeroAString(numero)+ ")")
			valor += 1
			# todo: eliminar esto
			if nuevoNumero <= 126 and 32 <= nuevoNumero:
				mensaje = mensaje + numeroAAscii(final)
				print(mensaje)
			"""

			suma = 0
			lista = [ bases[x] for x in texto]
			for x in lista:
				suma = suma * 16 + x

			final = hexaString(suma)

			return final
		else:
			return None

#pene2= bitsHexa(str(145))
#print(partirString(pene2, 4))
print(hexa("*", "2F", 1, ""))
# print(hexa("#", "2D", 1, ""))
# Yo (felipe) estuve modificando algunas cosas por acá, por lo que si algo falla, toda la culpa a mi.
