import random

import PySimpleGUI as SimpleGui
import logging
import IntervalGenerator as IntervalGenerator
import IntervalPlayer as IntervalPlayer
import IntervalComparer as IntComparer


class ChooseExactModule:
    def __init__(self):
        self.window = None
        self.correct_tries = 0
        self.all_tries = 0

    def run_module(self):
        layout = [[SimpleGui.Text('Choose exact interval')],
                  [SimpleGui.Text('_' * 100, size=(65, 1))],
                  [SimpleGui.Text('All tries: '), SimpleGui.Text(self.all_tries, size=(10, 1), key="AllTries")],
                  [SimpleGui.Text('Correct tries: '),
                   SimpleGui.Text(self.correct_tries, size=(10, 1), key="CorrectTries")],
                  [SimpleGui.Text('_' * 100, size=(65, 1))],
                  [SimpleGui.Button('Play Interval', size=(15, 1))],
                  [SimpleGui.Button('Left', key='LeftAnswer', size=(15, 1)),
                   SimpleGui.Button('Right', key='RightAnswer', size=(15, 1))],
                  [SimpleGui.Text('Last answer: '), SimpleGui.Text("", size=(10, 1), key="LastAnswer")],
                  [SimpleGui.Text('_' * 100, size=(65, 1))],
                  [SimpleGui.Button('Back to menu', size=(15, 1))]]

        self.window = SimpleGui.Window("Choose Exact", layout, size=(400, 500), element_justification='c')
        self.window.finalize()
        self.__common_answer()

        while True:
            event, values = self.window.read()
            if event == SimpleGui.WIN_CLOSED or event == 'Back to menu':
                break
            if event == 'Play Interval':
                IntervalPlayer.play_interval(self.correct)
            if event == 'LeftAnswer':
                self.__left_choosen()
            if event == 'RightAnswer':
                self.__right_choosen()

        self.window.close()
        return

    def __correct_answer(self):
        logging.info("Correct Answer")

        self.correct_tries += 1
        self.all_tries += 1

        self.window["LastAnswer"].update("Correct!")
        self.__common_answer()

    def __wrong_answer(self):
        logging.info("Wrong Answer")

        self.all_tries += 1

        self.window["LastAnswer"].update("Wrong!")
        self.__common_answer()

    def __common_answer(self):
        self.correct = IntervalGenerator.get_random_not_egdy_number()
        close_intervals = [self.correct.get_augmented_interval(), self.correct.get_diminished_interval()]
        incorrect = random.choice(close_intervals)

        options = [self.correct, incorrect]
        random.shuffle(options)

        self.correct_button = 'LeftAnswer' if options[0] == self.correct else 'RightAnswer'
        self.window['LeftAnswer'].update(options[0].get_interval_name())
        self.window['RightAnswer'].update(options[1].get_interval_name())

        self.window["AllTries"].update(self.all_tries)
        self.window["CorrectTries"].update(self.correct_tries)

    def __left_choosen(self):
        logging.debug("Left button clicked!")
        if self.correct_button == 'LeftAnswer':
            self.__correct_answer()
        else:
            self.__wrong_answer()

    def __right_choosen(self):
        logging.debug("Right button clicked!")
        if self.correct_button == 'RightAnswer':
            self.__correct_answer()
        else:
            self.__wrong_answer()
