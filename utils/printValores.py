from utils.strings import numeroAAscii

valores = {
	"*": "Binario",
	"&": "Octal",
	"#": "Decimal",
	"!": "Hexadecimal",
}

def printValores(index: int, mensaje: str, signo: str, inicial: str, final: str) -> list:
    print("Valor " + str(index) + ": " + final + " (Original: " + valores[signo] + " " + signo + inicial)
    index += 1


    if int(final) <= 126 and 32 <= int(final):
        mensaje += numeroAAscii(int(final))
        print(mensaje)

    return [index, mensaje]
