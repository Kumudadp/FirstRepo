def calc(op, num1, num2):
  if op == '+':
    return num1 + num2
  elif op == '-':
    return num1 - num2
  elif op == '*':
    return num1 * num2
  elif op == '//':
    return num1 // num2
  else:
    return 'Invalid operator'


while True:
  print("Enter '+' for addition")
  print("Enter '-' for subtraction")
  print("Enter '*' for multiplication")
  print("Enter '//' for division")
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  op = input("operator:")
  output = calc(op, num1, num2)
  print("Result:", output)
