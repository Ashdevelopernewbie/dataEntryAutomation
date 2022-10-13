
# myfile = open("lorem.txt", 'rt')
# contents = myfile.read()
# myfile.close()
# print(contents)

# This method reads the text file at whole
# This is bad for bigger text files
# with open ('lorem.txt', 'rt') as myFile:
#     contents = myFile.read()
# print(contents)

with open ("lorem.txt", "rt") as myFile:
    for myFile in myFile:
        if 'ipsum' in myFile:
            print('Found')
            break
        break