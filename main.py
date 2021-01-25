import logging
import ChooseHigherModule as ChooseHigher
import ChooseExactModule as ChooseExact
import ScaleModule as ScaleModule
import PySimpleGUI as SimpleGui

logging.basicConfig(level=logging.INFO)

SimpleGui.theme('DarkAmber')
layout = [[SimpleGui.Text('Pick module')],
          [SimpleGui.Text('_' * 100, size=(65, 1))],
          [SimpleGui.Text('Intervals exercises')],
          [SimpleGui.Button('Choose Higher', size=(15, 1))],
          [SimpleGui.Button('Choose Exact', size=(15, 1))],
          [SimpleGui.Text('_' * 100, size=(65, 1))],
          [SimpleGui.Text('Scales exercises')],
          [SimpleGui.Button('Major Scale', size=(15, 1))],
          [SimpleGui.Button('Minor Scale', size=(15, 1))],
          [SimpleGui.Text('_' * 100, size=(65, 1))],
          [SimpleGui.Button('Exit', size=(15, 1))]]

window = SimpleGui.Window("Pick module", layout, size=(400, 500), element_justification='c')

choose_higher_module = ChooseHigher.ChooseHigherModule()
choose_exact_module = ChooseExact.ChooseExactModule()
scale_module = ScaleModule.ScaleModule()

while True:
    event, values = window.read()
    if event == SimpleGui.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Choose Higher':
        choose_higher_module.run_module()
    if event == 'Choose Exact':
        choose_exact_module.run_module()
    if event == 'Major Scale':
        scale_module.run_module("major")
    if event == 'Minor Scale':
        scale_module.run_module("minor")
