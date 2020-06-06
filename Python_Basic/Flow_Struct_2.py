## Branching and control flow step by step

# Example of simple if/elif/else block
choice = '1'
if choice == '1':
    print('You have chosen option 1')
elif choice == '2':
    print('You have chosen option 2')
else:
    print('You have made an invalid choice')

# Example of boolean test - not operator
made_payment = True
a = 'Please pay monthly premium'
b = 'Welcome to your homepage'

if not made_payment:
    print(a)
else:
    print(b)

# Combining comparison operators and conditional tests
i = 20
j = 10
k = 30

if i < j and i < k:
    print("i is less than j and k")
elif i == j and i == k:
    print("i is equal to j and k")
else:
    print("i is greater than j")

# Example of ternary operator (simplifying if/else)
made_payment = True
a = 'Please pay monthly premium'
b = 'Welcome to your homepage'

print(a) if not made_payment else print(b)
print(b) if made_payment else print(a)
