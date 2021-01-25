import PySimpleGUI as SimpleGui
import logging
import IntervalGenerator as IntervalGenerator
import IntervalPlayer as IntervalPlayer
import IntervalComparer as IntComparer


class ChooseHigherModule:

    def __init__(self):
        self.first_interval = IntervalGenerator.get_random_interval()
        self.second_interval = IntervalGenerator.get_random_interval_from_root(self.first_interval.root)

        self.correct_tries = 0
        self.all_tries = 0
        self.window = None

    def run_module(self):
        layout = [[SimpleGui.Text('Choose higher interval')],
                  [SimpleGui.Text('_' * 100, size=(65, 1))],
                  [SimpleGui.Text('All tries: '), SimpleGui.Text(self.all_tries, size=(10, 1), key="AllTries")],
                  [SimpleGui.Text('Correct tries: '),
                   SimpleGui.Text(self.correct_tries, size=(10, 1), key="CorrectTries")],
                  [SimpleGui.Text('_' * 100, size=(65, 1))],
                  [SimpleGui.Button('Play Interval', size=(15, 1))],
                  [SimpleGui.Button('Left'), SimpleGui.Button('Same'), SimpleGui.Button('Right')],
                  [SimpleGui.Text('Last answer: '), SimpleGui.Text("", size=(10, 1), key="LastAnswer")],
                  [SimpleGui.Text('_' * 100, size=(65, 1))],
                  [SimpleGui.Button('Back to menu', size=(15, 1))]]

        # Create the Window
        self.window = SimpleGui.Window("ChooseHigher", layout, size=(400, 500), element_justification='c')

        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = self.window.read()
            if event == SimpleGui.WIN_CLOSED or event == 'Back to menu':
                break

            if event == 'Play Interval':
                IntervalPlayer.play_two_intervals(self.first_interval, self.second_interval)

            if event == 'Left' and IntComparer.check_if_first_greater(self.first_interval, self.second_interval):
                self.__correct_answer()

            elif event == 'Right' and IntComparer.check_if_first_greater(self.second_interval, self.first_interval):
                self.__correct_answer()

            elif event == 'Same' and IntComparer.check_if_are_same(self.first_interval, self.second_interval):
                self.__correct_answer()

            elif event == 'Right' or event == 'Left' or event == 'Same':
                self.__wrong_answer()

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

        self.window["AllTries"].update(self.all_tries)
        self.window["CorrectTries"].update(self.correct_tries)

        self.first_interval, self.second_interval = self.__get_new_intervals()

    @staticmethod
    def __get_new_intervals():
        first = IntervalGenerator.get_random_interval()
        second = IntervalGenerator.get_random_interval_from_root(first.root)
        return first, second
