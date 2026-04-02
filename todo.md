# Todo Tarea

## To do:
- [ ] Crear las funciones necesarias para el programa
	- [X] Leer texto
	- [X] Eliminar ruido
	- [X] Seleccionar x base
	- [X] Leer inputs
	- [X] Binario -> Decimal, Octal, Hexa
	- [X] Octal -> Binario, Decimal, Hexa
	- [X] Decimal -> Binario, Octal, Hexa
	- [X] Hexa -> Binario, Octal, Decimal
	- [X] Visualizador outputs (formato exacto del PDF)
	- [X] Completar conversiones faltantes en hexadecimal.py y octal.py
		- [X] hexadecimal.py: decimal -> hexadecimal devuelve decimal (str(suma))
		- [X] hexadecimal.py: octal -> hexadecimal sin implementar
		- [X] octal.py: hexadecimal -> octal devuelve texto fijo
	- [X] Arreglar padding en partirString para agrupacion de bits
		- [X] partirString: relleno con ceros usa len % cantidad, deberia usar cantidad - (len % cantidad)
	- [X] Revisar formato de salida en printValores
		- [X] printValores: falta cerrar parentesis en el print de la linea "Valor ..."
		- [X] salida: eliminar prints extra (caracter, textoNumero, transformado)
- [ ] Crear README.md
	- [ ] Nombre, Rol, Paralelo
	- [ ] Algoritmos utilizados (detalle de conversiones)
	- [ ] Supuestos utilizados
- [ ] Comentar y documentar la tarea.
- [ ] Pruebas con ejemplos (Chatgpt)
- [ ] (opcional) Divertirse

## Que nos falta

- [ ] Ajustar formato de salida según PDF (encabezados, comillas del mensaje, nombre del archivo)
- [ ] Aceptar letras hexadecimales como primer dígito tras el prefijo (!A1, !fF, etc.)
- [ ] Normalizar a mayúsculas o soportar minúsculas en MetodoHorner/bases para evitar KeyError
- [ ] Procesar archivos con múltiples líneas (no cortar tras la primera)
- [ ] Manejar error de lectura de archivo sin terminar abruptamente
- [ ] Documentar funciones (docstrings por función)
- [ ] Completar README con algoritmos y roles/paralelo
- [ ] Ejecutar pruebas con archivos de ejemplo

## Problemas actuales
- leerarchivo.py: solo acepta dígitos 0-9 como primer caracter tras el prefijo, por lo que !A1 se ignora.
- utils/strings.py: MetodoHorner no normaliza a mayúsculas; con hex en minúscula falla el diccionario bases.
- utils/leerarchivo.py: procesa solo la primera línea del archivo (break al final del while principal).
- utils/leerarchivo.py: no maneja errores de lectura de archivo (si falta el .txt, se cae).
- Formato de salida: no coincide 1:1 con el ejemplo del PDF (mensaje sin comillas ni “:”, nombre de archivo sin .txt).


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

## Instrucciones para el TOM

- Si quieres traer los cambios desde mi rama (estando tú en `main`) y no has hecho más cambios en tu rama, tienes que escribir:
```git
git fetch && git reset --hard origin/felipe
```
