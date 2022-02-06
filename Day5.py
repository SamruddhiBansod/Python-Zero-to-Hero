mylist = list(range(1, 50))

result3 = list(filter(lambda x: (x % 3 == 0), mylist))
result5 = list(filter(lambda x: (x % 5 == 0), mylist))

print("This number only divisible by 3 in 1-50 numbers : \n", result3)
print("This number only divisible by 5 in 1-100 number : ", result5)