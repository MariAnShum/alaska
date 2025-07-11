from pathlib import Path

MAIN_DIR = Path(__file__).parent.parent.parent
DATA_DIR = MAIN_DIR / "data"

DIR_WITH_CHUNKS = DATA_DIR / "chunks"
FIRST_DIR_WITH_KODIAK_CHUNKS = DIR_WITH_CHUNKS / "kodiak-1"

DIR_WITH_INVENTORIES = DATA_DIR / "inventories"
FILE_WITH_PREPROCESSING_PATTERNS = DIR_WITH_INVENTORIES / "chunk_preprocessing_patterns.csv"
