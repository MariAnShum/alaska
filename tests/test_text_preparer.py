from alaska.preparers.text_preparer import prepare_one_chunk
from tests.helpers import check_existence_of_output_csv_file_and_compare_with_gold_standard
from tests.paths import (
    GOLD_STANDARD_FILE_FOR_TESTING_TEXT_PREPARER,
    INPUT_DIR_FOR_TESTING_TEXT_PREPARER,
    OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER,
)


def test_prepare_one_chunk():

    if not OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER.exists():
        OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER.mkdir()

    prepare_one_chunk(
        filepath=INPUT_DIR_FOR_TESTING_TEXT_PREPARER / "fairy_tale.csv",
        output_dir_with_chunks=OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER
    )
    
    check_existence_of_output_csv_file_and_compare_with_gold_standard(
        output_file=OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER/"fairy_tale.csv",
        gold_standard_file=GOLD_STANDARD_FILE_FOR_TESTING_TEXT_PREPARER,
        unlink_if_successful=True,
    )
    
