import PySimpleGUI as sg

layout = [
    [sg.Text('Bill Total: '), sg.InputText(key='bill')],
    [sg.Frame('Tip Percentage', [[
        sg.Radio('10%', key='10', group_id='per'),
        sg.Radio('15%', key='15', default=True, group_id='per'),
        sg.Radio('20%', key='20', group_id='per')
    ]])],
    [sg.Button('Calculate')]
]

window = sg.Window('Tip Calculator').Layout(layout)
event, values = window.Read()

bill = round(float(values['bill']), 2)

if values['10']:
    total = round(bill * 1.1, 2)
    tip = round(total-bill, 2)
    sg.Popup('New Total: ' + '$' + str(total) + '\n' + 'Tip: ' + str(tip))
elif values['15']:
    total = round(bill * 1.15, 2)
    tip = round(total-bill, 2)
    sg.Popup('New Total: ' + '$' + str(total) + '\n' + 'Tip: ' + str(tip))
elif values['20']:
    total = round(bill * 1.2, 2)
    tip = round(total-bill, 2)
    sg.Popup('New Total: ' + '$' + str(total) + '\n' + 'Tip: ' + str(tip))



