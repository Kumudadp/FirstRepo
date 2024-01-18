def calc(op, num1, num2):
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
  else:
    return 'Invalid operator'

result = []
while True:
  n=int(input(f"enter how many times the operation you want to perform:"))
  for _ in range(n):
    print("welcome to calculator")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("enter '%' for modulus")
    print("enter '**' for exponentiation")
    print("enter '5' for memory function")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("operator:")
    output = calc(op, num1, num2)
    print("Result:", output)
    result.append(output)
  print(result)
 
 continue_calculation = input("Do you want to perform more calculations? (yes/no): ").lower()
 if continue_calculation != 'yes':
      break
 
