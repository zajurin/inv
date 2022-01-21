from distutils.util import change_root
import subprocess as sp
import re
import time

list_to_search = ["AzureAdJoined : ", "AzureAdPrt : ",
                  "IsDeviceJoined : ", "IsUserAzureAD : "]
username = sp.getoutput("whoami")
checking_status = sp.getoutput("dsregcmd /status")
my_model = sp.getoutput("wmic csproduct get name")
mySerialNumber = sp.getoutput("wmic bios get serialnumber")

# Cleaning unwanted ne lines
theUsername = username.replace("\n", "")
theModel = my_model.replace("\n", "")
theSerialNumber = mySerialNumber.replace("\n", "")

# Remove multiple spaces in strings
cleanUserName = re.sub(" +", " ", theUsername)
cleanModel = re.sub(" +", " ", theModel)
cleanSerialNumber = re.sub(" +", " ", theSerialNumber)

print(cleanUserName)
print(cleanModel)
print(cleanSerialNumber)
print()


class MyCommand:
    def __init__(self, command):
        self.command = command
        global myResult
        myResult = sp.getoutput(self.command)


def Runner():
    repeat_n_times = 1
    while repeat_n_times <= 2:
        for eachSearched in list_to_search:
            try:
                myInstance = MyCommand("dsregcmd /status")
                time.sleep(1)  # change "2" to "360" for 6 minutes

                if eachSearched + "YES" in myResult:
                    print(eachSearched + "YES")

                elif eachSearched + "NO" in myResult:
                    global changer
                    changer = eachSearched + "NO"
                    print(changer)

                else:
                    print("Nothing was found it")
            except:
                print("error")
        repeat_n_times += 1
        if repeat_n_times < 3 and changer:
            print(
                "\nSeems that one or more of the values was 'NO'.\nWe need to update this process ")
            print()
            updating = sp.getoutput("gpupdate /force")
            print(updating)
            minutes_to_wait = .5
            myTime = minutes_to_wait = 60
            print(f"Waiting {minutes_to_wait} minutes")
            timeInSeconds = time.sleep(myTime)
            print(f"\nTry nuber {repeat_n_times} \n")

        else:
            print("\n\nrepeat_n_times is not lower than 3 or changer isn't NOT ")


Runner()
