# Write a script that renames all files in a specific directory
import os
import time
from time import sleep
from dotenv import load_dotenv

# Load .env file
load_dotenv()

folderName = os.getenv("SRC")
print(folderName)


def removeText(folderName):
    """This method deletes text files """
    print("Cleaning Text files ...")
    for filename in (os.listdir(folderName)):
        if filename.endswith(".txt"):
            os.remove(os.path.join(folderName, filename))
    print("Done ...")


def fileOrganiser(name, folderName=folderName):
    """ This method renames pdf files, 
        It takes two arguments folderName, this is the file path 
        and name to be given to the files
     """
    count = 1
    print("Renaming PDF files ...")
    for _, filename in enumerate(os.listdir(folderName)):
        renamedFile = f"{name}_{count}.pdf"
        src = f"{folderName}/{filename}"
        dst = f"{folderName}/{renamedFile}"
        os.rename(src, dst)
        count += 1
    print("Done .. ")
    print(f"we have renamed {count-1} files successfully")


# Remove Text files
removeText(folderName)
time.sleep(.100)
# rename pdf files
fileOrganiser("iDariParaCezasiMaliSuclariOnleme")
