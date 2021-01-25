import pytest
import Interval as Interval

notes_number_from_C = [('C', 0),
                       ('C#', 1),
                       ('D', 2),
                       ('D#', 3),
                       ('E', 4),
                       ('F', 5),
                       ('F', 6),
                       ('G', 7),
                       ('G#', 8),
                       ('A', 9),
                       ('A#', 10),
                       ('B', 11)]

notes_number_from_B = [('B', 0),
                       ('A#', 1),
                       ('A', 2),
                       ('G#', 3),
                       ('G', 4),
                       ('F#', 5),
                       ('F', 6),
                       ('E', 7),
                       ('D#', 8),
                       ('D', 9),
                       ('C#', 10),
                       ('C', 11)]


@pytest.mark.parametrize("second,distance", notes_number_from_C)
def test_distance_increasing(second, distance):
    root = 'C'
    unison = Interval.Interval(root, second)
    assert unison.get_interval_number() == distance


@pytest.mark.parametrize("second,distance", notes_number_from_B)
def test_distance_increasing(second, distance):
    root = 'B'
    unison = Interval.Interval(root, second)
    assert unison.get_interval_number() == distance


def test_diminished_unison_should_raise_error():
    with pytest.raises(ValueError):
        unison = Interval.Interval('C', 'C')
        unison.get_diminished_interval()


def test_augmented_out_of_actave_should_raise_error():
    with pytest.raises(ValueError):
        interval = Interval.Interval('C', 'B')
        interval.get_augmented_interval()


c_intervals_with_dimished_and_augmented = [
    ('C', 'C', None, None, 'C#', 1),
    ('C', 'C#', 'C', 0, 'D', 2),
    ('C', 'D', 'C#', 1, 'D#', 3),
    ('C', 'D#', 'D', 2, 'E', 4),
    ('C', 'E', 'D#', 3, 'F', 5),
    ('C', 'F', 'E', 4, 'F#', 6),
    ('C', 'F#', 'F', 5, 'G', 7),
    ('C', 'G', 'F#', 6, 'G#', 8),
    ('C', 'G#', 'G', 7, 'A', 9),
    ('C', 'A', 'G#', 8, 'A#', 10),
    ('C', 'A#', 'A', 9, 'B', 11),
    ('C', 'B', 'A#', 10, None, None)]


@pytest.mark.parametrize('note,second,dimished_second,dimished_number,_a,_b', c_intervals_with_dimished_and_augmented)
def test_diminished_increasing(note, second, dimished_second, dimished_number, _a, _b):
    inter = Interval.Interval(note, second)
    if note == second:
        return

    dimished = inter.get_diminished_interval()
    assert dimished.secondNote == dimished_second
    assert dimished.get_interval_number() == dimished_number


@pytest.mark.parametrize('note,second,_a,_b,augmented_second,augmented_number',
                         c_intervals_with_dimished_and_augmented)
def test_augmented_increasing(note, second, _a, _b, augmented_second, augmented_number):
    inter = Interval.Interval(note, second)
    if inter.secondNote == 'B':
        return

    augmented = inter.get_augmented_interval()
    assert augmented.secondNote == augmented_second
    assert augmented.get_interval_number() == augmented_number


def test_decreasing_diminished_should_raise():
    with pytest.raises(ValueError):
        interval = Interval.Interval('B', 'A#')
        interval.get_diminished_interval()


def test_decreasing_augmented_should_raise():
    with pytest.raises(ValueError):
        interval = Interval.Interval('B', 'A#')
        interval.get_augmented_interval()


notes_with_bemols = [('A', 'G#'),
                     ('A#', 'A'),
                     ('B', 'A#'),
                     ('C', 'B'),
                     ('C#', 'C'),
                     ('D', 'C#'),
                     ('D#', 'D'),
                     ('E', 'D#'),
                     ('F', 'E'),
                     ('F#', 'F'),
                     ('G', 'F#'),
                     ('G#', 'G')]


@pytest.mark.parametrize("note,bemol", notes_with_bemols)
def test_bemol(note, bemol):
    assert Interval.get_bemol(note) == bemol

@pytest.mark.parametrize("note,bemol", notes_with_bemols)
def test_sharp(note,bemol):
    assert Interval.get_sharp(bemol) == note
