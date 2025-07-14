from alaska.processing.discourse_analysis.formal_deciphering import (
    count_fixed_and_missed_syllables_in_one_chunk,
)

from tests.paths import DIR_WITH_FORMAL_DECIPHERING_TEST_FILES


INPUT_CHUNKS = list(DIR_WITH_FORMAL_DECIPHERING_TEST_FILES.glob("*.csv"))

def test_count_total_and_missed_syllables_in_one_chunk():

    GOLD_STANDARD_COUNTS = {
        "novel.csv": {
            "fixed_syllables": 215,
            "missed_syllables": 14,
        },
        "village_story.csv": {
            "fixed_syllables": 169,
            "missed_syllables": 0,
        },
        "piece_with_alaskan_russian.csv": {
            "fixed_syllables": 186,
            "missed_syllables": 9,
        },
    }

    resulting_counts = {
        "novel.csv": {
            "fixed_syllables": 0,
            "missed_syllables": 0,
        },
        "village_story.csv": {
            "fixed_syllables": 0,
            "missed_syllables": 0,
        },
        "piece_with_alaskan_russian.csv": {
            "fixed_syllables": 0,
            "missed_syllables": 0,
        },
    }

    for chunk in INPUT_CHUNKS:

        chunk_name = chunk.name

        fixed_syllables, missed_syllables = count_fixed_and_missed_syllables_in_one_chunk(
            filepath=chunk,
        )

        resulting_counts[chunk_name]["fixed_syllables"] = fixed_syllables
        resulting_counts[chunk_name]["missed_syllables"] = missed_syllables

    for chunk in INPUT_CHUNKS:
        # I know that different syllable counters have different accuracy
        # and some even return several options of pronunciation,
        # i.e. 2 and 3 syllables for the word "family".
        # That is why, for fixed syllables, I allow margin +- 5%
        # around "gold standard" -- my manual count.

        chunk_name = chunk.name

        minimal_margin = GOLD_STANDARD_COUNTS[chunk_name]["fixed_syllables"] * 0.95
        maximal_margin = GOLD_STANDARD_COUNTS[chunk_name]["fixed_syllables"] * 1.05
        assert resulting_counts[chunk_name]["fixed_syllables"] >= minimal_margin \
            and resulting_counts[chunk_name]["fixed_syllables"] <= maximal_margin
        assert resulting_counts[chunk_name]["missed_syllables"] == GOLD_STANDARD_COUNTS[chunk_name]["missed_syllables"]
