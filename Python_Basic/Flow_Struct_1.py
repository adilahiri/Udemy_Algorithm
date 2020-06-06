## Branching and controlling the execution flow of programs
## using if/elif/else blocks and conditional tests

# Documentation on conditional operators can be found here:
# https://docs.python.org/3/library/stdtypes.html#comparisons

# Below is the multiplication/division program from the video

print("Welcome to the calc program")
print("-"*30)
choice = input("Choose 1 to multiply, 2 to divide-> ")
if choice == "1" or choice =="2":
    num_1 = int(input("Enter first number-> "))
    num_2 = int(input("Enter second number-> "))
    if choice == "1":
        print(f"{num_1} multiplied by {num_2} is: {num_1*num_2}")
    else:
        print(f"{num_1} divided by {num_2} is: {num_1/num_2}")
else:
    print("You've made an invalid selection")
