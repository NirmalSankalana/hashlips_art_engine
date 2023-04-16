import os

# specify the directory containing the PNG files
directory = "./layers/Lense1/"

# loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        # create the new filename by replacing "-" with " "
        new_filename = filename.replace("-", " ")
        
        # rename the file with the new filename
        os.rename(directory + filename, directory + new_filename)
