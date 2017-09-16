# Author: Ahmad Bilal Khalid (ABK)
# This program is provided for free of cost and have no guarrentee of any kind.

def draw(labels, values):
    for l in range(len(labels)):
        print(labels[l])

        for v in range(len(values[l])):
            if values[l][v] == '1':
                print(u"\u2588", end='')
            else:
                print("_", end='')
        print("")
    
filename = input("Enter file name: ")
file = open(filename, "r")

line = file.readline()
line = line.strip()
labels = line.split(chr(9))

values = []
for label in labels:
    values.append(list())

line = file.readline()
while line != "":
    fmtline = line.strip(chr(10)) # To remove \n
    fmtline = fmtline.replace(chr(9), '') # To remove \t
    for c_index in range(len(fmtline)):
        values[c_index].append(fmtline[c_index])
    line = file.readline()


draw(labels, values)
