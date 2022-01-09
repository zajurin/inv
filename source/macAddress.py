import subprocess

result = subprocess.run("ipconfig /all", capture_output=True, text=True).stdout
# str_result = result.stdout.decode('utf-8')
# print(result)

myWord = "Wireless LAN adapter Wi-Fi:"

print(result)

if myWord in result:
    print("I saw it")


# lines = [line.startswith(myWord) for line in result]
# for line in lines:
#     for word in line.split(" "):
#         if word.startswith(myWord):
#             print(word)


# if "Wireless LAN adapter Wi-Fi:" in result:
#     print("I saw it")
