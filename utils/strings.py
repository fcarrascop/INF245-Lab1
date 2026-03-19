from utils.bases import bases
from utils.ascii import ascii

def partirString(string: str, cantidad: int = 3) -> list[str]:
	if len(string) % cantidad != 0:
		string = "0" * (len(string) % cantidad) + string
	return [string[i:i+cantidad] for i in range(0, len(string), cantidad)]


def numeroAAscii(numero):
    return ascii[numero]
