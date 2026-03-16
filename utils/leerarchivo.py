conversion = {
    '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9
}
valor = 1

mensaje = 1

print("-- DECODIFICADOR DE NOTAS --\n")


base_solicitada = input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): ")


if base_solicitada not in ["2", "8", "10", "16"]:
    print("Base inválida, en caso de querer decodificar el código, vuelve a intentar el DECODIFICADOR DE NOTAS con alguna de las bases permitidas mencionadas anteriormente")
    exit()


print()


archivo = open("notas_dm.txt", "r")


print("""[+] Procesando archivo: notas_dm
[!] Filtrando ruido místico (valores fuera de rango ASCII)...\n""")


print("LISTA DE VALORES EXTRAÍDOS (Base "+ base_solicitada + "):")


print("--------------------------------------------------")


while True:
    linea = archivo.readline()


    i = 0


    while i < len(linea):
        caracter = linea[i]

        if caracter in "*&#!" and i + 1 < len(linea) and linea[i + 1] in "0123456789":

            pos_primer_numero = i + 1
            pos_segundo_numero = pos_primer_numero
            while pos_segundo_numero < len(linea) and linea[pos_segundo_numero] in "0123456789":
                pos_segundo_numero += 1
            texto_numero = linea[pos_primer_numero:pos_segundo_numero]
        i = i + 1
    if linea == "":
        break

    print(linea)


archivo.close()
