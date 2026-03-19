from convertion.binario import binario
from convertion.decimal import decimal
from convertion.octal import octal
from convertion.hexadecimal import hexadecimal


valor = 1
mensaje = ""

print("-- DECODIFICADOR DE NOTAS --\n")


baseSolicitada = input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): ")


if baseSolicitada not in ["2", "8", "10", "16"]:
    print("Base inválida, en caso de querer decodificar el código, vuelve a intentar el DECODIFICADOR DE NOTAS con alguna de las bases permitidas mencionadas anteriormente")
    exit()


print()


archivo = open("notas_dm.txt", "r")


print("""[+] Procesando archivo: notas_dm
[!] Filtrando ruido místico (valores fuera de rango ASCII)...\n""")


print("LISTA DE VALORES EXTRAÍDOS (Base "+ baseSolicitada + "):")


print("--------------------------------------------------")


while True:
    linea = archivo.readline()


    i = 0


    while i < len(linea):
        if linea == "":
            break
        caracter = linea[i]

        if caracter in "*&#!" and i + 1 < len(linea) and linea[i + 1] in "0123456789":

            pos_primer_numero = i + 1
            pos_segundo_numero = pos_primer_numero
            while pos_segundo_numero < len(linea) and linea[pos_segundo_numero] in "0123456789":
                pos_segundo_numero += 1
            textoNumero = linea[pos_primer_numero:pos_segundo_numero]
            if baseSolicitada == 16:
                hexadecimal(caracter, textoNumero, valor, mensaje)
            elif baseSolicitada == 10:
                decimal(caracter, textoNumero, valor, mensaje)
            elif baseSolicitada == 8:
                octal(caracter, textoNumero, valor, mensaje)
            elif baseSolicitada == 2:
                binario(caracter, textoNumero, valor, mensaje)

        i = i + 1

    print(linea)


archivo.close()
