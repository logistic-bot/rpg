"""
This file implements the slowinput function.
"""

from src.core.utils.slowprint import slowprint


def slowinput(text: str,
              interval: float = 0.03,
              end: str = "",
              end_interval: float = 0,
              fast: bool = False) -> str:
    """
    This functions call slowprint with all provided arguments, then calls input() and return the
    result. For all parameters, see slowprint()
    """
    slowprint(text, interval, end, end_interval, fast)
    return input()
