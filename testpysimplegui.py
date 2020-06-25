import PySimpleGUI as sg

def ToDoItem(num):
    return [sg.Text(f'{num}. '), sg.In()]

layout = [ToDoItem(x) for x in range(1,6)] + [[sg.Button('Save'), sg.Button('Exit')]]

window = sg.Window('To Do List Example', layout)
event, values = window.read()
print(values)

lista = []
for key, value in values.items():
    if value != '':
        lista.append(value)

print(lista)