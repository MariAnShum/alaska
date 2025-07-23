import re

from typing import Path

from alaska.constants.paths import DIR_WITH_CHUNKS


def validate() -> None:
    
    for path_to_chunk in list(DIR_WITH_CHUNKS.glob("*.csv")):
        validate_one_chunk(path_to_chunk)


def validate_one_chunk(
    path_to_chunk: Path,
) -> None:
    pass


def validate_symbols_in_text(
    path_to_chunk: Path,
) -> None:
    """
    In transcripts and chunks, only the following symbols are allowed:

    - basic Latin and Cyrillic letters,
    - ordinary white spaces (not non-breaking ones),
    - full stop, three dots, question mark,
    - single scare quote ',
    - stress mark above a vowel (Unicode 0301),
    - angle brackets with numbers inside (missed syllables counts),
    - hyphens -,
    - colons in timecodes,
    - and semicolons as CSV columns delimiters.

    All the other symbols must be deleted or replaced by more appropriate ones.
    A major part of work is done by the script in text_preparer, but some detais must be fixed
    manually. This validator serves to detect such cases.
    """

