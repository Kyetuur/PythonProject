import random
import Interval as Interval
import logging

logger = logging.getLogger(name="IntervalGenerator")


def get_random_root():
    root = random.choice(Interval.notes)
    logger.debug(f"Get random root returned {root}")

    return root


def get_random_interval_from_root(root):
    second_note = random.choice(Interval.notes)
    interval = Interval.Interval(root, second_note)

    logger.debug(f"Get random interval from root returned {interval}")
    return interval


def get_random_interval():
    random_interval =  get_random_interval_from_root(get_random_root())
    logger.debug(f"Get random interval {random_interval}")
    return random_interval


def get_random_increasing_interval():
    interval = get_random_interval()
    while not interval.check_if_increasing():
        logger.debug(f"Rerolling interval, current {interval}")
        interval = get_random_interval()

    logger.debug(f"Get random increasing returned {interval}")
    return interval


def get_random_not_egdy_number():
    interval = get_random_increasing_interval()
    while interval.get_interval_number() == 0 or interval.secondNote == 'B':
        interval = get_random_increasing_interval()

    logger.debug(f"Get random not edgy {interval}")
    return interval
