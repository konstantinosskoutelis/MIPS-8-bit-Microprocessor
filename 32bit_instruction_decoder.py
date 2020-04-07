f = open("./32bit_binary_output.dat", "r")
contents = f.readlines()

operations = [('00','R'),('01','I'),('10','J')]
functions = [('000','addition'),('001','subtraction'),('010','bitwise-and'),('011','bitwise-or'),('100','set-less-than'),('101','n/a')]
number =0


for line in contents:
    print("Line No " + str(number) + " : " + str(line))
    opcode =str(line)[:6] 
    if opcode == '000000':
        # print("R-type Instruction")
        op = operations[0]
        function = str(line)[6:12]
        if(function == '100000'):
            # print("Addition function")
            funct = functions[0]
        elif(function == '100010'):
            # print("Subtraction function")
            funct = functions[1]
        elif(function == '100100'):
            # print("bitwise-and function")
            funct = functions[2]
        elif(function == '100101'):
            # print("bitwise-or function")
            funct = functions[3]
        elif(function == '101010'):
            # print("set-less-than function")
            funct = functions[4]
                    


    elif opcode == '000010':
        # print("J-type Instruction")
        op = operations[2]
        funct = functions[5]
    else :
        # print("I-type Instruction")
        op = operations[1]
        funct = functions[5]
        
        


    
    
    if number == 0:
        break
    number += 1