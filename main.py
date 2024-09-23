logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#calculator
#add
def add(n1,n2):
  return n1+n2
#subtract
def subtract(n1,n2):
  return n1-n2
#multiply
def multiply(n1,n2):
  return n1*n2
#divide
def divide(n1,n2):
  return n1/n2
operations={"+":add,
            "_":subtract,
            "*":multiply, 
            "/":divide}  
def calculator():
    print(logo)
    num1=float(input("what is the first number?"))
    for symbol in operations:
      print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol=input("pick an operation:")
        num2=float(input("what is the second number?"))
        calculation_funtion=operations[operation_symbol]
        first_answer=calculation_funtion(num1,num2)
        print(f" {num1} {operation_symbol} {num2} = {first_answer}")
        #End of the first opration:
        if input(f"type 'y' to continue calculating with or type 'n' to start new calculation:")=="y":
            num1=first_answer
        else:
          should_continue=False
          calculator()
calculator()         
