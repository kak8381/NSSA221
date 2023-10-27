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

def find_file(filename):
    for root, dirs, files in os.walk('/'):
        if filename in files:
            print("File found!")
            return os.path.join(root, filename)
        else:
            return False

def makelink(filename):
    desktop_dir = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    desktop_link = os.path.join(desktop_dir, os.path.basename(find_file(filename)))
    if os.path.exists(desktop_link):
        print("Link already exists.")
    else:
        
        if find_file(filename) != False:
            print("Creating Link...")
            #make link
            
            try:
                os.symlink(find_file(filename), desktop_link)
                print("Link successful!!")
            except:
                print("An error occured")
        else:
            print("Oh no! Could not find file, please make sure file exists so the link has something to point to.")

def deletelink(linkname):
    if os.path.exists(linkname):
        #delete link
        if os.path.isdir(linkname):
            if os.path.islink(linkname):
                os.unlink(linkname)
            else:
                shutil.rmtree(linkname)
                print("Link successfully deleted!!")
        else:
            if os.path.islink(linkname):
                os.unlink(linkname)
            else:
                removeobj(linkname)
            
    else:
        print("Oh no! Could not find link or file, please make sure link exists.")

def removeobj(linkname):
    var = input("Link was not found would you still like to remove this object?(yes/no)")
    if var.islower() == "yes":
        os.remove(linkname)
        print("object deleted")
    elif var.islower() == "no":
        return 0
    else:
        print("please enter yes or no")
        removeobj(linkname)

def report():
    dirname = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    linklist = os.popen("find " + dirname + " -type l").read().split("\n")
    print("The links you have in " + dirname + " are:")
    for i in range(0,len(linklist)):
        print(linklist[i] + "\n")

def main():
    menu()
    print("Enter you selection: ")
    val = input("")
    if val == "1":
        filename = input("Please enter a filename to make a link with:\n ")
        makelink(filename)
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
        menu()

if __name__ == "__main__":

    subprocess.run(["clear"])
    while True:
       main()
