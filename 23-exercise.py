# exercise-1
winning_number=17
your_input=int(input("guess a number between 1 and 100: "))
if your_input==winning_number:
    print("you won")
else:#nested if else
    if your_input<winning_number:
        print("too low") 
    else:
        print("too high")    