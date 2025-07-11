from pathlib import Path

DIR_WITH_TEST_FILES = Path(__file__).parent / "test_data"

DIR_WITH_PREPARERS_TEST_FILES = DIR_WITH_TEST_FILES / "preparers"

DIR_WITH_TEXT_PREPARER_TEST_FILES = DIR_WITH_PREPARERS_TEST_FILES / "text_preparer"
INPUT_DIR_FOR_TESTING_TEXT_PREPARER = DIR_WITH_TEXT_PREPARER_TEST_FILES / "input"
OUTPUT_DIR_FOR_TESTING_TEXT_PREPARER = DIR_WITH_TEXT_PREPARER_TEST_FILES / "output"
