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

baseSigno = {
	"2": "*",
	"8": "&",
	"10": "#",
	"16": "!"
}

transformaciones = {
    "*": binario,
	"&": octal,
	"#": decimal,
	"!": hexadecimal
}


# archivo = "./Archivos_prueba/Encriptados/prueba_1.txt"
archivo = "notas_dm.txt"
# archivo = "notas_dm_base2.txt"
# archivo = "notas_dm_base8.txt"
# archivo = "notas_dm_base10.txt"
# archivo = "notas_dm_base16.txt"

def leerArchivo():
    global valor, mensaje, archivo

    valor = 1
    mensaje = ""
    archivo = "notas_dm.txt"

    print("-- DECODIFICADOR DE NOTAS --\n")
    baseSolicitada = input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): ")

    if baseSolicitada not in ["2", "8", "10", "16"]:
        print("Base inválida, en caso de querer decodificar el código, vuelve a intentar el DECODIFICADOR DE NOTAS con alguna de las bases permitidas mencionadas anteriormente")
        exit()
    print()

    archivo = open(archivo, "r")

    print("[+] Procesando archivo: notas_dm")
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
                    

                    if baseSolicitada == "16":
                        valor, mensaje = hexadecimal(caracter, textoNumero, valor, mensaje)
                    elif baseSolicitada == "10":
                        valor, mensaje = decimal(caracter, textoNumero, valor, mensaje)
                    elif baseSolicitada == "8":
                        valor, mensaje = octal(caracter, textoNumero, valor, mensaje)
                    elif baseSolicitada == "2":
                        valor, mensaje = binario(caracter, textoNumero, valor, mensaje)

                    """if (len(textoNumero) > 0):
                        print(f"caracter: {caracter}")
                        transformado = transformaciones[caracter](baseSigno[baseSolicitada], textoNumero)

                        print(caracter)
                        print(textoNumero)
                        print(transformado)

                        valor, mensaje = printValores(valor, mensaje, caracter, textoNumero, transformado)"""
            i = i + 1
        break

    print("--------------------------------------------------")
    print("MENSAJE DECODIFICADO")
    print(f"{mensaje}\n")
    print("[Proceso finalizado con éxito]")

    archivo.close()



