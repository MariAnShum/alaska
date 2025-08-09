import re

from pathlib import Path
from tinybear.csv_xls import read_dicts_from_csv, write_csv

from alaska.constants.paths import (
    DIR_WITH_INVENTORIES,
    FIRST_DIR_WITH_KODIAK_CHUNKS,
    LEXICAL_DECIPHERING_MEASURE_RESULTS,
    SECOND_DIR_WITH_KODIAK_CHUNKS,
    DIR_WITH_NINILCHIK_CHUNKS,
    DIR_WITH_PRIBILOVS_AND_INTERIOR_CHUNKS,
)

FILE_WITH_STOPWORDS = DIR_WITH_INVENTORIES / "stopwords.txt"
list_of_stop_words = []
with open(FILE_WITH_STOPWORDS, "r") as f:
    for line in f:
        list_of_stop_words.append(line[:-1]) # Remove \n at the end of each word


def count_lexical_deciphering_measure_in_chunks_and_write_metrics_into_result_table(
    input_dir_with_chunks: Path,
    output_file_for_measures: Path,
) -> None:

    files_to_process = input_dir_with_chunks.glob("*.csv")
    for filepath in files_to_process:

        key_words, stop_words = count_key_and_stop_words_in_one_chunk(
            filepath=filepath,
        )

        write_results_into_result_table(
            chunk_filename=filepath.name,
            collection_name=input_dir_with_chunks.name,
            key_words=key_words,
            stop_words=stop_words,
            table_filepath=output_file_for_measures,
        )


def count_key_and_stop_words_in_one_chunk(
    filepath: Path,
) -> tuple[int, int]:
    
    replies = read_dicts_from_csv(
        path_to_file=filepath,
        delimiter=";",
    )
    # I tried using read_one_column but perhaps it is intended for
    # comma delimiters only while my transcripts always use semicolon

    key_words = 0
    stop_words = 0

    for reply in replies:
        replica = reply["replica"]
        words = replica.split()
        for word in words:
            if word in list_of_stop_words:
                stop_words += 1
                continue

            key_words += 1
    
    print(f"Succesfully count in {filepath.name}: {key_words=} and {stop_words=}")
    
    return (key_words, stop_words)


def write_results_into_result_table(
    chunk_filename: str,
    collection_name: str,
    key_words: int,
    stop_words: int,
    table_filepath=LEXICAL_DECIPHERING_MEASURE_RESULTS,
) -> None:
    
    rows_of_resulting_table = read_dicts_from_csv(
            path_to_file=table_filepath,
            delimiter=",",
        )
    
    found_this_chunk_in_table = False

    for row in rows_of_resulting_table:
        if row["chunk_name"] != chunk_filename:
            continue
        found_this_chunk_in_table = True
        print(f"Filename {chunk_filename} already exists in table. Updating metrics.")
        row["key_words"] = key_words
        row["stop_words"] = stop_words
        row["lexical_deciphering_measure"] = lexical_deciphering_measure(key_words, stop_words)
    
    if not found_this_chunk_in_table:
        print(f"Creating row for the new file {chunk_filename}.")
        new_row = {
            "collection_name": collection_name,
            "chunk_name": chunk_filename,
            "key_words": key_words,
            "stop_words": stop_words,
            "lexical_deciphering_measure": lexical_deciphering_measure(key_words, stop_words),
        }
        rows_of_resulting_table.append(new_row)

    write_csv(
        rows=rows_of_resulting_table,
        path_to_file=table_filepath,
        overwrite=True,
        delimiter=",",
    )


def lexical_deciphering_measure(
    key_words: int,
    stop_words: int,
) -> float:
    
    return round(key_words / (key_words + stop_words), 2)


if __name__ == "__main__":
    count_lexical_deciphering_measure_in_chunks_and_write_metrics_into_result_table(
        input_dir_with_chunks=FIRST_DIR_WITH_KODIAK_CHUNKS,
        output_file_for_measures=LEXICAL_DECIPHERING_MEASURE_RESULTS,
    )
