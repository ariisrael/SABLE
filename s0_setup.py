#Name:        s0_setup.py
#Purpose:     Set up project folders
#Invocation:  python3 s0_setup.py <projName>

import os
import re
import sys

#Name:        valid_arguments
#Purpose:     Check whether the command-line arguments are valid
#Parameters:  sys.argv (globally defined list of command-line arguments)
#Returns:     True (arguments are valid) or False (arguments are invalid)

def valid_arguments():
    if len(sys.argv) == 2 and re.search(r"^[a-zA-Z][a-zA-Z_-]*$", sys.argv[1]):
        return True
    return False

#Name:        create_folders
#Purpose:     Create project folders
#Parameters:  projName (project name)
#Returns:     

def create_folders(projName):
    projDir = "/" + projName + "/"
    if os.path.isdir(projDir):
        print("\nProject folder " + projDir + " already exists\n")
    else:
        os.system("mkdir " + projDir)
        os.system("mkdir " + projDir + "crawl/")
        os.system("mkdir " + projDir + "download/")
        #The folder /projName/dump/ is created by Apache Nutch when its database contents are output to CSV format
        os.system("mkdir " + projDir + "neg_pdf/")
        os.system("mkdir " + projDir + "neg_prob/")
        os.system("mkdir " + projDir + "neg_txt/")
        os.system("mkdir " + projDir + "neg_xml/")
        os.system("mkdir " + projDir + "pos_pdf/")
        os.system("mkdir " + projDir + "pos_prob/")
        os.system("mkdir " + projDir + "pos_txt/")
        os.system("mkdir " + projDir + "pos_xml/")
        os.system("mkdir " + projDir + "pred_pdf/")
        os.system("mkdir " + projDir + "pred_prob/")
        os.system("mkdir " + projDir + "pred_txt/")
        os.system("mkdir " + projDir + "pred_xml/")
        os.system("mkdir " + projDir + "urls/")
        print("\nProject folder " + projDir + " and subfolders created\n")
    return

def main():
    if valid_arguments():
        create_folders(sys.argv[1])
    else:
        print("\nInvalid arguments\n")
    return

if __name__ == "__main__":
    main()
