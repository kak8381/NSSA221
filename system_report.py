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
import os


#Device information
def device():
    #linux command hostname / hostname -d
    #socket.dif
    hostname = os.popen("hostname | awk -f '.' '{print $1}' ").read()
    domainname = os.popen("hostname | awk -f '.' '{print $2 $3}'").read()
    return "\nDevice Information" + "\nHostname:" + "\t" + "\t" + hostname  + "Domain:" + "\t" + "\t" + "\t"+ domainname + "\n"
#network information

def network():
    #getting the ip address
    ip = os.popen("ifconfig | awk 'NR==2{print $2}'").read()
    gateway = os.popen("ip r | awk 'NR==1{print $3}'").read()
    subnet = os.popen("ifconfig | awk 'NR==2{print $4}'").read()
    
    return "\nNetwork Information" + "\n" + "IP Address: \t\t" + ip + "Gateway:" + "\t" + "\t" + gateway +"\n" + "Network Mask:\t\t" + subnet + "\n"

#os information system, version , kernal version
def os_info():
    system = os.popen('uname -o').read()
    version = os.popen('uname -r').read()
    kversion = os.popen('uname -v').read()

    return "\nOS Information" +"\nOperating System: \t\t" + system + "Operating Version:\t\t" + version +  "Kernal Version:\t\t\t" + kversion 

#storage information
def storage():
    capacity = os.popen("df -h / | awk 'NR==2{print $2}'").read()
    availible = os.popen("df -h / | awk 'NR==2{print $4}'").read()
    return "\nStorage Information" +"\n" + "Hard Drive Capacity:\t\t" + capacity + "\n" + "Available Space:\t\t" + availible + "\n"

#process information
def processor():
    
    return "\nProcessor Information" +"\n"

#memory information
def memory():
    #free command
    ram = os.popen("free | awk 'NR==2{print $2}'").read()
 
    ramavailable = os.popen("free | awk 'NR==2{print $3}'").read()
    
    return "\nMemory Information" + "\n"+ ram

#writing and creating a file
def file_edit(text):
   file = open(text, "w")
   date = os.popen("date").read()
   file.write("\tSystem Report " + date + "\n") 
   file.write(device())
   file.write(network())
   file.write(os_info())
   file.write(storage())
   file.write(processor())
   file.write(memory())

def main():
    text = "output.txt"
    file_edit(text)
    output = subprocess.check_output(["cat", text])
    output = output.decode('utf-8')
    subprocess.run(["clear"])
    print(output)


if __name__ == "__main__":
    subprocess.run(["clear"])

    main()

