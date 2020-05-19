from unittest.mock import patch

from hypothesis import given, assume, settings
from hypothesis.strategies import text, decimals, integers, booleans

from src.core.utils.slowprint import slowprint


@given(t=text(), interval=decimals(max_value=1, allow_infinity=False, allow_nan=False), end=text(),
       end_interval=decimals(
           max_value=1, allow_infinity=False, allow_nan=False, min_value=0),
       fast=booleans(),
       char_count_interval=integers(), by_word=booleans())
@settings(deadline=3000)  # the deadline is in milliseconds, so this is 3 seconds
def test_slowprint(t, interval, end, end_interval, fast, char_count_interval,
                   by_word):
    assume(end_interval > float("-Infinity"))
    slowprint(t, interval, end, end_interval, fast, char_count_interval, by_word)
