while True:
    print("1. Add \n2. Subtract \n3. Multiply \n4. Divide")
    operation = int(input("Operation(1/2/3/4): "))
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    if operation == 1:
        result = num1 + num2
        print("Result:",result)
    elif operation == 2:
        print("Result:",num1-num2)
    elif operation == 3:
        print("Result:",num1*num2)
    elif operation == 4:
        print("Result:",num1/num2)
    else:
        print("Invalid Operation")
    con = input("Continue(y/n): ").lower
    if con == "y":
        pass
    elif con != "y":
        break