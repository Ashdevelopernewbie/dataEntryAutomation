PNR = []
with open ("file.txt", 'rt') as myfile:

    content = myfile
    for myline in myfile:
        if 'PNR' in myline:
            myline.append(myline.rstrip('\n'))
    for element in myline:
        print(element)