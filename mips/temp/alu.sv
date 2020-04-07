module ALU(
  input [7:0] Operand1,Operand2,
  input E,
  input [3:0] Mode,
  input [3:0] CFlags,
  output[7:0] Out,
  output[3:0] Flags
//Z(Zero), C(Carry), S(Sign),O(Overflow) bits, from MSB to LSB connected to status register
);

logic Z,S,O;
logic CarryOut;
logic [7:0] Out_ALU;

always@(*)
begin
  case(Mode)
  4'b0000: {CarryOut,Out_ALU} = Operand1+Operand2;//addition
  4'b0001: 
  begin
    Out_ALU = Operand1 - Operand2;//subtraction
    CarryOut = !Out_ALU[7]; //
  end
  4'b0010: Out_ALU = Operand1;
  4'b0011: Out_ALU = Operand2;
  4'b0100: Out_ALU = Operand1 & Operand2; // AND
  4'b0101: Out_ALU = Operand1 | Operand2; //OR
  4'b0110: Out_ALU = Operand1 ^ Operand2; //XOR
  4'b0111: 
  begin
    Out_ALU = Operand2 - Operand1;
    CarryOut = !Out_ALU[7];  
  end
  4'b1000: {CarryOut, Out_ALU} = Operand2 + 8'h1;
  4'b1001:
  begin
    Out_ALU = Operand2 - 8'h1;
    CarryOut = Out_ALU[7];
  end
  4'b1010: Out_ALU = (Operand2 << Operand1[2:0]) | (Operand2 >> Operand1[2:0]);
  4'b1011: Out_ALU = (Operand2 >> Operand1[2:0]) | (Operand2 << Operand1[2:0]);
  4'b1100: Out_ALU = Operand2 << Operand1[2:0];
  4'b1101: Out_ALU = Operand2 >> Operand1[2:0]; // returns unsigned
  4'b1110: Out_ALU = Operand2 >>> Operand1[2:0]; //sign extension - returns signed
  4'b1111: 
  begin
    Out_ALU = 8'h0 - Operand2;
    CarryOut = !Out_ALU[7];
  end
  default: Out_ALU = Operand2;
  endcase
end

assign O = Out_ALU[7]^Out_ALU[6];
assign Z = (Out_ALU ==0)?1'b1: 1'b0;
assign S = Out_ALU[7];
assign Flags = {Z,CarryOut,S,O};
assign Out = Out_ALU;
endmodule





















