import PySimpleGUI as sg
import os
import glob
import subprocess


# Save the scripts
bash_scripts = next(os.walk('./bash-scripts'))[2]
puppeteer_scripts = next(os.walk('./puppeteer-scripts'))[2]

# Set theme for window
sg.theme('BluePurple')

# Layout of window
main_layout = [[sg.Text('Choose a script to run.'), sg.Text(key='-OUTPUT-')],
            [sg.Text('Scripts:'), sg.Listbox(s=(50,5), key='-IN-', values=puppeteer_scripts, expand_x=True, expand_y=True)],
          [sg.Button('Run'), sg.Button('Exit')]]

log_layout = [
    [sg.Multiline(s=(50, 10), key="-LOGS-", expand_x=True, expand_y=True), sg.Button('Clear Logs')]
]

layout = [
    [sg.TabGroup([
        [sg.Tab('Scripts', main_layout), sg.Tab('Logs', log_layout)]
    ], expand_x=True, expand_y=True)]
]

window = sg.Window('Pup Scripts', layout, element_justification='c', resizable=True)

# Variables
current_script = ""
logs = []

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Run':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update("Running: " + values['-IN-'][0])
        current_script = values['-IN-']
        # os.system('sh ./bash-scripts/run.sh ' + current_script[0])
        result = subprocess.run('sh ./bash-scripts/run.sh ' + current_script[0], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for log_output in result.stdout.split('\n'):
            window['-LOGS-'].print(log_output)
    if event == 'Clear Logs':
        window['-LOGS-'].update('')

window.close()