from pathlib import Path

from processing.discourse_analysis.formal_deciphering import (
    get_number_of_deciphered_syllables,
    fill_formal_deciphering_report,
)

from processing.discourse_analysis.lexical_deciphering import (
    get_lexical_deciphering_measure,
    fill_lexical_deciphering_report,
)

from constants.paths import (
    DIR_WITH_OUTPUT_KODIAK_FILES,
    DIR_WITH_OUTPUT_NINILCHIK_FILES,
)


def discourse_analysis() -> None:
    for dir_to_open in [
        DIR_WITH_OUTPUT_KODIAK_FILES,
        DIR_WITH_OUTPUT_NINILCHIK_FILES,
    ]:
        for dir_of_interview_file in list(dir_to_open.iterdir()):
            filepath = dir_of_interview_file / "temporary" / "frequencies_of_all_words.txt"
            deciphered_syllables = get_number_of_deciphered_syllables(
                Path(filepath)
            )
            formal_deciphering_report_file = Path(
                filepath).parent.parent / "discourse_reports" / "formal_deciphering_report.txt"
            fill_formal_deciphering_report(
                deciphered_syllables=deciphered_syllables,
                formal_deciphering_report_file=formal_deciphering_report_file,
            )
            total_words_counter, key_words_counter = get_lexical_deciphering_measure(filepath)
            lexical_deciphering_report_file = Path(
                filepath).parent.parent / "discourse_reports" / "lexical_deciphering_report.txt"
            fill_lexical_deciphering_report(
                total_words_counter=total_words_counter,
                key_words_counter=key_words_counter,
                lexical_deciphering_report_file=lexical_deciphering_report_file,
            )