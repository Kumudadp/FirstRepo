def calc(op,num1,num2):
  if op == '+':
    return num1 + num2
  elif op == '-':
    return num1 - num2
  elif op == '*':
    return num1 * num2
  elif op == '/':
    return num1 / num2
  elif op == '%':
    return num1 % num2
  elif op == '**':
    return num1 ** num2
  elif op == '5':
    i = int(input("which output do you want:"))
    if (i>n):
      print("invalid input")
    else:
      print(result[i-1])
      #for i, output in enumerate(result):
       #  print(f"output:{output}")
  else:
    return 0
result = []
while True:
 n=int(input(f"enter how many times the operation you want to perform:"))
 for _ in range(n):
  
    print("welcome to the calculator")
    print("enter '+' for addition")
    print("enter '-' for subtraction")
    print("enter '*' for multiplication")
    print("enter '/' for division")
    print("enter '%' for modulus")
    print("enter '**' for exponentiation")
    print("enter '5' for memory function")
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    op=input("enter the operator:")
    output=calc(op,num1,num2)
    print(output)
    result.append(output)
 print(result)
 
 continue_calculation = input("Do you want to perform more calculations? (yes/no): ").lower()
 if continue_calculation != 'yes':
      break
 
  
