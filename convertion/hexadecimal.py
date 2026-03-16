# from typing import
from octal import leerOctal
from utils.bases import bases
from utils.strings import decimalString
from utils.strings import stringANumero
from utils.strings import numeroAString
from utils.strings import numeroAAscii
from convertion.binario import leerBinario

def pasarAHexa(numero: int) -> str:
    hexa = ""
    letras = "0123456789ABCDEF"

    while numero > 0:
        hexa = letras[numero % 16] + hexa
        numero = numero // 16

    return(hexa)

def hexa(tipo: str, texto: str, valor: int, mensaje: str) -> str | None:
		numero = stringANumero(texto)

		if tipo == "*":
			# Binario

			nuevoNumero = leerBinario(numero)
			numeroFinal = pasarAHexa(nuevoNumero)

			print("Valor "+ numeroAString(valor) + ": "+ numeroFinal + " (Original: Octal &"+ numeroAString(numero)+ ")")
			valor += 1

			if nuevoNumero <= 126 and 32 <= nuevoNumero:
				mensaje = mensaje + numeroAAscii(nuevoNumero)
				print(mensaje)
				
			return numeroFinal

		elif tipo == "&":
			# Octal
			# Conversión de base pasando por decimal

			nuevoNumero = leerOctal(numero)
			numeroFinal = pasarAHexa(nuevoNumero)

			print("Valor "+ numeroAString(valor) + ": "+ numeroFinal + " (Original: Octal &"+ numeroAString(numero)+ ")")
			valor += 1

			if nuevoNumero <= 126 and 32 <= nuevoNumero:
				mensaje = mensaje + numeroAAscii(nuevoNumero)
				print(mensaje)
			return numeroFinal
		
		elif tipo == "#":
			# Decimal
			# Expanción posicional

			numeroFinal = pasarAHexa(numero)
			final = stringANumero(numeroFinal)
			print("Valor "+ numeroAString(valor) + ": "+ numeroFinal + " (Original: Octal &"+ numeroAString(numero)+ ")")
			valor += 1

			if nuevoNumero <= 126 and 32 <= nuevoNumero:
				mensaje = mensaje + numeroAAscii(final)
				print(mensaje)

			return final
		else:
			return None

# Yo (felipe) estuve modificando algunas cosas por acá, por lo que si algo falla, toda la culpa a mi.
