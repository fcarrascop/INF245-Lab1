from leerarchivo import conversion
from utils import ascii

def partirString(string: str, cantidad: int = 3) -> list[str]:
	if len(string) % cantidad != 0:
		string = "0" * (len(string) % cantidad) + string
	return [string[i:i+cantidad] for i in range(0, len(string), cantidad)]

def decimalString(numero: int) -> str:
	if (numero == 0):
		return "0"

	texto = []
	while numero > 0:
		digito = numero % 10
		texto.append("0123456789"[digito])
		numero //= 10

	texto.reverse()
	final = "".join(texto)
	return final

def numeroAString(numero):
    resultado = ""
    
    while numero > 0:
        digito = numero % 10
        caracter = chr(digito + ord('0'))
        resultado = caracter + resultado
        numero = numero // 10
    
    return resultado

def stringANumero(texto):
    numero = 0
    u = 0
    while u < len(texto):
        numero = numero * 10 + conversion[texto[u]]
        u = u + 1 
    return numero

def numeroAAscii(numero):
    return ascii[numero]