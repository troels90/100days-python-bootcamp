import art

print(art.logo)

def add(n1 ,n2):
  return n1 + n2

def multiply(n1, n2):
  return n1*n2

def subtract(n1, n2):
  return n1-n2

def divide(n1, n2):
  return n1/n2

operations = {
  "+":add,
  "*":multiply,
  "-":subtract,
  "/":divide
}

def calculator():
  num1 = float(input("What is the first number: "))
  for symbol in operations:
      print(symbol)
  calculating = True
  
  while calculating:
  
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the second number: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} =  {answer}")
    proceed = input("You want to continue calculating with {answer} | y / n | : ").lower()
    if proceed == "n":
      calculating = False
      calculator()
    else:
      num1 = answer
  
calculator()