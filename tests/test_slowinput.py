from hypothesis import given, settings, example
from hypothesis.strategies import text, decimals, integers, booleans

import src.core.utils.slowinput


@given(t=text(), interval=decimals(max_value=1, allow_infinity=False, allow_nan=False,
                                   min_value=0),
       end=text(),
       end_interval=decimals(
           max_value=1, allow_infinity=False, allow_nan=False, min_value=0),
       fast=booleans(),
       char_count_interval=integers(), by_word=booleans(), inp=text())
@settings(deadline=3000)  # the deadline is in milliseconds, so this is 3 seconds
@example("This is three words. (no, way more than that)", 0, "\n", 0, False, 1, True, "ANOTHER")
@example("This is three words. (no, way more than that)", 0, "\n", 0, False, 1, False, "TEST")
def test_slowinput(t, interval, end, end_interval, fast, char_count_interval,
                   by_word, inp):
    src.core.utils.slowinput.input = lambda: inp
    src.core.utils.slowinput.slowinput(t, interval, end, end_interval, fast, char_count_interval,
                                       by_word)
