from utils.strings import numeroAAscii

valores = {
	"*": "Binario",
	"&": "Octal",
	"#": "Decimal",
	"!": "Hexadecimal",
}

"""
print("Valor "+ numeroAString(valor) + ": "+ numeroFinal + " (Original: Octal &"+ numeroAString(numero)+ ")")
			valor += 1
			# todo: eliminar esto
			if nuevoNumero <= 126 and 32 <= nuevoNumero:
				mensaje = mensaje + numeroAAscii(final)
				print(mensaje)
"""

def printValores(index: int, mensaje: str, signo: str, inicial: str, final: str) -> None:
	print("Valor " + str(index) + ": " + final + " (Original: " + valores[signo] + " " + signo + inicial)

	index += 1

	if int(final) <= 126 and 32 <= int(final):
		mensaje += numeroAAscii(int(final))
