from utils.bases import bases
from utils.ascii import ascii
from utils.strings import MetodoHorner
from utils.printValores import printValores

def decimal(tipo: str, texto: str, valor: int, mensaje: str) -> str | None:

    if tipo == "#":

        mensaje = mensaje + printValores(valor, tipo, texto, texto, 10)
			
        valor = valor + 1

        return valor, mensaje
    
    elif tipo == "*":
    	# Binario
    	# División repetida
        suma = 0

        for x in texto:
            suma = suma * 2 + bases[x]

        mensaje = mensaje + printValores(valor, tipo, texto, str(suma).lstrip("0"), 10)
			
        valor = valor + 1

        return valor, mensaje

    elif tipo == "&":
    	# Octal
    	# División repetida
        suma = 0
        lista = [ bases[x] for x in texto]
        for x in lista:
            suma = suma * 8 + x

        final = str(suma)

        mensaje = mensaje + printValores(valor, tipo, texto, final.lstrip("0"), 10)
			
        valor = valor + 1

        return valor, mensaje

    elif tipo == "!":
    	# Hexadecimal
    	# División repetida

        mensaje = mensaje + printValores(valor, tipo, texto, str(MetodoHorner(texto, 16)).lstrip("0"), 10)
			
        valor = valor + 1

        return valor, mensaje
    else:
    	return None

