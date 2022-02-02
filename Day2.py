lottery  = "hello coders"
# 'h' or 'e' or 'o' or 'c' or 'd'
print("choose correct character of the word '",lottery,"' to win the lottery")
inputs = input(" ")

if inputs == lottery[0].lower() or inputs == lottery[1].lower() or inputs == lottery[4].lower() or inputs == lottery[6].lower() or inputs == lottery[8].lower():
    print("congratulations,you won the lottery!")
else:
    print("sorry, You didn't win the lottery")