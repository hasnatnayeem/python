import os, sys, zipfile, datetime, schedule

def job():
    print("Working")
    path = "/home/nayeem/Desktop/texts"
    log_file_extention = ".txt"

    files = os.listdir(path);

    now = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    archive_name = "log_" + now + ".zip"

    try:
        z = zipfile.ZipFile(os.path.join(path, archive_name), "w") # Creating zip file
    except:
        print("Error creating ZIP file")
        sys.exit()


    try :
        # Adding files to archive
        for file_name in os.listdir(path):
            if file_name.endswith(log_file_extention):
                print("Adding " + file_name)
                file_path = os.path.join(path,file_name)
                z.write(file_path, file_name) # Only adding the file instead of full directory
        z.close() # Closing file after writing is finished
    except:
        print("Problem occurred while adding files to archive")
        sys.exit()


    try:
        # Deleting archived files
        for file_name in os.listdir(path):
            if file_name.endswith(log_file_extention):
                file_path = os.path.join(path,file_name)
                os.remove(file_path)
    except:
        print("Problem occurred while deleting files")
        sys.exit()



schedule.every(10).seconds.do(job)

while 1:
    schedule.run_pending()

