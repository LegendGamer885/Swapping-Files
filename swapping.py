def swapFileData():
    file1 = input("Enter first file name ")
    file2 = input("Enter Second File name ")

    with open(file1,"r") as FileA:
        data_A = FileA.read()
    
    FileB = open(file2)
    data_B = FileB.read()

    writeA = open(file1,"w")
    writeA.write(data_B)

    writeB = open(file2,"w")
    writeB.write(data_A)

swapFileData()