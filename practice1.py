# practice 1
import random

num = random.randint(0, 100)


def odd_or_even(num):
    if num % 2 == 0:
        return "odd"
    else:
        return "even"


# # practice 2
number = int(input("Enter a number : "))


def result(number):
    Total = 0
    for num in number:
        Total += num
    return Total


# practice 3
text = input("enter your text :")
numbers = 0
character = 0

for word in text:
    if word == " ":
        continue
    elif word in "0123456789":
        numbers += 1
    else:
        character += 1
print(f"character : {character}  numbers : {numbers}")
