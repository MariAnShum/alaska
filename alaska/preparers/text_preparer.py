import re
from copy import deepcopy
from pathlib import Path
from tinybear.csv_xls import read_dicts_from_csv, write_csv

from alaska.constants.paths import (
    DIR_WITH_CHUNKS,
    FILE_WITH_PREPROCESSING_PATTERNS,
    FIRST_DIR_WITH_KODIAK_CHUNKS,
)


def prepare_chunks(
    input_dir_with_chunks: Path,
    output_dir_with_chunks: Path,
) -> None:

    files_to_process = input_dir_with_chunks.glob("*.csv")
    for filepath in files_to_process:

        remove_and_replace_extra_symbols_in_one_chunk(
            filepath=filepath,
            output_dir_with_chunks=output_dir_with_chunks,
        )
        add_column_for_reply_ids_and_fill_it_in_one_chunk(
            filepath=filepath,
            output_dir_with_chunks=output_dir_with_chunks,
        )


def remove_and_replace_extra_symbols_in_one_chunk(
    filepath: Path,
    output_dir_with_chunks: Path,
) -> None:
    
    replies = read_dicts_from_csv(
        path_to_file=filepath,
        delimiter=";",
    )
    patterns = read_dicts_from_csv(FILE_WITH_PREPROCESSING_PATTERNS)

    copied_replies = deepcopy(replies)

    for pattern in patterns:
        for i in range(len(copied_replies)):
            column_in_chunk_where_to_look_up = pattern["lookup_column"]
            copied_replies[i][column_in_chunk_where_to_look_up] = re.sub(
                pattern=pattern["search"],
                repl=pattern["replace_with"],
                string=copied_replies[i][column_in_chunk_where_to_look_up],
                )
    for reply in copied_replies:
        if not reply["replica"]:
            copied_replies.remove(reply)
    print(f"Successfully prepared replicas from file {filepath.name}")
            
    write_csv(
        rows=copied_replies,
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


# def make_all_stresses_and_their_vowels_united_symbols(
#         data_from_file: str,
# ) -> str:
#     double_to_single = {
#         "á": "á",
#         "é": "é",
#         "í": "í",
#         "ó": "ó",
#         "ú": "ú",
#         "Á": "Á",
#         "É": "É",
#         "Í": "Í",
#         "Ó": "Ó",
#         "Ú": "Ú",
#     }
#     for key in double_to_single:
#         data_from_file = data_from_file.replace(key, double_to_single[key])
#     data_from_file = data_from_file.replace("̇", "")
#     return data_from_file


if __name__ == "__main__":
    prepare_chunks(
        input_dir_with_chunks=FIRST_DIR_WITH_KODIAK_CHUNKS,
        output_dir_with_chunks=FIRST_DIR_WITH_KODIAK_CHUNKS,
    )
