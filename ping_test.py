#shabang

# Kasey Kiggins
# Kak8381@rit.edu
#Date: 9/12/2023

# create menu

def menu():
    print( "Welcome to Ping_test.py! \n Please select one of the following: \n 1.) Display the defualt gateway\n 2.) Test local connectivity\n 3.) Test remote connectivity \n 4.) Test DNS resolution\n 5.)Exit/end script")

#display the default gateway

def default():



    return 0
    # us the ip r command
#test the local connectivity

def local():
    #use 


    return 0
#test remote connectivity

def remote():




    return 0
    #use 129.21.3.17
#test dns resolution

def dns():



    
    return 0
    #use 8.8.8.8
#Exit/quit the script

def main():
    menu()
    val = input("")
    if val== 1:
        default()
    elif val == 2:
        local()
    elif val == 3:
        remote()
    elif val == 4:
        dns()
    elif val ==5:
        exit()
    else:
        print("Please enter an option as listed")
        main()
