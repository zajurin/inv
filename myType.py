import subprocess as sp
import psutil

# command = 'wmic path softwareLicensingService get OA3xOriginalProductKey'
# print('')
# y = sp.getoutput(command)
# print(type(y))

ram_Bytes = psutil.virtual_memory().total
ram_GB = ram_Bytes / 1000000
print(ram_GB)