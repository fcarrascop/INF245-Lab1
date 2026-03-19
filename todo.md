# Todo Tarea

## To do:
- [ ] Crear las funciones necesarias para el programa
	- [X] Leer texto
	- [X] Eliminar ruido
	- [X] Seleccionar x base
	- [X] Leer inputs
	- [X] Binario -> Decimal, Octal, Hexa
	- [ ] Octal -> Binario, Decimal, Hexa
	- [X] Decimal -> Binario, Octal, Hexa
	- [ ] Hexa -> Binario, Octal, Decimal
	- [ ] Visualizador outputs
	- [ ] Completar conversiones faltantes en hexadecimal.py y octal.py
		- [ ] hexadecimal.py: decimal -> hexadecimal devuelve decimal (str(suma))
		- [ ] hexadecimal.py: octal -> hexadecimal sin implementar
		- [ ] octal.py: hexadecimal -> octal devuelve texto fijo
	- [ ] Arreglar padding en partirString para agrupacion de bits
		- [ ] partirString: relleno con ceros usa len % cantidad, deberia usar cantidad - (len % cantidad)
	- [ ] Revisar formato de salida en printValores
		- [ ] printValores: falta cerrar parentesis en el print de la linea "Valor ..."
		- [ ] salida: eliminar prints extra (caracter, textoNumero, transformado)
- [ ] Crear README.md
	- [ ] Nombre, Rol, Paralelo
	- [ ] Algoritmos utilizados
	- [ ] Supuestos utilizados
- [ ] Comentar y documentar la tarea.
- [ ] Pruebas con ejemplos (Chatgpt)
- [ ] (opcional) Divertirse

## Problemas (según codex)
Problemas principales
- hexadecimal.py: cuando el tipo es # (decimal → hexadecimal) devuelves str(suma) en decimal, no en base 16. Eso rompe el resultado en base 16 y el mensaje ASCII.
- hexadecimal.py: el caso & (octal → hexadecimal) está sin implementar (devuelve nada útil). Si el archivo trae & y eliges base 16, fallará.
- octal.py: el caso ! (hexadecimal → octal) devuelve "Hexa" fijo, no hace conversión real.
- binario.py: para tipo & y ! usas agrupación por 3/4 bits pero partirString rellena con ceros al inicio de forma incorrecta (usa len % cantidad en vez de la cantidad de ceros necesarios). Eso altera conversiones cuando el largo no es múltiplo de 3 o 4.
- printValores.py: print de la línea “Valor ...” no cierra paréntesis ). Dependiendo del archivo, eso puede provocar error de sintaxis o salida incompleta.
- leerarchivo.py: estás imprimiendo caracter, textoNumero, transformado en cada token; eso no es el formato pedido en el PDF (solo la lista y el mensaje). No es error lógico, pero rompe la salida esperada.
- leerarchivo.py: no validas que el número extraído pertenezca a la base del prefijo más allá del while de captura; si hay mezcla con ruido tipo !F23A, tu transformaciones deben convertirlo bien. Actualmente no todas las conversiones están completas.


## Reglas
- Todo tiene que estár documentado. No por lineas, sino por funciones.
- Tratar de ocupar nombres descriptivos para las variables/funciones. Ocupar camelCase.
- Ocupar el git de forma ordenada. O sino wate.
- Tratar de separar todo en archivos aparte y en carpetas diferentes. Para que se vea bonito por lo menos.
- No chatgpt!!!!

## Documentación funciones (en general)
```python
def get_user_by_id(user_id: int) -> dict | None:
    """
    Obtiene un usuario desde la base de datos.

    Args:
        user_id (int): Identificador único del usuario.

    Returns:
        dict | None:
            Diccionario con la información del usuario si existe,
            de lo contrario None.

    Raises:
        DatabaseConnectionError: Si falla la conexión a la base de datos.

    Example:
        >>> get_user_by_id(10)
        {"id": 10, "name": "Felipe"}
    """
```
