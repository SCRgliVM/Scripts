import os,re

for x in os.listdir():
    if re.search("x86_64-w64-mingw32-", x):
        y = x.replace("x86_64-w64-mingw32-", "").replace(".exe", "")
        print("\\    "+y+"=\""+x+"\"")
