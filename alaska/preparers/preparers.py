from pathlib import Path

from preparers.dir_preparer import prepare_dirs
from preparers.text_preparer import (
    remove_auxiliary_segments_from_file_and_count_missing_syllables,
    unify_diacritics
)
from preparers.get_frequencies_dict import get_frequencies_dict_with_capitals

from constants.paths import (
    DIR_WITH_OUTPUT_KODIAK_FILES,
    DIR_WITH_OUTPUT_NINILCHIK_FILES,
)


def preparers() -> None:
    prepare_dirs()
    for dir_to_open in [
        DIR_WITH_OUTPUT_KODIAK_FILES,
        DIR_WITH_OUTPUT_NINILCHIK_FILES,
    ]:
        for dir_of_interview_file in list(dir_to_open.iterdir()):
            input_filepath = list(dir_of_interview_file.glob("*.txt"))[0]
            working_filepath = dir_of_interview_file / "temporary" / input_filepath.name
            missing_syllables = remove_auxiliary_segments_from_file_and_count_missing_syllables(
                input_filepath=input_filepath,
                output_filepath=working_filepath,
                logging=False
            )
            formal_deciphering_report_file = (
                    Path(working_filepath).parent.parent / "discourse_reports" / "formal_deciphering_report.txt"
            )
            with open(
                    formal_deciphering_report_file,
                    "w",
                    encoding="utf-8"
            ) as f:
                f.write(str(missing_syllables))
            unify_diacritics(working_filepath)
            get_frequencies_dict_with_capitals(working_filepath)
