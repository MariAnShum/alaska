from pathlib import Path

MAIN_DIR = Path(__file__).parent.parent.parent
DATA_DIR = MAIN_DIR / "data"

DIR_WITH_CHUNKS = DATA_DIR / "chunks"
FIRST_DIR_WITH_KODIAK_CHUNKS = DIR_WITH_CHUNKS / "kodiak-1"
SECOND_DIR_WITH_KODIAK_CHUNKS = DIR_WITH_CHUNKS / "kodiak-2"
DIR_WITH_NINILCHIK_CHUNKS = DIR_WITH_CHUNKS / "ninilchik"
DIR_WITH_PRIBILOVS_AND_INTERIOR_CHUNKS = DIR_WITH_CHUNKS / "pribilovs_and_interior"

DIR_WITH_INVENTORIES = DATA_DIR / "inventories"
FILE_WITH_PREPROCESSING_PATTERNS = DIR_WITH_INVENTORIES / "chunk_preprocessing_patterns.csv"
FORMAL_DECIPHERING_MEASURE_RESULTS = DIR_WITH_INVENTORIES / "formal_deciphering_measures.csv"
LEXICAL_DECIPHERING_MEASURE_RESULTS = DIR_WITH_INVENTORIES / "lexical_deciphering_measures.csv"
