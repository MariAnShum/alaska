import re
from pathlib import Path

from alaska.constants.paths import DIR_WITH_CHUNKS


def lint_chunks(
    input_dir_with_chunks=DIR_WITH_CHUNKS,
    output_dir_with_chunks=DIR_WITH_CHUNKS,
) -> None:

    files_to_process = input_dir_with_chunks.glob("*.docx")
    for file in files_to_process:

        lint_chunk(file)


def lint_chunk(file: Path) -> None:
    pass


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
