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

#making the link
def makelink(linkname,  path):
    desktop_dir = os.path.join(os.path.join(os.path.expanduser('~/Desktop'))) #path to desktop
    desktop_link = os.path.join(desktop_dir, os.path.basename(path))#path to link if it exists
    if os.path.exists(desktop_link):#check it link exists
        print("Link already exists.")
    else:
    #creating the link 
        if path != False:
            print("Creating Link...")
            #make link
            os.popen("ln -s " + path + " " + desktop_dir +"/"+ linkname)#command to make link
            print("Link successful!!")
        else:
            print("Oh no! Could not find file, please make sure file exists so the link has something to point to.")

def deletelink(linkname):
    linkpath = os.path.realpath(linkname)#path to link
    desktop_dir = os.path.join(os.path.join(os.path.expanduser('~/Desktop')))#path to desktop
    if linkpath != False:
        #delete link
        os.unlink(desktop_dir + "/" + linkname)
        print("Link successfully deleted!!")
            
    else:
        print("Oh no! Could not find link or file, please make sure link exists.\n")

def report():
    dirname = os.path.join(os.path.join(os.path.expanduser('~/Desktop')))#path to desktop
    linklist = os.popen("ls -l " + dirname ).read()#command to print list of links
    directorylist = os.popen("ls" + dirname).read().split("\n")
    list = []
    for i in range(len(directorylist)):
       links = os.readlink(dirname + "/" + directorylist[i])
       list.append(links + "\n")
    print("The links you have in " + dirname + " are: \n"+ linklist)
    print("The links you have in " + dirname + " are: \n"+ list)

def main():
    menu()
    path = ""
    list_of_files = []
    print("Enter you selection: ")
    val = input("")
    if val == "1":
        filename = input("Please enter a filename to make a link with:\n ")
        for root, dirs, files in os.walk('/'):
            if filename in files:
                path = os.path.join(root, filename)
                list_of_files.append(path)
            else:
                continue
        if len(path) < 3:
            print("File not found, or out of scope.")
        else:
            print("File found!")
            if len(list_of_files) > 1:
                for i in range(len(list_of_files)):
                    print(str(i + 1) + ".) " + list_of_files[i])
                filechoice = input("Please select a file you would like to make a link with.")
                if int(filechoice) < len(list_of_files):
                    path = list_of_files[int(filechoice)]
                else:
                    print("incorrect input")
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
