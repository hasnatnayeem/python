import os, zipfile, datetime

path = "/home/nayeem/log_directory"

files = os.listdir(path);

if len(files) > 0:
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    archive_name = "log_" + now + ".zip"

    z = zipfile.ZipFile(os.path.join(path, archive_name), "w") # Creating zip file

    # Adding files to archive
    for file_name in os.listdir(path):
        if file_name.endswith(".txt"):
            print("Adding " + file_name)
            file_path = os.path.join(path,file_name)
            z.write(file_path, file_name) # Only adding the file instead of full directory
            os.remove(file_path)

    z.close()

    # Deleting archived files
    for file_name in os.listdir(path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(path,file_name)
            os.remove(file_path)

