from utils.bases import bases
from utils.ascii import ascii

def partirString(string: str, cantidad: int = 3) -> list[str]:
	if len(string) % cantidad != 0:
		faltan = cantidad - (len(string) % cantidad)
		string = "0" * faltan + string
	return [string[i:i+cantidad] for i in range(0, len(string), cantidad)]

def numeroAAscii(numero: str, base: int) -> str:
    valor = MetodoHorner(numero, base)
    
    if valor <= 126 and 32 <= valor:
        letraMensaje = ascii[valor]
        return letraMensaje

    else:
        return ""

def MetodoHorner(numero: str, base: int) -> int:
	valor = 0

	for digito in numero:
		valor = valor * base + bases[digito]
		
	return valor