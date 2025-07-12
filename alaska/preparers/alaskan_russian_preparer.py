"""
Навскидку тут надо сделать две функции:
1. Если около слова есть нижнее подчеркивание, то отследить второе нижнее подчеркивание дальше
и обвести подчеркиваниями все слова между ними (так я отмечаю каждое аляскинское русское слово)
2. Заменить составные гласные с ударениями на раздельно ударение и гласную букву
(заготовка ниже)
В обеих функциях прочитывать только одну колонку -- replica
"""


# def make_all_stresses_and_their_vowels_united_symbols(
#         data_from_file: str,
# ) -> str:
#     double_to_single = {
#         "á": "á",
#         "é": "é",
#         "í": "í",
#         "ó": "ó",
#         "ú": "ú",
#         "Á": "Á",
#         "É": "É",
#         "Í": "Í",
#         "Ó": "Ó",
#         "Ú": "Ú",
#     }
#     for key in double_to_single:
#         data_from_file = data_from_file.replace(key, double_to_single[key])
#     data_from_file = data_from_file.replace("̇", "")
#     return data_from_file
