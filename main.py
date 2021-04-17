#ToDo: hostfile enfernen
#(error)Meldungen v fping nicht ausgeben
import subprocess as sp
import os
import time


def glob():
    global output
    output = []


def ping():
    try:
        print("Generating (temporary) hostfile")
        os.system("fping -g 192.168.8.1 192.168.8.200 | grep alive > host")
    except:
        print("An error has occurred!!")

    os.system("clear")


def getName():
    f = open("host", "r")

    for i in f.readlines():

        txt = i.replace(" is alive", "")
        txt = txt.replace("\n", "")

        try:

            host = sp.check_output(["arp", txt]).decode("utf-8")

            if "--" in host:
                pass

            else:
                posA = host.find("Iface")
                posB = host.find("ether")
                name = txt + " ------> " + host[posA + 6:posB - 3]
                print(name)
                output.append(name)

        except:
            print("An error has occurred! IP= "+txt)


def fileHandling(k, w):
    if k.upper() == "Y":
        print("Keeping the hostfile")

    elif k.upper() == "N":
        print("Deleting the hostfile")
        os.system("rm host")

    else:
        print("Can't understand what you want me to do with the hostfile. I'm keeping it.")

    if w.upper() == "Y":
        print("Writing the output to 'OUTPUT.txt'. ")


        for i in output:
            os.system("echo '" + i + "' >> OUTPUT.txt")

    elif k.upper() == "N":
        pass

    else:
        print("Writing the output to 'OUTPUT.txt'. ")

        for i in output:
            os.system("echo '" + i + "' >> OUTPUT.txt")




glob()
ping()
getName()

keep = input("Do you want to keep the hostfile? (Y/N)")
write = input("Do you want to write the output into a file? (Y/N)")

fileHandling(keep, write)

print("Goodby!")

time.sleep(3)