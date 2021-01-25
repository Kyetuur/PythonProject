import musicalbeeps
import logging

logger = logging.getLogger(name="Player")

player = musicalbeeps.Player(volume=0.3, mute_output=True)


def play_interval(interval):
    logger.info(interval)
    player.play_note(interval.root, 0.5)
    player.play_note(interval.secondNote, 0.5)


def play_two_intervals(first_interval, second_interval):
    play_interval(first_interval)
    player.play_note("pause", 0.5)
    play_interval(second_interval)
