#! /usr/bin/python
##Imports
import os
import sys
import argparse

##Example how the path and text_to_replace should look
##path = '/Users/name/Downloads/folder
##text_to_replace = "text"

##Preforme substring replacement
def replace_substring_name(path,text_to_replace):

    arr = os.listdir(path)

    for files in arr:

        if(text_to_replace in files):
            old_file = os.path.join(path, files)
            new_file = os.path.join(path, files.replace(text_to_replace, ''))
            os.rename(old_file, new_file)

##Display warning as well as asking for acceptance of warning
def print_warning(text_to_replace):
    print(f"\033[31mWARNING ALL FILES WITHIN THE DIRECTORY WILL RENAMED!\033[0m")
    print('\nExample of the changes going to be made (any file extention can be used .txt is only used as a example):')
    print(f"\n\t Previous file name: \t \033[31m {text_to_replace}\033[0mfile.txt")
    print(f"\n\t New file name: \t file.txt")
    print("\nWould you like to still preforme the action (Y/N)?")
    check = str(input())
    if (check.__eq__('y')):
        return True
    else:
        return False

def display_file_in_directory(path):
    directory = os.listdir(path)
    print('\n The following files will be mutated:')
    for file in directory:
        print(f'\n{file}')
    print('Continue with filename change (Y/N)?')
    check = input().lower()
    if (check.__eq__('y')):
        return True
    else:
        return False


def main():
    ##Initate variables passed by users
    os.system('cls||clear')
    parser = argparse.ArgumentParser(
        description="Script that removes substring from all file names within a directory."
    )
    parser.add_argument("--path", required=True, type=str,help="Enter the path for the directory containing the files.")
    parser.add_argument("--substring", required=True, type=str,help="Enter the substring to remove from filenames.")
    args = parser.parse_args()
    path = args.path
    text_to_replace = args.substring

    ##Display warning message
    check_aggrement = print_warning(text_to_replace)

    ##Display files to be mutated
    check_selected_files = display_file_in_directory(path)

    ##Checking if warning was accepted
    if(check_aggrement == True and check_selected_files == True):
        replace_substring_name(path,text_to_replace)
        print(f'\nAction Completed data was saved to the following directory: {path}')
    else:
        print("\nGoodbye")

