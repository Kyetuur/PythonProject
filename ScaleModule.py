import logging
import random

import PySimpleGUI as SimpleGui
import ScaleBuilder as ScaleBuilder
import IntervalGenerator as IntervalGenerator
import Interval as Interval


class ScaleModule:
    def __init__(self):
        self.window = None
        self.correct_tries = 0
        self.all_tries = 0
        self.scale_generator = None
        self.current = 0
        self.correct = None

    def run_module(self, scale):
        layout = [[SimpleGui.Text('Scale')],

                  [SimpleGui.Text('_' * 100, size=(65, 1))],

                  [SimpleGui.Button('__', key='1', disabled=True),
                   SimpleGui.Button('__', key='2', disabled=True),
                   SimpleGui.Button('__', key='3', disabled=True),
                   SimpleGui.Button('__', key='4', disabled=True),
                   SimpleGui.Button('__', key='5', disabled=True),
                   SimpleGui.Button('__', key='6', disabled=True),
                   SimpleGui.Button('__', key='7', disabled=True),
                   SimpleGui.Button('__', key='8', disabled=True)],
                  [SimpleGui.Text('' * 100, size=(65, 1))],
                  [SimpleGui.Button("__", key="LeftAnswer"), SimpleGui.Button("__", key="RightAnswer")],

                  [SimpleGui.Text('_' * 100, size=(65, 1))],
                  [SimpleGui.Button('Back to menu', size=(15, 1))]
                  ]

        self.window = SimpleGui.Window("Scale", layout, size=(400, 500), element_justification='c')
        self.window.finalize()
        self.current = 1
        if scale == "major":
            self.scale_generator = ScaleBuilder.build_major_scale_on_root(IntervalGenerator.get_random_root())
        else:
            self.scale_generator = ScaleBuilder.build_minor_scale_on_root(IntervalGenerator.get_random_root())

        self.correct = next(self.scale_generator)
        self.__common_answer()

        while True:
            event, values = self.window.read()
            if event == SimpleGui.WIN_CLOSED or event == 'Back to menu':
                break

            if event == "LeftAnswer":
                self.__left_chosen()

            if event == "RightAnswer":
                self.__right_chosen()

        self.window.close()
        return

    def __left_chosen(self):
        logging.debug("Left button clicked!")
        if self.correct_button == 'LeftAnswer':
            self.__correct_answer()
        else:
            self.__wrong_answer()

    def __right_chosen(self):
        logging.debug("Right button clicked!")
        if self.correct_button == 'RightAnswer':
            self.__correct_answer()
        else:
            self.__wrong_answer()

    def __correct_answer(self):
        logging.info("Correct Answer")

        self.window[str(self.current)].update(button_color=('white', 'light green'))
        self.__common_answer()

    def __wrong_answer(self):
        logging.info("Wrong Answer")

        self.window[str(self.current)].update(button_color=('white', 'pink'))
        self.__common_answer()

    def __common_answer(self):
        self.window[str(self.current)].update(self.correct)
        self.current += 1

        try:
            self.correct = next(self.scale_generator)
        except StopIteration:
            self.window['LeftAnswer'].update("_", disabled=True)
            self.window['RightAnswer'].update("_", disabled=True)
            return

        close_notes = [Interval.get_sharp(self.correct), Interval.get_bemol(self.correct)]
        incorrect = random.choice(close_notes)

        options = [self.correct, incorrect]
        random.shuffle(options)

        self.correct_button = 'LeftAnswer' if options[0] == self.correct else 'RightAnswer'
        self.window['LeftAnswer'].update(options[0])
        self.window['RightAnswer'].update(options[1])
