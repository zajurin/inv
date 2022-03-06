import time
import subprocess as sp
import re
import platform

azureDictionary = {}

list_to_search = ["AzureAdJoined : ", "AzureAdPrt : ",
                  "IsDeviceJoined : ", "IsUserAzureAD : "]
# Final Operating System
final_os = platform.system()
final_os_version = platform.release()
concatenate_os_version = f"{final_os} {final_os_version}"


class MyCommand:
    def __init__(self, command):
        self.command = command
        global myResult
        myResult = sp.getoutput(self.command)


class RemoveSpace_Colon:
    def __init__(self, stringWithSpaces, nameDB, result_to_send):
        self.stringWithSpaces = stringWithSpaces
        self.nameDB = nameDB
        self.result_to_send = result_to_send

        # changer = eachSearched + "NO"
        # print(changer)
        deleteSpace_eachSearched = re.sub(
            " +", "", self.stringWithSpaces)
        remove_Colon_eachSearched = deleteSpace_eachSearched.replace(
            ":", "")
        self.nameDB[remove_Colon_eachSearched] = self.result_to_send


def Runner():
    repeat_n_times = 1
    while repeat_n_times <= 2:
        for eachSearched in list_to_search:
            try:
                myInstance = MyCommand("dsregcmd /status")
                # change number between parenthesis to "360" for 6 minutes
                time.sleep(1)

                if eachSearched + "YES" in myResult:
                    print(eachSearched + "YES")
                    deleteSpace_eachSearched = re.sub(" +", "", eachSearched)
                    remove_Colon_eachSearched = deleteSpace_eachSearched.replace(
                        ":", "")
                    azureDictionary[remove_Colon_eachSearched] = "YES"

                elif eachSearched + "NO" in myResult:
                    changer = eachSearched + "NO"
                    print(changer)
                    deleteSpace_eachSearched = re.sub(" +", "", eachSearched)
                    remove_Colon_eachSearched = deleteSpace_eachSearched.replace(
                        ":", "")
                    azureDictionary[remove_Colon_eachSearched] = "NO"
# ????????????????????? CHECKING SPACES in re.sub(" +", "", eachSearched) ?????????????????????????????????
                elif "Windows 10" in concatenate_os_version:
                    deleteSpace_eachSearched = re.sub(" +", "", eachSearched)
                    remove_Colon_eachSearched = deleteSpace_eachSearched.replace(
                        ":", "")
                    azureDictionary[remove_Colon_eachSearched] = "NO (Windows 10 is present. So check this laptop)"

                else:
                    # *** OOP ***
                    string_To_DB = "NOT present in {0}".format(
                        concatenate_os_version)
                    instanceOfRemoveSpace_Colon = RemoveSpace_Colon(
                        eachSearched, azureDictionary, string_To_DB)

                    # FUNCTIONAL PROGRAMMING
                    # deleteSpace_eachSearched = re.sub(" +", "", eachSearched)
                    # remove_Colon_eachSearched = deleteSpace_eachSearched.replace(
                    #     ":", "")
                    # azureDictionary[
                    #     remove_Colon_eachSearched] = f"NOT present in {concatenate_os_version}"
                    # print(changer)

# ?????????????????????????????????????????????????????????????????
            except Exception as e:
                print(f"***ERROR: {e}")
        repeat_n_times += 1
        statusNO = eachSearched + "NO"
        if repeat_n_times < 3 and statusNO:
            print(
                "\nSeems that one or more of the values was 'NO'.\nWe need to update this process ")
            print()
            updating = sp.getoutput("gpupdate /force")
            print(updating)
            minutes_to_wait = .1
            myTime = minutes_to_wait * 60
            print(f"Waiting {minutes_to_wait} minutes")
            timeInSeconds = time.sleep(myTime)
            print(f"\nTry number {repeat_n_times} \n")

        else:
            print(
                f"\n\n{repeat_n_times} is not lower than 3 or changer isn't NOT ")


Runner()
print(azureDictionary)
