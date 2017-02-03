__author__ = 'rekhin'

import os

print("Rename file starts")
def rename_files():
    #files = os.listdir("/home/rekhin/Rexo/Develop/Works/learnPython/prank/prank")
    files = os.listdir(os.getcwd()+"/prank")
    current_dir = os.getcwd();
    #print current_dir
    os.chdir(os.getcwd()+"/prank")
    for one_file in files:
        #os.rename(one_file, one_file.translate(None, "0123456789"))
        os.rename("halo","hi")
        #print(one_file)

def main():
    rename_files()
main()