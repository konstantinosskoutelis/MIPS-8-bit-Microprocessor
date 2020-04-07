f = open("./8bit_hex_input.dat", "r")
contents = f.readlines()
finalString = []
number = 0
relations = [ ('0','0000'),('1','0001'),('2','0010'),('3','0011'),('4','0100'),('5','0101'),('6','0110'),('7','0111'),('8','1000'),('9','1001'),('a','1010'),('b','1011'),('c','1100'),('d','1101'),('e','1110'),('f','1111')  ]

def getHex(character):
    for item in relations: 
        temp =item[item[0] == character] 
        if len(temp)>1:
            return temp
def writeFile(listInput):
    f1=open('./32bit_binary_output.dat', 'a')
    for content in finalString: 
        content = str(content).replace(" ","")
        f1.write(content + "\n")


for line in contents:
    finalString.append('')
    for character in line:
        temp = getHex(character)
        if(str(temp).isnumeric()):
            finalString[number] += " " + str(getHex(character))
    number+=1

writeFile(finalString)


