#!/usr/bin/python3 

"""
Kasey Kiggins
Kak8381@rit.edu
Date: 10/25/2023
"""

#add imports
import shutil
import subprocess
import platform
import re
import os


#must create links on the users desktop "/home/user/desktop"
#make symbolic link, delete a link, and run report

#command line menu
def menu():
    directory = os.popen("pwd").read()
    print("You are currently in " + directory +
        "\nPlease pick an option:" + 
        "\n1.) Make symbolic link" +
        "\n2.) Delete a link" +
        "\n3.) Run Report" +
        "\ntype quit to end")

def makelink(linkname,  path):
    desktop_dir = os.path.join(os.path.join(os.path.expanduser('~/Desktop')))
    print(desktop_dir)
    desktop_link = os.path.join(desktop_dir, os.path.basename(path))
    if os.path.exists(desktop_link):
        print("Link already exists.")
    else:
        
        if path != False:
            print("Creating Link...")
            #make link
            os.popen("ln -s " + path + " " + desktop_dir +"/"+ linkname)
            print("Link successful!!")
        else:
            print("Oh no! Could not find file, please make sure file exists so the link has something to point to.")

def deletelink(linkname):
    linkpath = os.path.realpath(linkname)
    desktop_dir = os.path.join(os.path.join(os.path.expanduser('~/Desktop')))
    if linkpath != False:
        #delete link
        os.unlink(desktop_dir + "/" + linkname)
        print("Link successfully deleted!!")
            
    else:
        print("Oh no! Could not find link or file, please make sure link exists.")

def report():
    dirname = os.path.join(os.path.join(os.path.expanduser('~/Desktop')))
    linklist = os.popen("ls -l " + dirname ).read()
    print("The links you have in " + dirname + " are: \n"+ linklist)

def main():
    menu()
    path = ""
   
    print("Enter you selection: ")
    val = input("")
    if val == "1":
        filename = input("Please enter a filename to make a link with:\n ")
        for root, dirs, files in os.walk('/'):
            if filename in files:
                print("File found!")
                path = os.path.join(root, filename)
            else:
                continue
        linkname = input("What would you like the link to be named? \n")
        makelink(linkname, path)
    elif val == "2":
        linkname = input("Please enter a link you would like to delete:\n ")
    
        deletelink(linkname)
    elif val == "3":
        report()
    elif val == "quit":
        exit()
    else:
        subprocess.run(["clear"])
        print("please enter a usable value")

if __name__ == "__main__":

    subprocess.run(["clear"])
    while True:
       main()
