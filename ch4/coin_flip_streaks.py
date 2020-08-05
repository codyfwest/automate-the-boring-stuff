# Chapter 4: Coin Flip Streaks Practice Project
import random


flip_list = []
number_of_streaks = 0
current_streak = 0

for r in range(10000):
    for experiment_num in range(100):
        # Code that creates a list of 100 heads or tails values
        # Heads = 1 and Tails = 0
        if random.randint(0, 1) == 1:
            flip_list.append(1)
        else:
            flip_list.append(0)
        # Code that checks if there is a streak of 6 heads or tails in a row

    for x in range(1, len(flip_list)):
        if flip_list[x] == flip_list[x - 1]:
            current_streak += 1
        else:
            current_streak = 0

        if current_streak == 6:
            number_of_streaks += 1
            current_streak
    flip_list = []


print(number_of_streaks)
print('Chance of streak: %s%%' % (number_of_streaks / 100))
