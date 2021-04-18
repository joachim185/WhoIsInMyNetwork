'''ToDO: Mac Adressen anzeigen lassen
    Anzahl der Gefundenen Clients anzeigen lassen
    Variablen besser benennen
'''



import subprocess as sp
import os
import time


def ping():
    try:
        print("Checking the Network. Please be patient...")
        f=sp.getoutput(["fping -a -q -g 192.168.8.1 192.168.8.255"])
        return f
    except:
        print("An error has occurred!!")

    os.system("clear")


def getName(u):
    output=[]
    user=u.split("\n")

    for i in user:

        if "duplicate" in i:
            pass

        else:

            try:

                host = sp.check_output(["arp", i]).decode("utf-8")

                if "--" in host:
                    pass

                else:
                    posA = host.find("Iface")
                    posB = host.find("ether")
                    name = i + " ------> " + host[posA + 6:posB - 3]
                    print(name)
                    output.append(name)

            except:
                print("An error has occurred! IP= "+i)

    return output

def fileHandling(w,o):

    if w.upper() == "Y":
        print("Writing the output to 'OUTPUT.txt'. ")


        for i in o:
            os.system("echo '" + i + "' >> OUTPUT.txt")

    elif w.upper() == "N":
        pass

    else:
        print("Writing the output to 'OUTPUT.txt'. ")

        for i in o:
            os.system("echo '" + i + "' >> OUTPUT.txt")


users=ping()
o=getName(users)

write = input("Do you want to write the output into a file? (Y/N)")
fileHandling(write,o)

print("Goodby!")

time.sleep(3)
