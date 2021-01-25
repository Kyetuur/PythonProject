
import Interval as Interval

def build_major_scale_on_root(root):
        yield root
        yield Interval.notes[(Interval.notes.index(root) + 2) % len(Interval.notes)]
        yield Interval.notes[(Interval.notes.index(root) + 4) % len(Interval.notes)]
        yield Interval.notes[(Interval.notes.index(root) + 5) % len(Interval.notes)]
        yield Interval.notes[(Interval.notes.index(root) + 7) % len(Interval.notes)]
        yield Interval.notes[(Interval.notes.index(root) + 9) % len(Interval.notes)]
        yield Interval.notes[(Interval.notes.index(root) + 11) % len(Interval.notes)]
        yield Interval.notes[(Interval.notes.index(root) + 12) % len(Interval.notes)]


def build_minor_scale_on_root(root):
        yield root
        yield Interval.notes[(Interval.notes.index(root) + 2) % len(Interval.notes)]
        yield Interval.notes[(Interval.notes.index(root) + 3) % len(Interval.notes)]
        yield Interval.notes[(Interval.notes.index(root) + 5) % len(Interval.notes)]
        yield Interval.notes[(Interval.notes.index(root) + 7) % len(Interval.notes)]
        yield Interval.notes[(Interval.notes.index(root) + 8) % len(Interval.notes)]
        yield Interval.notes[(Interval.notes.index(root) + 10) % len(Interval.notes)]
        yield Interval.notes[(Interval.notes.index(root) + 12) % len(Interval.notes)]