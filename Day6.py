def decorators(fun):
    def deno(num1, num2):
        if num1 < num2:
            num1, num2 = num2, num1
        return fun(num1, num2)

    return deno


@decorators
def div(num1, num2):
    return num1 // num2


num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
print(num1, num2)

print(div(num1, num2))