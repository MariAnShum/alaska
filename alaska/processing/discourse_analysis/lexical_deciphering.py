import re

from pathlib import Path
from tinybear.csv_xls import read_dicts_from_csv

from alaska.constants.paths import DIR_WITH_INVENTORIES, FIRST_DIR_WITH_KODIAK_CHUNKS

FILE_WITH_STOPWORDS = DIR_WITH_INVENTORIES / "stopwords.txt"

# def get_lexical_deciphering_measure(
#         filepath: Path,
# ):
#     with open(filepath, "r", encoding="utf-8") as f:
#         frequencies_dict = {}
#         for line in f:
#             word, counter = line.split("\t")
#             word = word.replace(":", "")
#             counter = counter.replace("\n", "")
#             frequencies_dict[word] = counter
#     with open(FILE_WITH_STOPWORDS, "r", encoding="utf-8") as f:
#         custom_stopwords = set(f.read().split())
#     default_stopwords = set(stopwords.words('english'))
#     custom_stopwords = custom_stopwords.union(default_stopwords)
#     total_words_counter = 0
#     key_words_counter = 0
#     for key in frequencies_dict:
#         total_words_counter += int(frequencies_dict[key])
#         if key not in custom_stopwords:
#             key_words_counter += int(frequencies_dict[key])
#     return total_words_counter, key_words_counter


# def fill_lexical_deciphering_report(
#         total_words_counter: int,
#         key_words_counter: int,
#         lexical_deciphering_report_file: Path,
# ) -> None:
#     try:
#         lexical_deciphering_measure = round(key_words_counter / total_words_counter, 2)
#     except ZeroDivisionError:
#         lexical_deciphering_measure = 1
#     with open(lexical_deciphering_report_file, "w", encoding="utf-8") as f:
#         f.write(f"Total words:\t{total_words_counter}\n")
#         f.write(f"Key words:\t{key_words_counter}\n")
#         f.write(f"LDM:\t{lexical_deciphering_measure}\n")


if __name__ == "__main__":
    chunks = list(FIRST_DIR_WITH_KODIAK_CHUNKS.glob("*.csv"))

    global_overall_concordance = {}

    for chunk in chunks:
        replies = read_dicts_from_csv(
            path_to_file=chunk,
            delimiter=";",
        )

        for reply in replies:
            replica = reply["replica"]

            words = replica.replace(".", "").replace("?", "").replace("!", "").replace("_", "").split()
            for word in words:
                word = word.lower()
                if word not in global_overall_concordance.keys():
                    global_overall_concordance[word] = 1
                    continue
                global_overall_concordance[word] += 1
            
    ordered_concordance = dict(sorted(global_overall_concordance.items(), key=lambda item: item[1]))
    for item in ordered_concordance.items():
        print(item)
