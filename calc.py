def calculator():
     print("this is a simple calculator")
     print("this application is a simple calculator that performs simple operation")

     print("below are the operations you can perform")
     print("addition","subtraction","multiplication","division")

     print("A for Addition")
     print("B for Subtraction")
     print("C for Multiplication")
     print("D for Division")

     operation = input().upper()
     
     first_value = int(input("choose your first number\n"))
     second_value = int(input("choose your second number\n"))

     if operation == "A":
          print(first_value + second_value)
     elif operation == "B":
          print(first_value - second_value)
     elif operation == "C":
          print(first_value * second_value)
     elif operation == "D":
          print(first_value / second_value)
          try:
          except:
          
            