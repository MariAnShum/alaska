from tinybear.csv_xls import read_dicts_from_csv, write_csv

from alaska.constants.paths import FIRST_DIR_WITH_KODIAK_CHUNKS


if __name__ == "__main__":
    
    chunks = list(FIRST_DIR_WITH_KODIAK_CHUNKS.glob("*.csv"))
    # for chunk in chunks:

        # Use this to add new column after ID
        # lines = read_plain_rows_from_csv(chunk, ";")

        # lines[0].insert(1, "recording_number_inside_chunk")

        # for i in range(1, len(lines)):
        #     lines[i].insert(1, "1")

        # write_csv(
        #     rows=lines,
        #     path_to_file=chunk,
        #     overwrite=True,
        #     delimiter=";",
        # )

    # Use this to update recording numbers (first lines must be marked manually)
    # for chunk in chunks:

    #     lines = read_dicts_from_csv(chunk, ";")

    #     for i in range(len(lines)-1):

    #         if int(lines[i]["recording_number_inside_chunk"]) > int(lines[i+1]["recording_number_inside_chunk"]):
    #             lines[i+1]["recording_number_inside_chunk"] = lines[i]["recording_number_inside_chunk"]

    #     write_csv(
    #         rows=lines,
    #         path_to_file=chunk,
    #         overwrite=True,
    #         delimiter=";",
    #     )
