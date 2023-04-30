import time
import functions
import PySimpleGUI as psg
import os

# Verifica si el archivo lista.txt existe
if not os.path.exists("files/lista.txt"):
    with open("files/lista.txt", "w") as file:
        pass

# Setea el color de la vista
psg.theme("Purple")

# Crea los elementos de la vista
label_clock = psg.Text("", key="clock")
label = psg.Text("Escriba una tarea")
input_box = psg.InputText(tooltip="Ingrese una tarea", key="todo", size=50)
add_button = psg.Button("Agregar")

list_box = psg.Listbox(values=functions.get_lista(), key="todos",
                       enable_events=True, size=(50, 10))
edit_button = psg.Button("Editar")
complete_button = psg.Button("Completar")
exit_button = psg.Button("Salir")

# Orden de aparición de los elementos
window_elements = [[label_clock],
                   [label],
                   [input_box, add_button],
                   [list_box, edit_button, complete_button],
                   [exit_button]]

window = psg.Window("App: Lista de Tareas",
                    layout=window_elements,
                    font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%A %d/%m/%y %I:%M %p"))
    match event:
        case "Agregar":
            todos = functions.get_lista()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.set_lista(todos)
            functions.actualizar_lista(todos, window)
        case "Editar":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.get_lista()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.set_lista(todos)
                functions.actualizar_lista(todos, window)
            except IndexError:
                psg.popup("Por favor seleccione una tarea para editar.", font='15')
        case "Completar":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_lista()
                todos.remove(todo_to_complete)
                functions.set_lista(todos)
                functions.actualizar_lista(todos, window)
            except IndexError:
                psg.popup("Por favor seleccione una tarea para editar.", font='15')
        case "Salir":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0].strip("\n"))
        case psg.WIN_CLOSED:
            break

window.close()
