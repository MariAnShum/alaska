import re
from pathlib import Path
from tinybear.csv_xls import read_dicts_from_csv, write_csv

from alaska.constants.paths import (
    FIRST_DIR_WITH_KODIAK_CHUNKS,
    FORMAL_DECIPHERING_MEASURE_RESULTS,
    SECOND_DIR_WITH_KODIAK_CHUNKS,
    DIR_WITH_NINILCHIK_CHUNKS,
    DIR_WITH_PRIBILOVS_AND_INTERIOR_CHUNKS,
)


def count_formal_deciphering_measure_in_chunks_and_write_metrics_into_result_table(
    input_dir_with_chunks: Path,
    output_file_for_measures: Path,
) -> None:

    files_to_process = input_dir_with_chunks.glob("*.csv")
    for filepath in files_to_process:

        fixed_syllables, missed_syllables = count_fixed_and_missed_syllables_in_one_chunk(
            filepath=filepath,
        )

        write_results_into_result_table(
            chunk_filename=filepath.name,
            collection_name=input_dir_with_chunks.name,
            fixed_syllables=fixed_syllables,
            missed_syllables=missed_syllables,
            table_filepath=output_file_for_measures,
        )


def count_fixed_and_missed_syllables_in_one_chunk(
    filepath: Path,
) -> tuple[int, int]:
    
    replies = read_dicts_from_csv(
        path_to_file=filepath,
        delimiter=";",
    )
    # I tried using read_one_column but perhaps it is intended for
    # comma delimiters only while my transcripts always use semicolon

    fixed_syllables = 0
    missed_syllables = 0

    for reply in replies:
        replica = reply["replica"]
        words = replica.split()
        for word in words:
            if "<" in word:
                try:
                    number_of_missed_syllables = int(re.sub("\D", "", word))
                    missed_syllables += number_of_missed_syllables
                except ValueError:
                    pass
                continue
            number_of_syllables = _count_syllables_in_one_word(word)
            fixed_syllables += number_of_syllables
    
    print(f"Succesfully count in {filepath.name}: {fixed_syllables=} and {missed_syllables=}")
    
    return (fixed_syllables, missed_syllables)


def write_results_into_result_table(
    chunk_filename: str,
    collection_name: str,
    fixed_syllables: int,
    missed_syllables: int,
    table_filepath=FORMAL_DECIPHERING_MEASURE_RESULTS,
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
        row["fixed_syllables"] = fixed_syllables
        row["missed_syllables"] = missed_syllables
        row["formal_deciphering_measure"] = formal_deciphering_measure(fixed_syllables, missed_syllables)
    
    if not found_this_chunk_in_table:
        print(f"Creating row for the new file {chunk_filename}.")
        new_row = {
            "collection_name": collection_name,
            "chunk_name": chunk_filename,
            "fixed_syllables": fixed_syllables,
            "missed_syllables": missed_syllables,
            "formal_deciphering_measure": formal_deciphering_measure(fixed_syllables, missed_syllables),
        }
        rows_of_resulting_table.append(new_row)

    write_csv(
        rows=rows_of_resulting_table,
        path_to_file=table_filepath,
        overwrite=True,
        delimiter=",",
    )


def _count_syllables_in_one_word(
    word: str,
) -> int:
    """
    На вход получает слово латиницей или кириллицей
    """
    frequent_irregular_words_in_lowercase_to_their_syllable_counts = {
        "evening": 2,
        "maybe": 2,
        "mr": 2,
        "mr.": 2,
        "mrs": 2,
        "mrs.": 2,
        "ms": 1,
        "ms.": 1,
        "russian": 1,
    }

    word = re.sub("\W|'", "", word.lower())

    if word in frequent_irregular_words_in_lowercase_to_their_syllable_counts.keys():
        return frequent_irregular_words_in_lowercase_to_their_syllable_counts[word]
    
    vowels = ['a', 'e', 'o', 'u', 'i', 'á', 'é', 'í', 'ó', 'ú', 'ý',
              'а', 'е', 'о', 'у', 'и', 'ы', 'я', 'ё', 'ю', 'э']
    previous_is_vowel = False  # Ложь здесь подразумевает, что слева или согласный, или начало строки
    previous_is_consonant_y = False  # Требуется только тогда, когда до 'y' замечен согласный (но не начало строки)
    syl = 0
    for i, char in enumerate(word):  # Проходится по каждой букве слова
        if char == 'e' and i == len(word) - 1:
            if syl == 0:
               syl += 1
        elif char in vowels:
            previous_is_consonant_y = False
            if not previous_is_vowel:
                syl += 1
            previous_is_vowel = True
        elif char == 'y':
            if not previous_is_vowel and i != 0:
                previous_is_consonant_y = True
            else:
                previous_is_vowel = False
                previous_is_consonant_y = False
        else:
            if previous_is_consonant_y:
                syl += 1
            previous_is_consonant_y = False
            previous_is_vowel = False
        """
        Итак, здесь 4 условия первого уровня:
        - Если последняя буква слова е и до нее гласных не было, то добавить 1.
            Ниже из всех слов с е на конце вычитается 1; текущий шаг позволяет учитывать слова типа he, she, the.
        - Если буква гласная: в любом случае отменить prev_is_y (на всякий случай)
        - - если до нее согласная или начало слова, то добавить 1, назначить previous_is_vowel
        - - если до нее гласная, то ничего не добавлять.
            Это позволяет считать дифтонги как 1 гласный
        - Если буква у:
        - - надо ставить prev_is_y исключительно в том случае, если до него идет согласный
        - Если буква согласная помимо у: в любом случае отменить previous_is_vowel
        - - если до нее идет у, то учесть у как гласный и отменить prev_is_y
        """
    if (word.startswith("some") and word != "some") or word.startswith("every") or (
            word.endswith("ed") and not word.endswith("ded") and not word.endswith("ted")) or (
            word.endswith("eteen")):
        syl -= 1
    if word.endswith("y") and (
            len(word) == 1 or word[-2] not in vowels):  # Окончание на Су рассматривается отдельно. Неудобно.
        syl += 1
    return syl


def formal_deciphering_measure(
    fixed_syllables: int,
    missed_syllables: int,
) -> float:
    
    return round(fixed_syllables / (fixed_syllables + missed_syllables), 2)


if __name__ == "__main__":
    count_formal_deciphering_measure_in_chunks_and_write_metrics_into_result_table(
        input_dir_with_chunks=FIRST_DIR_WITH_KODIAK_CHUNKS,
        output_file_for_measures=FORMAL_DECIPHERING_MEASURE_RESULTS,
    )
