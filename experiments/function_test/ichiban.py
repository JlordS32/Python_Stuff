import random
import time

print("Welcome to Ichiban Kuji!")

seconds = 1

A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []

Figure = 0

for i in range(3):
    A.append("A = Figure")
for i in range(1):
    B.append("B = Figure")
for i in range(22):
    C.append("C = Signature Board")
for i in range(14):
    E.append("E = Rubber Charm")
for i in range(0):
    F.append("F = Note")
for i in range(0):
    G.append("G = Mini Plate")
for i in range(0):
    H.append("H = Folder Set")

figure_class = A + B

result = A + B + C + D + E + F + G + H

tickets = int(input("\nHow many tickets? "))

print("\nHere are your prizes: ")
print("----------------------")
for i in range(tickets):
    time.sleep(seconds)
    x = random.choice(result)
    result.remove(x)
    if x in figure_class:
        Figure += 1
    print(x)
if Figure == 0:
    print("\nNo figures unfortunately, better try again next time.")
elif Figure == 1:
    print("\nCongratulations! You just won {} figure.".format(Figure))
else:
    print("\nCongratulations! You won {} figures.".format(Figure))



