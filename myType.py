import subprocess as sp
import psutil

ram_Bytes = psutil.virtual_memory().total
ram_GB = ram_Bytes / 1000000000
print(ram_GB)
