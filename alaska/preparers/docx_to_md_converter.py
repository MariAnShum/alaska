import mammoth

from html2markdown import convert
from pathlib import Path

from alaska.constants.paths import (
    DIR_WITH_CHUNKS,
    DIR_WITH_UNCONVERTED_DOCS_CHUNKS,
)


def convert_files_from_docx_to_md(dir_with_files_to_convert = DIR_WITH_UNCONVERTED_DOCS_CHUNKS):

    files_to_convert = dir_with_files_to_convert.glob("*.docx")
    for file in files_to_convert:

        convert_one_file_from_docx_to_md(file)


def convert_one_file_from_docx_to_md(file: Path):
    filestem = file.stem
    with open(file, "rb") as docx_file:
        html_result = mammoth.convert_to_html(docx_file)
        html = html_result.value
        markdown = convert(html)
        
        with open(f"{DIR_WITH_CHUNKS}/{filestem}.csv", "w", encoding="utf-8") as md_file:
            md_file.write(markdown)


if __name__ == "__main__":
    convert_files_from_docx_to_md()
