# Lista de tareas

Esta es una aplicación sencilla de lista de tareas, desarrollada en Python utilizando la biblioteca PySimpleGUI para la interfaz gráfica de usuario de escritorio y las funciones definidas en el archivo functions.py para trabajar con una lista de tareas almacenada en un archivo de texto. La aplicación permite al usuario agregar, editar y completar tareas.

## Requerimientos

Antes de ejecutar la aplicación, asegúrate de tener instalado Python 3.10 o superior en tu sistema. Además, necesitarás instalar el paquete PySimpleGUI. Puedes instalar este paquete ejecutando el siguiente comando en tu terminal:

```
pip install PySimpleGUI
```

## Ejecución

Para ejecutar la aplicación, simplemente abre una terminal en el directorio donde se encuentra el archivo `app.py` y ejecuta el siguiente comando:

```
python app.py
```


## Funciones

A continuación se describen las funciones que se utilizan en este archivo:

* `functions.get_lista(filepath: str = FILEPATH) -> List[str]`: Esta función lee un archivo de texto y devuelve una lista de tareas. La ruta del archivo de texto se puede especificar como argumento. Si no se especifica, se utiliza la ruta predeterminada.

* `functions.set_lista(tds: List[str], filepath: str = FILEPATH) -> None`: Esta función escribe una lista de tareas en un archivo de texto. La lista de tareas y la ruta del archivo de texto se pueden especificar como argumentos. Si no se especifica la ruta del archivo, se utiliza la ruta predeterminada.

* `functions.actualizar_lista(tds: List[str], window: sg.Window) -> None`: Esta función actualiza la interfaz gráfica de usuario con la lista de tareas actualizada. La lista de tareas y la ventana de la interfaz gráfica de usuario se especifican como argumentos.

## Interfaz gráfica de usuario

La interfaz gráfica de usuario de esta aplicación consiste en una ventana principal que contiene los siguientes elementos:

* Un reloj que muestra la hora actual.
* Un campo de entrada de texto para escribir la tarea.
* Un botón para agregar una nueva tarea.
* Una lista de tareas.
* Un botón para editar la tarea seleccionada.
* Un botón para marcar como completada la tarea seleccionada.
* Un botón para salir de la aplicación.

La lista de tareas se actualiza automáticamente cuando se agrega o se completa una tarea.

## Contribuciones

Si deseas contribuir a esta aplicación, eres bienvenido a hacerlo. Simplemente haz un fork del repositorio, haz tus cambios y envía un pull request. Tu contribución será revisada y, si es aceptada, se fusionará con la rama principal del repositorio.

## Licencia

Esta aplicación se distribuye bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.