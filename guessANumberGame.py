import random

print("***This is a geussing a number game that prompts user to pick a number***")
print("***Then propmts to do some additions, division and subtractions***")
print("***At the end it guesses the number that could be the answer***")
print()

input("Think of a number from 1-100 and hit enter (DO NOT TYPE): ")
input("add the same number that you picked and hit enter (DO NOT TYPE): ")

#add logic to genrate random number then removing odd number
my_number = random.randint(1,100)
if my_number % 2 == 1:
    my_number -= 1
print(my_number)

input("add the above number and hit enter (DO NOT TYPE): ")
input("Now devide the totel you have by 2 and hit enter (DO NOT TYPE): ")
input("Minus the number you picked in beginning and hit enter (DO NOT TYPE): ")

#formula to calculate the answer
answer = my_number / 2

print(f"The answer is -> {answer} 😊")

