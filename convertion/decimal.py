from utils.bases import bases
from utils.ascii import ascii
from utils.strings import MetodoHorner
from utils.printValores import printValores

def decimal(tipo: str, texto: str, valor: int, mensaje: str) -> str | None:

    if tipo == "#":
        return texto
    elif tipo == "*":
    	# Binario
    	# División repetida
        suma = 0

        for x in texto:
            suma = suma * 2 + bases[x]

        printValores(valor, mensaje, tipo, texto, str(suma), 10)

        return None

        # return final

    elif tipo == "&":
    	# Octal
    	# División repetida
        suma = 0
        lista = [ bases[x] for x in texto]
        for x in lista:
            suma = suma * 8 + x

        final = str(suma)

        printValores(valor, mensaje, tipo, texto, final, 10)

        return None

    elif tipo == "!":
    	# Hexadecimal
    	# División repetida

        printValores(valor, mensaje, tipo, texto, str(MetodoHorner(texto, 16)), 10)

        return None
    else:
    	return None

# print(decimal("!", "41"))
