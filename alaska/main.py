from helpers.clear_dirs import clear_output_dirs, clear_all_except_reports_in_all_dirs
from preparers.preparers import preparers
from processing.discourse_analysis.discourse_analysis import discourse_analysis
from processing.alaskan_russian.alaskan_russian import alaskan_russian

FLAGS = "rmall"

preparers()
discourse_analysis()
alaskan_russian()

if "rmall" in FLAGS:
    clear_output_dirs()
elif "rmtemp" in FLAGS:
    clear_all_except_reports_in_all_dirs()
