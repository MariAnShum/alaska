import re
from pathlib import Path


def remove_auxiliary_segments_from_file_and_count_missing_syllables(
        input_filepath: Path,
        output_filepath: Path,
        logging: bool = True,
) -> int:
    with open(input_filepath, "r", encoding="utf-8") as f:
        data_from_file = f.read()
    data_from_file, missing_syllables_counter = _extract_missing_syllables(data_from_file)
    segments_to_remove = {
        r"\*[\s0-9a-zA-Z  а-яА-ЯёЁ.;,:?/]+\*": "Removing commentary",
        r"<[\s0-9a-zA-Z  а-яА-ЯёЁ.;,:?/]+>": "Removing commentary in angle brackets",
        r"\(.{,5}\)": "Removing discourse markers in round brackets",
        r"\{.*}": "Removing sequences in figure brackets",
        r"\w*'?\w*={1,3}": "Removing false-starts and corrections",
        r"\d?\d:\d\d": "Removing timecodes",
        r"(Ir|Rt)\d?:?": "Removing locutor codes",
        r"(:|;)?\d+": "Removing numbers",
        r"[а-яА-ЯёЁ]+": "Removing Cyrillic words",
        r"[.…,;:?!|–—\[\]]": "Finally, removing punctuation marks and square brackets",
    }
    for expression in segments_to_remove:
        if logging:
            print(segments_to_remove[expression])
        data_from_file = re.sub(re.compile(expression, flags=re.MULTILINE), "", data_from_file)
    data_from_file = _remove_extra_spaces(data_from_file)
    data_from_file = _remove_extra_space_at_start(data_from_file)
    with open(output_filepath, "w", encoding="utf-8") as f:
        f.write(data_from_file)
    return missing_syllables_counter


def unify_diacritics(
        filepath: Path
) -> None:
    with open(filepath, "r", encoding="utf-8") as f:
        data_from_file = f.read()
    data_from_file = _unify_apostrophes(data_from_file)
    data_from_file = _make_all_stresses_separate_from_vowels(data_from_file)
    data_from_file = _remove_extra_symbols_at_all(data_from_file)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(data_from_file)


def _unify_apostrophes(
        data_from_file: str,
) -> str:
    apostrophe_like_symbols = ["ʼ", "’", "ˮ", "՚", "＇", "‘"]
    for symbol in apostrophe_like_symbols:
        data_from_file = data_from_file.replace(symbol, "'")
    return data_from_file


def _make_all_stresses_separate_from_vowels(
        data_from_file: str,
) -> str:
    single_to_double = {
        "á": "á",
        "é": "é",
        "í": "í",
        "ó": "ó",
        "ú": "ú",
        "Á": "Á",
        "É": "É",
        "Í": "Í",
        "Ó": "Ó",
        "Ú": "Ú",
    }
    for key in single_to_double:
        data_from_file = data_from_file.replace(key, single_to_double[key])
    data_from_file = data_from_file.replace("̇", "")
    return data_from_file


def _remove_extra_symbols_at_all(
        data_from_file: str,
) -> str:
    symbols_to_remove = ["͘", "̇", "«", "»", "“", "”", "\"", "„", "“"]
    for symbol in symbols_to_remove:
        data_from_file = data_from_file.replace(symbol, "")
    return data_from_file


def _remove_extra_spaces(
        data_from_file: str,
) -> str:
    data_from_file = re.sub(re.compile(r"\s{2,}|\n"), " ", data_from_file)
    data_from_file = re.sub(re.compile(r"\t"), " ", data_from_file)
    return data_from_file


def _remove_extra_space_at_start(
        data_from_file: str,
) -> str:
    data_from_file = re.sub(re.compile(r"^\s+", flags=re.MULTILINE), "", data_from_file)
    return data_from_file


def _extract_missing_syllables(
        data_from_file: str,
):
    missing_syllables_counter = 0
    missing_syllables = re.findall(re.compile(r"<\d>"), data_from_file)
    for item in missing_syllables:
        item = item.replace("<", "")
        item = item.replace(">", "")
        missing_syllables_counter += int(item)
    data_from_file = re.sub(re.compile(r"<\d>"), "", data_from_file)
    return data_from_file, missing_syllables_counter
