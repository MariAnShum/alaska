from pathlib import Path


def get_number_of_deciphered_syllables(
        filepath: Path,
) -> int:
    with open(filepath, "r", encoding="utf-8") as f:
        frequencies_dict = {}
        for line in f:
            word, counter = line.split("\t")
            word = word.replace(":", "")
            counter = counter.replace("\n", "")
            frequencies_dict[word] = counter
    syllables_in_words = {}
    total_deciphered_counter = 0
    for key in frequencies_dict:
        syllables_in_word = _count_syl(key)
        syllables_in_words[key] = syllables_in_word
        total_deciphered_counter += syllables_in_word*int(frequencies_dict[key])
    syllables_in_words = sorted(syllables_in_words.items(), key=lambda x: x[1], reverse=True)
    with open(filepath.parent / "syllables_of_all_latin_words.txt", "w", encoding="utf-8") as f:
        for item in syllables_in_words:
            f.write(f"{item[0]}:\t{item[1]}\n")
    return total_deciphered_counter


def _count_syl(w):
    """
    На вход получает слово латиницей
    """
    w = w.lower()
    vowels = ['a', 'e', 'o', 'u', 'i', 'á', 'é', 'í', 'ó', 'ú', 'ý',
              'а', 'е', 'о', 'у', 'и', 'ы', 'я', 'ё', 'ю', 'э']
    previous_is_vowel = False  # Ложь здесь подразумевает, что слева или согласный, или начало строки
    previous_is_consonant_y = False  # Требуется только тогда, когда до 'y' замечен согласный (но не начало строки)
    syl = 0
    for i, char in enumerate(w):  # Проходится по каждой букве слова
        if char == '́':
            pass
        elif char == 'e' and i == len(w) - 1:
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
        Итак, здесь 5 условий первого уровня:
        - знак ударения игнорировать.
        - если последняя буква слова е и до нее гласных не было, то добавить 1.
            Ниже из всех слов с е на конце вычитается 1; текущий шаг позволяет учитывать слова типа he, she, the.
        - если буква гласная: в любом случае отменить prev_is_y (на всякий случай)
        - - если до нее согласная или начало слова, то добавить 1, назначить previous_is_vowel
        - - если до нее гласная, то ничего не добавлять.
            Это позволяет считать дифтонги как 1 гласный
        - если буква у:
        - - надо ставить prev_is_y исключительно в том случае, если до него идет согласный
        - если буква согласная помимо у: в любом случае отменить previous_is_vowel
        - - если до нее идет у, то учесть у как гласный и отменить prev_is_y
        """
    if (w.startswith("some") and w != "some") or w.startswith("every") or (
            w.endswith("ed") and not w.endswith("ded") and not w.endswith("ted")):
        syl -= 1
    if w.endswith("y") and (
            len(w) == 1 or w[-2] not in vowels):  # Окончание на Су рассматривается отдельно. Неудобно.
        syl += 1
    return syl


def fill_formal_deciphering_report(
        deciphered_syllables: int,
        formal_deciphering_report_file: Path,
) -> None:
    with open(
            formal_deciphering_report_file,
            "r",
            encoding="utf-8",
    ) as f:
        missing_syllables = int(f.read().replace("\n", ""))
    formal_deciphering_measure = round(deciphered_syllables / (missing_syllables + deciphered_syllables), 2)
    with open(
            formal_deciphering_report_file,
            "w",
            encoding="utf-8",
    ) as f:
        f.write(f"Deciphered syllables:\t{deciphered_syllables}\n")
        f.write(f"Missing syllables:\t{missing_syllables}\n")
        f.write(f"FDM:\t{formal_deciphering_measure}\n")
