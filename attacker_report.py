#!/usr/bin/python3 

"""
Kasey Kiggins
Kak8381@rit.edu
Date: 11/08/2023
"""

#add imports
import shutil
import subprocess
import platform
import re
import os
#from geoip import geolite2
import pathlib
from operator import itemgetter

#regex to match ip pattern
ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
# creating a dictionary to store ips
ip_counts = {}
#reading the files
def file_read():
    try:
        with open("syslog.log", 'r') as file:
            file_contents = file.read()
            #split file into only ip address by regex
            ip_address = re.findall(ip_pattern, file_contents)
            #put ips in dictionary to count
            for ip in ip_address:
                if ip in ip_counts:
                    ip_counts[ip] += 1
                else:
                    ip_counts[ip] = 1
            #sort the dictionary low to high
            sorted_ip_counts = dict(sorted(ip_counts.items(), key=itemgetter(1)))
            for ip, count in sorted_ip_counts.items():
                #print in format
                country = {ip}.country
                print(f"{count}\t\t + {ip}\t\t" + country)
           

    except FileNotFoundError:
        print("The file syslog.log was not found please check the name or path of the file.")
    return file_contents


def main():
    file_read()

if __name__ == "__main__":
    subprocess.run(["clear"])

    main()
