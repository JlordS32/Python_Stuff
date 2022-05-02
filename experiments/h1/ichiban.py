import random

figures = ["2", "4"]


for i in range(0, 10):
    i = random.randrange(1, 22)
    print(i)

if str(i) in figures:
    print("Congrats you just won {} prizes".format(figures))
elif str(i) in figures[0]:
    print("You won prize A.")
elif str(i) in figures[1]:
    print("You won prize B.")
else:
    print("Better luck next time.")