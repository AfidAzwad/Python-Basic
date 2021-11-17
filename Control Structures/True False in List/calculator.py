num1 = float(input("Enter a number: "))

num2 = float(input("Enter another number: "))




while True:
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(" : ")


   if user_input == "quit":
      break

   elif user_input == "add":

      result = str(num1 + num2)
      print("The answer is " + result)


   elif user_input == "sub":

      result = str(num1 -  num2)
      print("The answer is " + result)


   elif user_input == "mul":

      result = str(num1 * num2)
      print("The answer is " + result)


   elif user_input == "div":
      result = str(num1 / num2)
      print("The answer is " + result)

   else:
      print("Unknown input")