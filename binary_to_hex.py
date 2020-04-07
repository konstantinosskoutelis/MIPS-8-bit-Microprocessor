f = open("./IO_files/fibonacci_binary.dat", "r")
#print(f.read())
contents = f.readlines()
finalString = []
number = 0
relations = [ ('0','0000'),('1','0001'),('2','0010'),('3','0011'),('4','0100'),('5','0101'),('6','0110'),('7','0111'),('8','1000'),('9','1001'),('a','1010'),('b','1011'),('c','1100'),('d','1101'),('e','1110'),('f','1111')  ]

def writeFile(listInput):
    f1=open('./IO_files/8bit_hex_output.dat', 'a')
    f1.seek(0)#write at start of file
    f1.truncate()#move pointer at beginning of file to start writing
    for content in listInput: 
        content = str(content).replace(" ","")
        f1.write(content + "\n")

def binToHex(stringInput):
    num = 0
    for item in relations: 
        if (item[1] == stringInput):
            return(relations[num][0])
        num+=1

number = 0
for line in contents:
    finalString.append('')
    splittedString = [line[i:i+4] for i in range(0, len(line), 4)]
    for subString in splittedString:
        #print(subString + " " + str(binToHex(subString)))
        temp = str(binToHex(subString))
        if(temp!='None'):
            finalString[number]+= temp
    number+=1     
writeFile(finalString)
        