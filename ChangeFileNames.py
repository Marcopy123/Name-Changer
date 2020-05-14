import os # import os library
import sys # import sys library

new_name = '' # initialize new_name variable
file_names_count = 0 # initialize file_names_count variable
directories_names_count = 0 # initialize directories_names_count variable
consent = '' # initialize conset variable

for _, directories_names, file_names in os.walk(os.getcwd()): # store the directories_names and file_names of the                                               # current working directory_name into directories_names 
                                                   # and file_names variables
    for file_name in file_names:  # check every file_name
        if " " in file_name:  # if file_name contains space
            new_name = file_name.replace(" ", "_") # assign new_name to the original file_name 
                                          # new_name with underscore

            consent = input(f"Would you like to replace {file_name} to {new_name} ? ")  # ask for consent to replace
            while consent.lower() != 'no' and consent.lower() != 'yes':
                consent = input(
                    f"Would you like to replace {file_name} to {new_name} ? ")

            if consent.lower() == "yes":    # if they accept
                file_names_count += 1    # increment file_names_count
                os.rename(file_name, new_name)    # renew_name the file_name
                print(f"Replacing {file_name} to {new_name}\n")

    for directory_name in directories_names:   # check every directory_name
        if " " in directory_name:    # if directory_name contains space
            # assign new_name to the original directory_name new_name with underscore
            new_name = directory_name.replace(" ", "_")

            # ask for consent
            consent = input(f"Would you like to replace {directory_name} to {new_name} ? ")

            while consent.lower() != 'no' and consent.lower() != 'yes':
                consent = input(
                    f"Would you like to replace {directory_name} to {new_name} ? ")

            if consent.lower() == 'yes':    # if they accept
                directories_names_count += 1  # increment directories_names_count
                os.rename(directory_name, new_name)   # renew_name the directory_name
                print(f"Replacing {directory_name} to {new_name}\n")

if file_names_count + directories_names_count == 0:    # if nothing has changed
    print("Did not replace anything")
    sys.exit()  # exit code

if directories_names_count > 1:   
    print(
        f"Replaced a total of {file_names_count} file_name(s) and {directories_names_count} directories_names !")
    sys.exit()

print(
    f"Replaced a total of {file_names_count} file_name(s) and {directories_names_count} directory_name !")
