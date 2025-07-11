from alaska.preparers.text_preparer import (
    add_column_for_reply_ids_and_fill_it_in_one_chunk,
    remove_and_replace_extra_symbols_in_one_chunk,
)
from tests.helpers import check_existence_of_output_csv_file_and_compare_with_gold_standard
from tests.paths import (
    DIR_WITH_TEXT_PREPARER_TEST_FILES,
    INPUT_DIR_FOR_TESTING_TEXT_PREPARER,
    OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER,
)

GOLD_STANDARD_FILE_FOR_TESTING_REMOVING_AND_REPLACING = DIR_WITH_TEXT_PREPARER_TEST_FILES / "removing_and_replacing_gold_standard.csv"
GOLD_STANDARD_OF_CHUNK_WITH_REPLY_IDS = DIR_WITH_TEXT_PREPARER_TEST_FILES / "ready_chunk_gold_standard.csv"

def test_prepare_one_chunk():

    if not OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER.exists():
        OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER.mkdir()

    remove_and_replace_extra_symbols_in_one_chunk(
        filepath=INPUT_DIR_FOR_TESTING_TEXT_PREPARER / "fairy_tale.csv",
        output_dir_with_chunks=OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER
    )
    
    check_existence_of_output_csv_file_and_compare_with_gold_standard(
        output_file=OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER/"fairy_tale.csv",
        gold_standard_file=GOLD_STANDARD_FILE_FOR_TESTING_REMOVING_AND_REPLACING,
        unlink_if_successful=True,
    )
    

def test_add_column_for_reply_ids_and_fill_it_in_one_chunk():

    if not OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER.exists():
        OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER.mkdir()

    add_column_for_reply_ids_and_fill_it_in_one_chunk(
        filepath=INPUT_DIR_FOR_TESTING_TEXT_PREPARER / "same_tale_without_reply_ids.csv",
        output_dir_with_chunks=OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER,
    )

    check_existence_of_output_csv_file_and_compare_with_gold_standard(
        output_file=OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER / "same_tale_without_reply_ids.csv",
        gold_standard_file=GOLD_STANDARD_OF_CHUNK_WITH_REPLY_IDS,
    )
