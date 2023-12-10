def add(a,b):
    answer = int(a) + int(b)
    print(str(a) + "+" + str(b) + "=" + str(answer) + "\n")

def sub(a,b) :
    answer = int(a) - int(b)
    print(str(a) + '-'+ str(b) + '=' + str(answer) + "\n")

def mul(a,b):
    answer = int(a) * int(b)
    print(str(a) + '* '+ str(b) + '=' + str(answer) + "\n")

def div(a,b):
    answer = int(a) / int(b)
    print(str(a) + '/'+ str(b) + '=' + str(answer) + "\n")

while True:
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Quit")

    option = input("Choose an option:")

    if option == "a" or option == "A":
        a = input("Select your first number:")
        b = input ("Select your second number")
        result = add(a,b)
    elif option == "b" or option =="B":
        a = input("Select your first number:")
        b = input ("Select your second number")
        result = sub(a,b)
    elif option == "c" or option =="C":
        a = input("Select your first number:")
        b = input ("Select your second number")
        result = mul(a,b)
    elif option == "d" or option =="D":
        a = input("Select your first number:")
        b = input ("Select your second number")
        result = div(a,b)
    elif option == "e" or option == "E":
        print("Program ended")
        quit()