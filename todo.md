# Todo Tarea

## To do:
- [ ] Crear las funciones necesarias para el programa
	- [X] Leer texto
	- [X] Eliminar ruido
	- [X] Seleccionar x base
	- [X] Leer inputs
	- [ ] Binario -> Decimal, Octal, Hexa
	- [ ] Octal -> Binario, Decimal, Hexa
	- [ ] Decimal -> Binario, Octal, Hexa
	- [ ] Hexa -> Binario, Octal, Decimal
	- [ ] Visualizador outputs
- [ ] Crear README.md
	- [ ] Nombre, Rol, Paralelo
	- [ ] Algoritmos utilizados
	- [ ] Supuestos utilizados
- [ ] Comentar y documentar la tarea.
- [ ] Pruebas con ejemplos (Chatgpt)
- [ ] (opcional) Divertirse


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
