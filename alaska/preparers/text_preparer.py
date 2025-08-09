import re

from pathlib import Path
from tinybear.csv_xls import read_dicts_from_csv, write_csv

from alaska.constants.paths import (
    DIR_WITH_CHUNKS,
    FILE_WITH_PREPROCESSING_PATTERNS,
    FIRST_DIR_WITH_KODIAK_CHUNKS,
)

"""
This module should only be used with files converted from DOCS to MD and written as CSV tables.
Each CSV must have right structure: before you proceed, make sure that each reply resides
on its own line, that is no replies are 'glued' together into one line and no reply is split across
several lines. No replicas must contain semicolons because the semicolon is used as CSV delimiter.
Also, before you proceed you should manually replace &lt; with <, &gt; with >, &amp; with & and &nbsp;
with simple whitespace.

The module makes some replacements in texts: it eliminates symbols that are not necessary for further
work, 
"""

def prepare_chunks(
    input_dir_with_chunks: Path,
    output_dir_with_chunks: Path,
) -> None:

    chunks = input_dir_with_chunks.glob("*.csv")
    for chunk in chunks:

        remove_and_replace_extra_symbols_in_one_chunk(
            filepath=chunk,
            output_dir_with_chunks=output_dir_with_chunks,
        )
        add_column_for_reply_ids_and_fill_it_in_one_chunk(
            filepath=chunk,
            output_dir_with_chunks=output_dir_with_chunks,
        )


def remove_and_replace_extra_symbols_in_one_chunk(
    filepath: Path,
    output_dir_with_chunks: Path,
) -> None:
    
    """
    Find all unallowed symbols and do to them what is right -- either remove altogether
    or replace with allowed analogs. Correction is done on the basis of instruction
    made as a list of pairs of replacement -- "unallowed sumbol(s) to what they must
    be replaces with".
    Instruction is stored in inventories, in chunk_preprocessing_patterns.csv.

    List of symbols allowed in replicas:
    1. basic Latin alphabet,
    2. basic Cyrillic alphabet,
    3. angle brackets < and > with numbers inside them (no words allowed),
    4. numbers without brackets,
    5. apostrophe ',
    6. acute for denoting stress (Unicode 0301),
    7. final punctuation: full stop, question and exclamation marks, three dots,
    8. dash in complex words and interjections such as "uh-huh",
    9. underscore _, technical mark for denoting words written in italics.

    Some symbols are allowed exclusively in the rest of reply:
    1. semicolon acting as CSV delimiter,
    2. colon in timecodes.
    """
    
    replies = read_dicts_from_csv(
        path_to_file=filepath,
        delimiter=";",
    )
    patterns = read_dicts_from_csv(FILE_WITH_PREPROCESSING_PATTERNS)

    for pattern in patterns:
        for i in range(len(replies)):
            column_in_chunk_where_to_look_up = pattern["lookup_column"]
            replies[i][column_in_chunk_where_to_look_up] = re.sub(
                pattern=pattern["search"],
                repl=pattern["replace_with"],
                string=replies[i][column_in_chunk_where_to_look_up],
                )
    for reply in replies:
        if not reply["replica"]:
            replies.remove(reply)
    print(f"Successfully prepared replicas from file {filepath.name}")
            
    write_csv(
        rows=replies,
        path_to_file=output_dir_with_chunks / filepath.name,
        overwrite=True,
        delimiter=";",
    )

    print(f"Successfully written into {output_dir_with_chunks / filepath.name}")


def add_column_for_reply_ids_and_fill_it_in_one_chunk(
    filepath: Path,
    output_dir_with_chunks: Path,
):
    

    with open(filepath, "r") as f:
        header_and_rows = [line for line in f]

    header_and_rows[0] = "id;speaker_code;time_code;replica\n"

    for i in range(1, len(header_and_rows)):
        header_and_rows[i] = f"{i};{header_and_rows[i]}"

    with open(output_dir_with_chunks / filepath.name,"w") as f:
        for line in header_and_rows:
            f.write(line)


if __name__ == "__main__":
    prepare_chunks(
        input_dir_with_chunks=FIRST_DIR_WITH_KODIAK_CHUNKS,
        output_dir_with_chunks=FIRST_DIR_WITH_KODIAK_CHUNKS,
    )
