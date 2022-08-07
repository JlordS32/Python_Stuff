import random
import time

a_prize = 2
b_prize = 2
c_prize = 1
d_prize = 1
e_prize = 1
f_prize = 1
g_prize = 22
h_prize = 25
i_prize = 25

prizes_dict = {
    "A": ["A Prize"]*a_prize,
    "B": ["B Prize"]*b_prize,
    "C": ["C Prize"]*c_prize,
    "D": ["D Prize"]*d_prize,
    "E": ["E Prize"]*f_prize,
    "F": ["F Prize"]*g_prize,
    "G": ["G Prize"]*h_prize,
    "I": ["H Prize"]*i_prize
}

all_prizes = []

for i in prizes_dict.keys():
    for x in prizes_dict[i]:
        all_prizes.append(x)

ticket_number = int(input("How many tickets: "))

for reward in range(ticket_number):
    user_prize = random.choice(all_prizes)
    all_prizes.remove(user_prize)
    time.sleep(1)
    print(user_prize)