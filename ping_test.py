#shabang

#!/usr/bin/python3 

"""
Kasey Kiggins
Kak8381@rit.edu
Date: 9/12/2023
"""

#add imports
import subprocess
import platform
import re

# create menu

def menu():
    print( "Please select one of the following: \n 1.) Display the defualt gateway\n 2.) Test local connectivity\n 3.) Test remote connectivity \n 4.) Test DNS resolution\n 5.)Exit/end script")

#display the default gateway

def default():

    result = subprocess.run(["ip", "r"], capture_output=True)

    output = result.stdout.split()
    ip_bytes = output[2]

    ip_string = ip_bytes.decode('utf-8')

    return ip_string

def ping(address):
    result = subprocess.run(['ping', "-c", "4", address], capture_output=True)
    
    if result.returncode == 0:
        print(f"Ping to {address} was successful:\n")
        
    else:
        print(f"Ping to {address} failed with the following error message:\n")
        print(result.stderr)

    
#test the local connectivity

def local():
    #use default
    address= default()
    ping(address)
    #ping default

#test remote connectivity

def remote():
    #use 129.21.3.17
    host = "129.21.3.17"
    ping(host)
    

#test dns resolution

def dns():
    ping("google.com")
    #use 8.8.8.8

#making the program executable but not able to be edited

def exec():
    subprocess.run(["chmod", "+", "rx" ])
    subprocess.run(["chmod", "-", "w" ])
        



#Exit/quit the scripit

def main(): #clear
    menu()
    print("enter your selection: ")
    val = input("")
    if val== "1":
        print("Your default gateway is: " , default())
    elif val == "2":
        local()

    elif val == "3":
        remote()

    elif val == "4":
        dns()

    elif val == "5":
        subprocess.run(["clear"])
        exit()

    else:
        print("Please enter an option as listed")

    
if __name__ == "__main__":
    exec()
    subprocess.run(["clear"])
    while True:
       main()
