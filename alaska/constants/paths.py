from pathlib import Path

MAIN_DIR = Path(__file__).parent.parent.parent
DATA_DIR = MAIN_DIR / "data"

DIR_WITH_INPUT_FILES = DATA_DIR / "input"
DIR_WITH_INPUT_KODIAK_FILES = DIR_WITH_INPUT_FILES / "kodiak"
DIR_WITH_INPUT_NINILCHIK_FILES = DIR_WITH_INPUT_FILES / "ninilchik"
# DIR_WITH_INPUT_DOCX_FILES = DIR_WITH_INPUT_FILES / "docx_format"
# DIR_WITH_INPUT_DOCX_KODIAK_FILES = DIR_WITH_INPUT_DOCX_FILES / "kodiak"
# DIR_WITH_INPUT_DOCX_NINILCHIK_FILES = DIR_WITH_INPUT_DOCX_FILES / "ninilchik"

DIR_WITH_OUTPUT_FILES = DATA_DIR / "output"
DIR_WITH_OUTPUT_KODIAK_FILES = DIR_WITH_OUTPUT_FILES / "kodiak"
DIR_WITH_OUTPUT_NINILCHIK_FILES = DIR_WITH_OUTPUT_FILES / "ninilchik"

DIR_WITH_INVENTORIES = DATA_DIR / "inventories"
