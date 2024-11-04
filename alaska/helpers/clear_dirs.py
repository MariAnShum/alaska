import pathlib

from alaska.constants.paths import DIR_WITH_OUTPUT_KODIAK_FILES, DIR_WITH_OUTPUT_NINILCHIK_FILES

SUPERDIRS = [
        DIR_WITH_OUTPUT_KODIAK_FILES,
        DIR_WITH_OUTPUT_NINILCHIK_FILES
    ]


def clear_output_dirs():
    clear_reports_in_all_dirs()
    clear_temporary_files_in_all_dirs()
    delete_copied_transcripts_in_all_dirs()

    for superdir in SUPERDIRS:
        for subdir in superdir.iterdir():
            contents = [
                subdir / "alaska_reports" / "frequency_reports",
                subdir / "alaska_reports",
                subdir / "discourse_reports",
                subdir / "temporary"
            ]
            for subsubdir in contents:
                subsubdir.rmdir()
            subdir.rmdir()

def clear_all_except_reports_in_all_dirs():
    clear_temporary_files_in_all_dirs()
    delete_copied_transcripts_in_all_dirs()

    for superdir in SUPERDIRS:
        for subdir in superdir.iterdir():
            (subdir / "temporary").rmdir()

def clear_reports_in_all_dirs():
    for superdir in SUPERDIRS:
        for subdir in superdir.iterdir():
            for file in (subdir / "discourse_reports").iterdir():
                file.unlink()
    # When alaskan module is ready, include deletion of its files here

def clear_temporary_files_in_all_dirs():
    for superdir in SUPERDIRS:
        for subdir in superdir.iterdir():
            for file in (subdir / "temporary").iterdir():
                file.unlink()

def delete_copied_transcripts_in_all_dirs():
    for superdir in SUPERDIRS:
        for subdir in superdir.iterdir():
            for file in list(subdir.glob("*.txt")):
                file.unlink()

clear_output_dirs()
