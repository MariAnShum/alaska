import logging
import pandas as pd
import re

from pathlib import Path


logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class InvalidTimecodeError(Exception):
    pass


class ChunkValidator:
    def __init__(
        self,
        dir_with_chunks: Path,
    ):
        self.chunks = sorted(list(dir_with_chunks.glob("*.csv")))
        self.logger = logging.getLogger()
        self.chunk_collection = dir_with_chunks.name


    def validate(self):
        self.logger.info(f"\nChecking chunks ({len(self.chunks)} files) in {self.chunk_collection} collection")
        for chunk in self.chunk:
            self.validate_one_file(chunk)
    

    def validate_one_file(self):
        pass

def check_timecodes(rows):
    """
    Check if all timecodes correspond to format (\d?\d\:)?\d\d:\d\d or are None.
    This helps to detect cases where timecode and repica are not separated by semicolon for some reason.
    """
    pass

"""
One of the checks must be that CSV has excatly three columns.
"""
