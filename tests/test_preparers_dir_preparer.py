import pytest

from alaska.preparers.dir_preparer import (
    DirectoryGenerator,
    DirectoryGeneratorError,
    prepare_dirs,
)
from tests.paths import (
    DIR_WITH_DIRECTORY_GENERATOR_TEST_FILES,
    DIR_WITH_GOLD_STANDARD_DIRS_FOR_TESTING_DIRECTORY_GENERATOR,
    DIR_WITH_INPUT_FILES_FOR_TESTING_DIRECTORY_GENERATOR,
)


@pytest.fixture(scope="function")
def test_directory_generator():
    return DirectoryGenerator(
        input_directory_with_files=DIR_WITH_INPUT_FILES_FOR_TESTING_DIRECTORY_GENERATOR,
        output_directory_with_directories_for_each_file=DIR_WITH_DIRECTORY_GENERATOR_TEST_FILES,
    )


def test_prepare_dirs():
    pass


def test_generate_directories_throws_error_directory_contains_non_txt_files():
    new_directory_generator = DirectoryGenerator(
        input_directory_with_files=DIR_WITH_DIRECTORY_GENERATOR_TEST_FILES / "input_files_txt_and_csv",
        output_directory_with_directories_for_each_file=DIR_WITH_DIRECTORY_GENERATOR_TEST_FILES,
    )

    with pytest.raises(DirectoryGeneratorError, match="Input dir must contain only txt files."):
        new_directory_generator.generate_directories()
