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

        return str(suma)

        # return final

    elif tipo == "&":
    	# Octal
    	# División repetida
        suma = 0
        lista = [ bases[x] for x in texto]
        for x in lista:
            suma = suma * 8 + x

        final = str(suma)

        print(final)

        return final

    elif tipo == "!":
    	# Hexadecimal
    	# División repetida

        print(MetodoHorner(texto, 16))
        printValores(1, "", tipo, texto, str(MetodoHorner(texto, 16)), 10)

        return None
    else:
    	return None

# print(decimal("!", "41"))
