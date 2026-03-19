from utils.strings import numeroAAscii

valores = {
	"*": "Binario",
	"&": "Octal",
	"#": "Decimal",
	"!": "Hexadecimal",
}

def printValores(index: int, mensaje: str, signo: str, inicial: str, final: str, base: int) -> list:
    print("Valor " + str(index) + ": " + final + " (Original: " + valores[signo] + " " + signo + inicial+ ")")
    
    index += 1

    mensaje += numeroAAscii(final, base)
    print(numeroAAscii(final, base))
    print(mensaje)

    return None
