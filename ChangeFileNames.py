import os # import os library
import sys # import sys library

import cprint # import cprint library
import termcolor # import termcolor library

name = '' # initialize name variable
files_count = 0 # initialize files_count variable
directories_count = 0 # initialize directories_count variable
consent = '' # initialize conset variable

for _, directories, files in os.walk(os.getcwd()): # store the directories and files of the 
                                                   # current working directory into directories 
                                                   # and files variables
    for file in files:  # check every file
        if " " in file:  # if file contains space
            name = file.replace(" ", "_") # assign name to the original file 
                                          # name with underscore

            consent = input("Would you like to replace " +  
                            file + " to " + name + " ? ")  # ask for consent to replace

            if consent.lower() == "yes":    # if they accept
                files_count += 1    # increment files_count
                os.rename(file,name)    # rename the file
                termcolor.cprint(f"Replacing {file} to {name}\n", "green")

    for directory in directories:   # check every directory
        if " " in directory:    # if directory contains space
            # assign name to the original directory name with underscore
            name = directory.replace(" ", "_")

            consent = input("Would you like to replace " +
                            directory + " to " + name + " ? ")  # ask for consent

            if consent.lower() == 'yes':    # if they accept
                directories_count += 1  # increment directories_count
                os.rename(directory,name)   # rename the directory
                termcolor.cprint(f"Replacing {directory} to {name}\n","green")

if files_count + directories_count == 0:    # if nothing has changed
    termcolor.cprint("Did not replace anything","red")
    sys.exit()  # exit code

if directories_count > 1:   
    termcolor.cprint(
        f"Replaced a total of {files_count} file(s) and {directories_count} directories !", "green")
    sys.exit()

termcolor.cprint(
    f"Replaced a total of {files_count} file(s) and {directories_count} directory !", "green")
