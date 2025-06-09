from alaska.preparers.dir_preparer import prepare_dirs
from tests.paths import (
    DIR_WITH_INPUT_FILES_FOR_TESTING_DIR_PREPARER,
    DIR_WITH_GOLD_STANDARD_DIRS_FOR_TESTING_DIR_PREPARER,
)

def test_prepare_dirs():
    input_files = list[DIR_WITH_INPUT_FILES_FOR_TESTING_DIR_PREPARER.glob("*.csv")]
    print(input_files)
    assert False
