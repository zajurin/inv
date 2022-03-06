from distutils.util import change_root
import subprocess as sp
import re
# import time
import getmac
import platform
import psutil


def getFunction():
    dataDictionary = {}

    # list_to_search = ["AzureAdJoined : ", "AzureAdPrt : ",
    #                   "IsDeviceJoined : ", "IsUserAzureAD : "]
    username = sp.getoutput("whoami")
    checking_status = sp.getoutput("dsregcmd /status")
    my_model = sp.getoutput("wmic csproduct get name")
    mySerialNumber = sp.getoutput("wmic bios get serialnumber")
    myBrand = sp.getoutput("wmic csproduct get vendor")

    # Cleaning unwanted lines
    theUsername = username.replace("\n", "")
    theModel = my_model.replace("\n", "")
    theSerialNumber = mySerialNumber.replace("\n", "")
    theBrand = myBrand.replace("\n", "")

    # Remove multiple spaces in strings
    cleanUserName = re.sub(" +", " ", theUsername)
    cleanModel = re.sub(" +", " ", theModel)
    cleanSerialNumber = re.sub(" +", " ", theSerialNumber)
    cleanBrand = re.sub(" +", "", theBrand)
    ram_Bytes = psutil.virtual_memory().total

    # Remove extra words
    # Final Model, Serial Number, MAC Address, Brand and RAM
    finalModel = re.sub("Name ", "", cleanModel)
    finalSerialNumber = cleanSerialNumber.replace("SerialNumber ", "")
    finalmacAddress = getmac.get_mac_address()
    prev_finalBrand = re.sub("Vendor", "", theBrand)
    finalBrand = prev_finalBrand.strip()
    ram_GB = ram_Bytes / 1000000000

    # Final Operating System
    final_os = platform.system()
    final_os_version = platform.release()
    concatenate_os_version = f"{final_os} {final_os_version}"

    # sending data to Dictionary
    dataDictionary["username"] = cleanUserName
    dataDictionary["model"] = finalModel
    dataDictionary["serialNumber"] = finalSerialNumber
    dataDictionary["macAddress"] = finalmacAddress
    dataDictionary["operatingSystem"] = f"{final_os} {final_os_version}"
    dataDictionary["brand"] = finalBrand
    dataDictionary["ram"] = ram_GB

    print(f"userName: {cleanUserName}")
    print(f"Model: {finalModel}")
    print(f"Serial Number: {finalSerialNumber}")
    print(f"MAC ADDRESS: {finalmacAddress}")
    print(f"Operating System: {final_os} {final_os_version}")
    print(f"Brand: {finalBrand}")
    print(ram_GB)
    print()

    print(dataDictionary)
