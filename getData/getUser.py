import re
import time
import subprocess as sp


class RunCommand:
    def __init__(self, command):
        self.command = command
        global myResult
        myResult = sp.run(self.command, capture_output=True, text=True)
    # def getResult(self):
    #     self.myResult = myResult
        

user = RunCommand('whoami')

print(myResult.stdout)

# brand = RunCommand('wmic csproduct get name')
# model = RunCommand('wmic csproduct get name')
# serialNumber = RunCommand('wmic bios get serialnumber')
# macAddress = RunCommand('getmac /v')
# ram = RunCommand('')
# operatingSystem = RunCommand('')
# licence = RunCommand('')
# azureAdJoined = RunCommand('')
# azureAdPrt = RunCommand('')
# isDeviceJoined = RunCommand('')
# isUserAzureAD = RunCommand('')

# print(user, brand, model, serialNumber, ram, operatingSystem, licence, azureAdJoined, azureAdPrt, isDeviceJoined, isUserAzureAD, macAddress)

# searched = "1394 OHCI Compliant Ho Kernel2"
# def updating(myCommmand):
#     myupdateCode = sp.getoutput(myCommmand)
#     print(myupdateCode)

# try:
#     class RunDir:
#         def __init__(self, command):
#             self.command = command
#             # global myResult
#             myResult = sp.getoutput(self.command)
#             print(myResult)
#             if searched in myResult:
#                 time.sleep(3)
#                 print("I am waiting ...")
#                 updating("dir")
                   
#             else:
#                 whoisit = sp.getoutput("whoami")
#                 print("I did not saw it")
#                 print(f"in user {whoisit} ")

#     # myUsername = RunDir('whoami')
#     time.sleep(2)
#     myDir = RunDir('driverquery')
#     # myDir = RunDir('whoami')
# except:
#     print('Error')


# # print(myResult)

# # AzureAdJoined : YES
# # AzureAdPrt : YES
# # IsDeviceJoined : YES
# # IsUserAzureAD : YES