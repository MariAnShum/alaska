from pathlib import Path


def get_frequencies_dict_with_capitals(
        filepath: Path,
) -> None:
    with open(filepath, "r", encoding="utf-8") as f:
        data_from_file = f.read()
    frequencies_dict = {}
    data_from_file = data_from_file.split()
    for token in data_from_file:
        if token in frequencies_dict:
            frequencies_dict[token] += 1
        else:
            frequencies_dict[token] = 1
    frequencies_dict = sorted(frequencies_dict.items(), key=lambda x: x[1], reverse=True)
    with open(filepath.parent / "frequencies_of_all_words.txt", "w", encoding="utf-8") as f:
        for line in frequencies_dict:
            f.write(f"{line[0]}:\t{line[1]}\n")
