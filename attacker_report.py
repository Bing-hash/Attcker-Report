
# Nathan Dallmann         


from geoip import IPInfo, geolite2
import os



FILENAME = ""
# to store how many times a user failed to log in
log = {}
# to keep track of the keys used
keys = []
while(True):
    os.system("clear")
    FILENAME = input("Welcome to Attacker Report \nEnter log file: ")
    try:

        with open(FILENAME) as f:
            for line in f:
                # opening file and spliting the file. Date is grabbed for the printout
                tmp = line.split(" ")
                date = tmp[0]+" "+tmp[1]
                if "Failed" in tmp:
                    ip = tmp[10]
                    # had trouble getting the line with the failed login attempt, kept getting weird lines that went right through my if statement
                    # this second if checking length works to fix it
                    if len(ip.split("."))>2:
                        # if the address has already attempted to log into the server before, its int value is increased by one
                        # else a new entry is added to the log and keys
                        if ip in log:
                            log[ip]+=1
                        else:
                            log.update({ip:1})
                            keys.append(ip)
            # print(log)
            os.system("clear")
            print("Attacker Report - "+date+" 2021\n\n",end=" ")
            print("COUNT\tIP ADDRESS\tCOUNTRY\n",end=" ")
            for key in keys:
                # data is an IPInfo class. It contains lots of information about a given IP address. Including country of origin
                data = geolite2.lookup(key)

                # info is printed on the line
                print(log[key], end="\t")
                print(key, end="\t")
                print(data.country+"\n",end=" ")

                

        # file is closed
        f.close
        break





    except FileNotFoundError:
        print("File not found, press enter to try again: ")
        input("")