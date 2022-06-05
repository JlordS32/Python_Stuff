import random
import time

print("Welcome to Ichiban Kuji!")

seconds = 2

A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []

Figure = 0

for i in range(4):
    A.append("A = Figure")
    B.append("B = Figure")
for i in range(1):
    C.append("C = Figure")
for i in range(13):
    E.append("E = Mug")
for i in range(14):
    F.append("F = Note")
for i in range(14):
    G.append("G = Mini Plate")
for i in range(0):
    H.append("H = Folder Set")

figure_class = A + B + C + D

result = A + B + C + D + E + F + G + H

tickets = int(input("\nHow many tickets? "))

print("\nHere are your prizes: ")
print("----------------------")
for i in range(tickets):
    # time.sleep(seconds)
    x = random.choice(result)
    if x in figure_class:
        Figure += 1
    print(x)
if Figure == 0:
    print("\nNo figures unfortunately, better try again next time.")
elif Figure == 1:
    print("\nCongratulations! You just won {} figure.".format(Figure))
else:
    print("\nCongratulations! You won {} figures.".format(Figure))



