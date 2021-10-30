operand_1 = input("Enter operand one : ")
operand_2 = input("Enter operand two : ")
operator = input("Enter operator(+/-/*//) : ")

if(operator == "+"):
  return operand_1 + operand_2
elif(operator == "-"):
  return operand_1 - operand_2
elif(operator == "*"):
  return operand_1 * operand_2
elif(operator == "/"):
  return operand_1 / operand_2
print("Thank You!")
