from convertion.binario import binario
from convertion.octal import octal
from convertion.decimal import decimal
from convertion.hexadecimal import hexadecimal
from utils.printValores import printValores

aceptados = {
	"*": "01",
	"&": "01234567",
	"#": "0123456789",
	"!": "0123456789abcdefABCDEF"
}

transformaciones = {
    "2": binario,
	"8": octal,
	"10": decimal,
	"16": hexadecimal
}

def leerArchivo():
    """
    Lee el archivo de notas, convierte los valores y muestra el resultado.

    Args:
       	No recibe argumentos. El archivo a leer se define en el modulo.

    Returns:
       	None

    Raises:
       	FileNotFoundError: Si no existe el archivo de entrada.

    Example:
       	>>> leerArchivo()
       	None
    """

    global valor, mensaje, archivo

    valor = 1
    mensaje = ""
    archivo = "notas_dm.txt"

    print("--- DECODIFICADOR DE NOTAS ---")
    baseSolicitada = input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): ")

    if baseSolicitada not in ["2", "8", "10", "16"]:
        print("Base inválida, en caso de querer decodificar el código, vuelve a intentar el DECODIFICADOR DE NOTAS con alguna de las bases permitidas mencionadas anteriormente")
        exit()
    print()

    archivo = open(archivo, "r")

    print(f"[+] Procesando archivo: {archivo}...")
    print("[!] Filtrando ruido místico (valores fuera de rango ASCII)...")
    print("LISTA DE VALORES EXTRAÍDOS (Base "+ baseSolicitada + "):")
    print("--------------------------------------------------")

    while True:
        linea = archivo.readline()

        if linea == "":
            break
        i = 0

        while i < len(linea):
            caracter = linea[i]

            if caracter in "*&#!" and i + 1 < len(linea):
                caracteresAceptados = aceptados[caracter]
                pos_primer_numero = i + 1
                if linea[pos_primer_numero] in "0123456789":

                    pos_segundo_numero = pos_primer_numero

                    while pos_segundo_numero < len(linea) and linea[pos_segundo_numero] in caracteresAceptados:
                        pos_segundo_numero += 1

                    textoNumero = linea[pos_primer_numero:pos_segundo_numero]

                    valorFinal = transformaciones[baseSolicitada](caracter, textoNumero)

                    mensaje += printValores(valor, caracter, textoNumero, valorFinal.lstrip("0"), int(baseSolicitada))

                    valor += 1
            i = i + 1
        break

    print("--------------------------------------------------")
    print("MENSAJE DECODIFICADO:")
    print(f"\"{mensaje}\"")
    print("[Proceso finalizado con exito]")

    archivo.close()
