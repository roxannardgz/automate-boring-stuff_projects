#! python3

# renameDates.py - Rename filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY format.

import shutil, os, re

# Create a Regex that matches files with American date format
date_pattern = re.compile(r"""(.*?)
                          (0?[1-9]|1[0-2])-
                          (0?[1-9]|[12][0-9]|3[01])-
                          (19|20\d\d)
                          (.*?)$
                          """, re.VERBOSE)

# Loop over the files in the working diretory
for american_filename in os.listdir('.'):
    mo = date_pattern.search(american_filename)

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(3)
    year_part = mo.group(4)
    after_part = mo.group(5)


    # Form the European-style filename
    european_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part


    # Get the full file paths
    working_dir = os.path.abspath('.')
    american_filename = os.path.join(working_dir, american_filename)
    european_filename = os.path.join(working_dir, european_filename)


    # Rename the files
    print(f"Renaming '{american_filename}' to '{european_filename}'.")
    shutil.move(american_filename, european_filename)
