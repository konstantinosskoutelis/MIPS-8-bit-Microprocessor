f = open("./32bit_binary_output.dat", "r")
contents = f.readlines()


number =0
for line in contents:
    print("Line No " + str(number) + " : " + str(line))
    opcode =str(line)[:6] 
    print("OPCODE: " + opcode)
    
    
    if number == 0:
        break
    number += 1