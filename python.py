import random


input("pick a number from 1-100 and hit enter (DO NOT TYPE): ")
input("add the same number that you picked and hit enter (DO NOT TYPE): ")

#add logic to genrate random number then removing odd number
my_number = random.randint(1,100)
if my_number % 2 == 1:
    my_number -= 1
print(my_number)

input("add the above number and hit enter (DO NOT TYPE): ")
input("Now minus the half from totel you have and hit enter (DO NO" \
"T TYPE): ")
input("Minus the same number you added in beginning and hit enter (DO NOT TYPE): ")

#formula to calculate the answer
answer = my_number / 2

print(f"The answer is -> {answer} 😊")