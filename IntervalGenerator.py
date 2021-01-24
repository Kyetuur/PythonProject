import random
import Interval as Interval


def get_random_root():
    return random.choice(Interval.notes)


def get_random_interval_from_root(root):
    second_note = random.choice(Interval.notes)
    return Interval.Interval(root, second_note)


def get_random_interval():
    return get_random_interval_from_root(get_random_root())
