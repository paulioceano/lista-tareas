FILEPATH = "files/lista.txt"


def get_lista(filepath=FILEPATH):
    """ Lee un archivo de texto
    y retorna la lista de tareas."""
    with open(filepath, 'r') as file:
        tds = file.readlines()
    return tds


def set_lista(tds, filepath=FILEPATH):
    """ Escribe la lista de tareas
    en un archivo de texto. """
    with open(filepath, 'w') as file:
        file.writelines(tds)


def actualizar_lista(tds, window):
    window["todos"].update(values=tds)
    window["todo"].update(value="")
