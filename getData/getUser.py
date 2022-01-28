from distutils.util import change_root
import subprocess as sp
import re
import time
import getmac
import platform


dataDictionary = {}

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

# Remove extra words
finalModel = re.sub("Name ", "", cleanModel)
finalSerialNumber = cleanSerialNumber.replace("SerialNumber ", "")
finalmacAddress = getmac.get_mac_address()
final_os = platform.system()
final_os_version = platform.release()

concatenate_os_version = f"{final_os} {final_os_version}"

# sending data to Dictionary
dataDictionary["username"] = cleanUserName
dataDictionary["model"] = finalModel
dataDictionary["serialNumber"] = finalSerialNumber
dataDictionary["macAddress"] = finalmacAddress
dataDictionary["operatingSystem"] = f"{final_os} {final_os_version}"

print(f"userName: {cleanUserName}")
print(f"Model: {finalModel}")
print(f"Serial Number: {finalSerialNumber}")
print(f"MAC ADDRESS: {finalmacAddress}")
print(f"Operating System: {final_os} {final_os_version}")
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
                    deleteSpace_eachSearched = re.sub(" +", " ", eachSearched)
                    remove_Colon_eachSearched = deleteSpace_eachSearched.replace(
                        ":", "")
                    dataDictionary[remove_Colon_eachSearched] = "YES"

                elif eachSearched + "NO" in myResult:
                    global changer
                    changer = eachSearched + "NO"
                    print(changer)
                    deleteSpace_eachSearched = re.sub(" +", " ", eachSearched)
                    remove_Colon_eachSearched = deleteSpace_eachSearched.replace(
                        ":", "")
                    dataDictionary[remove_Colon_eachSearched] = "NO"
# ????????????????????? CHECK THIS CODE ?????????????????????????????????
                else:
                    if "Windows 10" in concatenate_os_version:
                        dataDictionary[remove_Colon_eachSearched] = "NO (Check this laptop)"

                    else:
                        if "Windows 10" in concatenate_os_version:
                            dataDictionary[remove_Colon_eachSearched] = "NO (Check this laptop)"
                        else:
                            print(
                                f"Your {concatenate_os_version} needs to be verified")
                            changer = "command did not work"

                            print(changer)
# ?????????????????????????????????????????????????????????????????
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
            myTime = minutes_to_wait * 60
            print(f"Waiting {minutes_to_wait} minutes")
            timeInSeconds = time.sleep(myTime)
            print(f"\nTry number {repeat_n_times} \n")

        else:
            print(
                f"\n\n{repeat_n_times} is not lower than 3 or changer isn't NOT ")


Runner()
print(dataDictionary)
