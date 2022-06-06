from zipfile import ZipFile

file_name = "src.zip"
path = "C:\\Users\\abduh\\OneDrive\\Desktop\\Task NBU\\"

with ZipFile(file_name, "r") as zip:
    zip.printdir()
    
    print("Extracting all the files now ...")
    
    zip.extractall()
    print("Done")
    
