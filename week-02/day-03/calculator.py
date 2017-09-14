# Create a simple calculator application which does read the parameters from the prompt 
# and prints the result to the prompt. 

# It should support the following operations: 
# +, -, *, /, % and it should support two operands. 

# The format of the expressions must be: {operation} {operand} {operand}. 
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit

def expression_input():
    print("Please enter the expression (e.g. + 4 4): " )
    exp = [x for x in input().split()]
    return exp

def calculation (expression):
    if expression[0] == "+":
        return int(expression[1]) + int(expression[2])
    elif expression[0] == "-":
        return int(expression[1]) - int(expression[2])
    elif expression[0] == "*":
        return int(expression[1]) * int(expression[2])
    elif expression[0] == "/":
        return int(expression[1]) / int(expression[2])
    elif expression[0] == "%":
        return int(int(expression[1]) % int(expression[2]))
    else:
        print("This function is supported.")

print(calculation(expression_input()))