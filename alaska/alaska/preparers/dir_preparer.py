from pathlib import Path

from alaska.constants.paths import (
    DIR_WITH_INPUT_KODIAK_FILES,
    DIR_WITH_INPUT_NINILCHIK_FILES,
    DIR_WITH_OUTPUT_KODIAK_FILES,
    DIR_WITH_OUTPUT_NINILCHIK_FILES,
)


DIRS_PAIRS = {
    DIR_WITH_INPUT_KODIAK_FILES: DIR_WITH_OUTPUT_KODIAK_FILES,
    DIR_WITH_INPUT_NINILCHIK_FILES: DIR_WITH_OUTPUT_NINILCHIK_FILES
}


def dir_preparer() -> None:
    for dirs_pair in DIRS_PAIRS.items():
        for filepath in dirs_pair[0].glob("*.txt"):
            filename = filepath.stem
            dir_for_file_in_output = dirs_pair[1] / filename
            dir_for_file_in_output.mkdir(exist_ok=True)
            _copy_file_from_input_to_output(
                input_filepath=filepath,
                output_dir=dir_for_file_in_output
            )
            discourse_reports_dir = dir_for_file_in_output / "discourse_reports"
            alaska_reports_dir = dir_for_file_in_output / "alaska_reports"
            frequency_reports_dir = alaska_reports_dir / "frequency_reports"
            temporary_files_dir = dir_for_file_in_output / "temporary"
            for dir_to_create in [
                discourse_reports_dir, alaska_reports_dir, frequency_reports_dir, temporary_files_dir
            ]:
                dir_to_create.mkdir(exist_ok=True)


def _copy_file_from_input_to_output(
        *,
        input_filepath: Path,
        output_dir: Path,
) -> None:
    with open(input_filepath, "r", encoding="utf-8") as f:
        lines = []
        for line in f:
            lines.append(line)
    with open(output_dir / input_filepath.name, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
