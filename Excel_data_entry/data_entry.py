from pathlib import Path

import PySimpleGUI as sg
import pandas as pd

# Add some color to the window
sg.theme('DarkTeal9')

current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
EXCEL_FILE = current_dir / 'Record_of_staff_travel_21-22.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('S/No', size=(3,1)), sg.InputText(key = 'S/No')],
    [sg.Text('Travel Date', size=(15,1)), sg.InputText(key='Travel Date')],
    [sg.Text('Staff/Visitors name', size=(15,1)), sg.InputText(key='Staff/Visitors name')],
    [sg.Text('From', size=(5,1)), sg.InputText(key='From')],
    [sg.Text('Destination', size=(5,1)), sg.InputText(key='Destination')],
    [sg.Text('To', size=(5,1)), sg.InputText(key='To')],
    [sg.Text('Cluster', size=(5,1)), sg.InputText(key='Cluster')],
    # [sg.Text('Favorite Colour', size=(15,1)), sg.Combo(['Green', 'Blue', 'Red'], key='Favorite Colour')],
    # [sg.Text('I speak', size=(15,1)),
    #                         sg.Checkbox('German', key='German'),
    #                         sg.Checkbox('Spanish', key='Spanish'),
    #                         sg.Checkbox('English', key='English')],
    # [sg.Text('No. of Children', size=(15,1)), sg.Spin([i for i in range(0,16)],
    #                                                    initial_value=0, key='Children')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Simple data entry form', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        clear_input()
window.close()