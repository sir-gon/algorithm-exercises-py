import logging

LOGGER = logging.getLogger(__name__)


def time_conversion(_s: str) -> str:
    meridian = _s[-2:]
    meridian = meridian.lower()

    time_str = _s[0:len(_s) - 2]
    time = time_str.split(':')
    hour = int(time[0])

    if hour >= 12:
        hour = 0

    if meridian == 'pm':
        hour += 12

    time[0] = str(hour).rjust(2, '0')
    conversion = ':'.join(time)

    return conversion
