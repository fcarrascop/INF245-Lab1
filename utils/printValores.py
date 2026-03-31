from utils.strings import numeroAAscii, MetodoHorner

valores = {
	"*": "Binario",
	"&": "Octal",
	"#": "Decimal",
	"!": "Hexadecimal",
}

def printValores(index: int, signo: str, inicial: str, final: str, base: int) -> str:
    
	if MetodoHorner(final, base) <= 126 and 32 <= MetodoHorner(final, base):
		print("Valor " + str(index) + ": " + final + " (Original: " + valores[signo] + " " + signo + inicial+ ")")

		nuevo = numeroAAscii(final, base)

		return nuevo

	return ""
