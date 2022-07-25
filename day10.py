def add(n1 , n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


calc = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div
}

num1 = int(input("Whats the num: "))
num2 = int(input("Whats the num: "))


for sign in calc:
    print(sign)

op = input("What sign do you want to use: ")


quick_maths = calc[op]
print(quick_maths(num1, num2))