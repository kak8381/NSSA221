#!/ust/bin/python3

"""
Kasey Kiggins
Kak8381@rit.edu
Date: 10/04/2023
"""

#add imports
import subprocess
import platform
import re

#writing and creating a file
def file_edit(text):
   file = open(text, "w")
   file.write("") 

def main():
    text = "output.txt"
    file_edit(text)

if __name__ == "__main__":
    subprocess.run(["clear"])

    main()

