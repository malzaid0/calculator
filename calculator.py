def main():
    # write your code here
    operations = ["+", "-", "/", "*"]

    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Choose the operation (+, -, /, *): ")

    if not num1.isdigit():
        print(num1 + " is not a valid number")
    elif not num2.isdigit():
        print(num2 + " is not a valid number")
    elif operation not in operations:
        print("operation is not valid")
    else:
        num1 = int(num1)
        num2 = int(num2)
        answer = 0
        if operation == operations[0]:
            answer = num1 + num2
        elif operation == operations[1]:
            answer = num1 - num2
        elif operation == operations[2]:
            answer = num1 / num2
        else:
            answer = num1 * num2
        print("The answer is %d" % answer)


if __name__ == '__main__':
    main()
