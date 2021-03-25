import os

filename = input("Enter file to modify: ")
string=""
with open(filename, "r") as fs:
    string = fs.read()

string = string.replace("p", "b")

with open(filename, "w") as fo:
    fo.write(string)
    fo.close()

os.system("python " + filename)