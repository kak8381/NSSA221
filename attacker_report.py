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
            ip_address = re.findall("Failed password for"+ r".*" + ip_pattern, file_contents)
            #put ips in dictionary to count
            for ip in ip_address:
                ip = str(ip)[str(ip).index("from ")+5:]
                if ip in ip_counts:
                    ip_counts[ip] += 1
                else:
                    ip_counts[ip] = 1
            #sort the dictionary low to high
            sorted_ip_counts = dict(sorted(ip_counts.items(), key=itemgetter(1)))
            for ip, count in sorted_ip_counts.items():
                #print in format
                country = geolite2.lookup(str(ip))
                if country == "None":
                    country = "unknown location"
                else:
                    if count < 20:
                        continue
                
                    else:
                        country = geolite2.lookup(str(ip))
                        if country == "None":
                            country = "unknown location"
                        else:
                            print(f"{count}\t + {ip}\t\t" + country.country)
            return file_contents
           

    except FileNotFoundError:
        print("The file syslog.log was not found please check the name or path of the file.")
    


def main():
    date = os.popen("date").read()
    print("Attacker Report - "+ date + "\n")
    print("Count\t\t" + "IP\t\t" + "Country")
    file_read()

if __name__ == "__main__":
    subprocess.run(["clear"])

    main()
