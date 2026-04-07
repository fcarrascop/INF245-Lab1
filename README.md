# Laboratorio 1

## Estudiantes
- Felipe Carrasco Patelli - 202473522-5 - Paralelo 200
- Tomas Gonzales Pinto - 202473519-5 - Paralelo 200

## Especificaciones y desarrollo
El programa lee un archivo de texto con un flujo continuo de caracteres, detecta los prefijos de base (* binario, & octal, # decimal, ! hexadecimal) y extrae los numeros validos. 
Despues convierte cada valor a la base solicitada (2, 8, 10 o 16), imprime la lista de valores convertidos y arma el mensaje ASCII filtrando solo el rango [32, 126].

## Como ejecutar
El programa se ejecuta con:
```python
python main.py
```
Para poder cambiar el archivo a descifrar, se tiene que modificar la variable `archivoALeer`. Ahí hay que agregar el nombre exacto del archivo, en el directorio del proyecto.
En este caso, viene por defecto el archivo `notas_dm.txt`

### Algoritmos de conversion
- Decimal a binario: Divisiones sucesivas entre 2
- Octal a binario: Conversión por agrupación de 3 bits
- Hexadecimal a binario: Conversión por agrupación de 4 bits
- Binario a octal: Agrupación de bits y evaluación de cada grupo en base 2 mediante expansión posicional
- Decimal a octal: Divisiones sucesivas entre 8
- Hexadecimal a octal: Agrupación de bits pasando por binario
- Binario a decimal: Método de Horner
- Octal a decimal: Método de Horner
- Hexadecimal a decimal: Método de Horner
- Binario a hexadecimal: Agrupación de 4 bits y mapeo
- Decimal a hexadecimal: Divisiones sucesivas entre 16
- Octal a hexadecimal: Conversión por agrupación de bits pasando por binario

## Supuestos
1. Se consideran validos los digitos hexadecimales en mayusculas y minusculas.
2. Los valores a convertir son positivos.
3. Solo se construye el mensaje con valores ASCII imprimibles (32 a 126).
