notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'G', 'G#', 'A', 'A#', 'B']
intervalNames = {
    0: 'unison',
    1: 'minor second',
    2: 'major second',
    3: 'minor third',
    4: 'major third',
    5: 'perfect fourth',
    6: 'tritone',
    7: 'perfect fifth',
    8: 'minor sixth',
    9: 'major sixth',
    10: 'minor seventh',
    11: 'major seventh',
    12: 'perfect octave',
}


class Interval:
    def __init__(self, root, secondNote):
        self.root = root
        self.secondNote = secondNote

    def get_interval_number(self):
        return abs(notes.index(self.secondNote) - notes.index(self.root))

    def get_interval_name(self):
        return intervalNames[self.get_interval_number()]

    def __str__(self):
        if notes.index(self.root) < notes.index(self.secondNote):
            return f'''Notes ({self.root}, {self.secondNote}) : {self.get_interval_name()} | Increasing'''
        else:
            return f'''Notes ({self.secondNote}, {self.root}) : {self.get_interval_name()} | Decreasing'''
