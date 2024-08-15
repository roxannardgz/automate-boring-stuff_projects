#! python3

# backupToZip.py - Copies an entire folder and its content into a ZIP file whose filename increments.

import zipfile, os

def backup_to_zip(folder):
    # Back up the entire contents of 'folfer' into a zip file

    folder = os.path.abspath(folder)  # make sure folder is absolute

    # Figure out the filename this code code should use 
    number = 1

    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'

        if not os.path.exists(zip_filename):
            break
        number+= 1

    # Create the zip file
    print(f"Creating {zip_filename}...")
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # Walk the entire folder tree and compress the files in each folder
    for foldername, subfolder, filenames in os.walk(folder):
        print(f"Adding files in {foldername}...")

        # Add the current folder to the zip file
        backup_zip.write(foldername)

        # Add all the files  in this folder to the zip file
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue    #don't back up the backup zip files
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print('Done!')

if __name__ == "__main__":
    backup_to_zip('.')
