from hypothesis import given, settings, example
from hypothesis.strategies import text, decimals, integers, booleans

from src.core.utils.slowprint import slowprint


@given(t=text(), interval=decimals(max_value=1, allow_infinity=False, allow_nan=False,
                                   min_value=0),
       end=text(),
       end_interval=decimals(
           max_value=1, allow_infinity=False, allow_nan=False, min_value=0),
       fast=booleans(),
       char_count_interval=integers(), by_word=booleans())
@settings(deadline=3000)  # the deadline is in milliseconds, so this is 3 seconds
@example("This is three words. (no, way more than that)", 0, "\n", 0, False, 1, True)
@example("This is three words. (no, way more than that)", 0, "\n", 0, False, 1, False)
def test_slowprint(t, interval, end, end_interval, fast, char_count_interval,
                   by_word):
    slowprint(t, interval, end, end_interval, fast, char_count_interval, by_word)
