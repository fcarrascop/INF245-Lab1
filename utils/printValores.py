from utils.strings import numeroAAscii

valores = {
	"*": "Binario",
	"&": "Octal",
	"#": "Decimal",
	"!": "Hexadecimal",
}

def printValores(index: int, signo: str, inicial: str, final: str, base: int) -> str:
    print("Valor " + str(index) + ": " + final + " (Original: " + valores[signo] + " " + signo + inicial+ ")")

    nuevo = numeroAAscii(final, base)

    return nuevo
