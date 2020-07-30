# This sequence actually works for any integer and sooner or later, ends up returning a 1.
# Mathematicians aren't even sure why.
# The Collatz sequence is called "the simplest impossible math problem"

while True:
    try:
        print('Enter an integer: ')
        input_number = int(input())
        break
    except ValueError:
        print('Please enter a valid integer dingus!')


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


num_not_one = True
new_num = collatz(input_number)
while num_not_one is True:
    if new_num == 1:
        num_not_one = False
        print('Amazing! A 1 was returned!')
    else:
        new_num = collatz(new_num)
        print(new_num)
