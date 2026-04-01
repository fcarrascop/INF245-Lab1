from utils.bases import bases
from utils.strings import MetodoHorner

def decimal(tipo: str, texto: str) -> str | None:

    if tipo == "#":
        return texto
    elif tipo == "*":
    	# Binario
    	# División repetida
        suma = 0

        for x in texto:
            suma = suma * 2 + bases[x]

        return str(suma)

    elif tipo == "&":
    	# Octal
    	# División repetida
        suma = 0
        lista = [ bases[x] for x in texto]
        for x in lista:
            suma = suma * 8 + x

        final = str(suma)

        return final

    elif tipo == "!":
    	# Hexadecimal
    	# División repetida

        return str(MetodoHorner(texto, 16))
    else:
    	return ""
