"""
This file implements the slowprint function.
"""

import sys
from time import sleep


def slowprint(text: str,  # pylint: disable=R0913
              interval: float = 0.02,
              end: str = "\n",
              end_interval: float = 0.5,
              fast: bool = False,
              char_count_interval: int = 1,
              by_word: bool = False) -> None:
    """
    Prints <text> slowly.

    :param text: The text to print
    :param interval: How many seconds to wait between each chunk
    :param end: The end. Default to \n
    :param end_interval: How many second to wait after everything is printed.
    :param fast: If true, print instantly.
    :param char_count_interval: How many character in each chunk. Default 1
    :param by_word: If true, char_count_interval is ignored and each word is a chunk. (split by ' ')
    :return: None
    """
    if fast:
        print(text, end=end)
    else:
        if by_word:
            words = text.split(" ")
            count = 0
            for word in words:
                sys.stdout.write(word)
                sys.stdout.write(" ")
                sys.stdout.flush()

                count += 1
                if count == char_count_interval:
                    sleep(interval)
                    count = 0
        else:
            count = 0
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()

                count += 1
                if count == char_count_interval:
                    sleep(interval)
                    count = 0

        sys.stdout.write(end)
        sleep(end_interval)
