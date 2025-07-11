import re
from copy import deepcopy
from pathlib import Path
from tinybear.csv_xls import read_dicts_from_csv, write_csv

from alaska.constants.paths import DIR_WITH_CHUNKS, FILE_WITH_PREPROCESSING_PATTERNS


def prepare_chunks(
    input_dir_with_chunks=DIR_WITH_CHUNKS,
    output_dir_with_chunks=DIR_WITH_CHUNKS,
) -> None:

    files_to_process = input_dir_with_chunks.glob("*.csv")
    for file in files_to_process:

        prepare_one_chunk(
            file=file,
            output_dir_with_chunks=output_dir_with_chunks,
        )


def prepare_one_chunk(
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
            copied_replies[i][pattern["lookup_column"]] = re.sub(
                pattern=pattern["search"],
                repl=pattern["replace_with"],
                string=copied_replies[i][pattern["lookup_column"]],
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
