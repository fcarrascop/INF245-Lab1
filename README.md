# Laboratorio 1

## Estudiantes
- Felipe Carrasco Patelli - 202473522-5 - Paralelo 200
- Tomas Gonzales Pinto - 202473519-5 - Paralelo 200

## Especificaciones y desarrollo
El programa lee un archivo de texto con un flujo continuo de caracteres, detecta los prefijos de base
(* binario, & octal, # decimal, ! hexadecimal) y extrae los numeros validos. Despues convierte cada
valor a la base solicitada (2, 8, 10 o 16), imprime la lista de valores convertidos y arma el mensaje
ASCII filtrando solo el rango [32, 126].

### Algoritmos de conversion
- Binario a decimal: suma posicional (metodo de Horner en base 2).
- Octal a decimal: suma posicional (metodo de Horner en base 8).
- Hexadecimal a decimal: suma posicional (metodo de Horner en base 16).
- Decimal a binario: divisiones sucesivas por 2.
- Decimal a octal: divisiones sucesivas por 8.
- Decimal a hexadecimal: divisiones sucesivas por 16.
- Binario a octal: agrupacion de 3 bits y mapeo.
- Binario a hexadecimal: agrupacion de 4 bits y mapeo.
- Octal a binario: cada digito a 3 bits.
- Hexadecimal a binario: cada digito a 4 bits.
- Octal a hexadecimal: octal -> binario -> hexadecimal.
- Hexadecimal a octal: hexadecimal -> binario -> octal.

## Supuestos
1. Se consideran validos los digitos hexadecimales en mayusculas y minusculas.
2. Los valores a convertir son positivos.
3. Solo se construye el mensaje con valores ASCII imprimibles (32 a 126).
