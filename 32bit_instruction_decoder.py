f = open("./32bit_binary_output.dat", "r")
contents = f.readlines()

operations = [('00','R'),('01','I'),('10','J')]
instructions_I = [('000','addi'),('001','beq'),('010','lb'),('011','sb')]
functions = [('000','addition','add'),('001','subtraction','sub'),('010','bitwise-and','and'),('011','bitwise-or','or'),('100','set-less-than','slt'),('101','n/a', 'n/a')]
number =0
instruction = []

def binaryToDecimal(binary):      
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return(decimal)     

def writeFile(listInput):
    f1=open('./8bit_hex_output.dat', 'a')
    for content in finalString: 
        content = str(content).replace(" ","")
        f1.write(content + "\n")


for line in contents:
    instruction.append('')  
    #print("Line No " + str(number) + " : " + str(line))

    opcode =str(line)[:6] 
    if opcode == '000000':
        # print("R-type Instruction")
        op = operations[0]
        function = str(line)[26:]
        ra = str(line)[6:11]
        rb = str(line)[11:16]
        rd = str(line)[16:21]
        ra_name = binaryToDecimal(int( 0 if ra.lstrip("0")=='' else ra.lstrip("0")  ))#in case it is reg 0, to return 0 and not throw an error
        rb_name = binaryToDecimal(int( 0 if rb.lstrip("0")=='' else rb.lstrip("0") ))
        rd_name = binaryToDecimal(int( 0 if rd.lstrip("0")=='' else rd.lstrip("0") ))

        if(function == '100000'):
            funct = functions[0]
        elif(function == '100010'):
            funct = functions[1]
        elif(function == '100100'):
            funct = functions[2]
        elif(function == '100101'):
            funct = functions[3]
        elif(function == '101010'):
            funct = functions[4]    
        #print(funct[1])        
        instruction[number] =funct[2] + " $" + str(rd_name) + ", $"+ str(ra_name) + ", $" + str(rb_name)


    elif opcode == '000010':
        # print("J-type Instruction")
        op = operations[2]
        funct = functions[5]
        dest = str(line)[6:]
        dest_name = binaryToDecimal(int(dest.lstrip("0")))
        instruction[number] = op[1] + " $dest("+str(dest_name)+")" 

    else :
        # print("I-type Instruction")
        op = operations[1]
        funct = functions[5]
        ra = str(line)[6:11]
        rb = str(line)[11:16]
        imm =str(line)[16:32]

        ra_name = binaryToDecimal(int( 0 if ra.lstrip("0")=='' else ra.lstrip("0")  ))#in case it is reg 0, to return 0 and not throw an error
        rb_name = binaryToDecimal(int( 0 if rb.lstrip("0")=='' else rb.lstrip("0") ))
        imm_name = binaryToDecimal(int( 0 if imm.lstrip("0")=='' else imm.lstrip("0") ))

        if opcode == '001000':
            funct_i = instructions_I[0]
            instruction[number] = funct_i[1] + " $"+str(rb_name)+", $"+ str(ra_name) +", "+ str(imm_name )

        elif opcode == '000100':
            funct_i = instructions_I[1]
            instruction[number] = funct_i[1] + " $"+str(rb_name)+", $"+ str(ra_name) +", "+ str(imm_name )

        elif opcode == '100000':
            funct_i = instructions_I[2]
            instruction[number] = funct_i[1] + " $"+str(rb_name)+", "+ str(imm_name) + " ($" + str(ra_name) + ")"

        elif opcode == '110000':
            funct_i = instructions_I[3]
            instruction[number] = funct_i[1] + " $"+str(rb_name)+", "+ str(imm_name) + " ($" + str(ra_name) + ")"  
    
    number += 1


print(instruction)

