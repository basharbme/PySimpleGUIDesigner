import PySimpleGUI as sg

layout = [[]]
window = sg.Window('App', layout)

while True:
	event, values = window.Read()
	if event is None or event == 'Exit':
		break

mice

window.Close()
