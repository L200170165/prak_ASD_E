import re

wiki = open("indonesia.txt", "r")
teks = wiki.read()
wiki.close()

print(re.findall(r'me\w+', teks.lower()))
