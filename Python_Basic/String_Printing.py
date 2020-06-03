## Print formatting
# We'll check out 3 ways to format print statements.
# String interpolation using format and f'strings
# and simple usage of comma
# String Interpolation: String interpolation is embedding variables
# or other objects to be evaluated within the String

stock_price = 1100
print("Today's price for google stock is:", stock_price)
print("Today's price for google stock is: {}".format(stock_price))
print(f"Today's price for google stock is: {stock_price}")

# We can interpolate multiple values
today_price = 1100
yesterday_price = 1000
print("Today's price:", today_price, "yesterday's price:", yesterday_price)
print("Today's price: {}, yesterday's price: {}".format(today_price, yesterday_price))
print(f"Today's price: {today_price}, yesterday's price: {yesterday_price}")

# Special characters
# \ - is an escape character, it escapes the special character
# following it in a string
# \n - species new line within the string
# \t - adds a tab in it's place within the string
print("My name is jon snow and not only do I know nothing but I also do nothing")

# This statement can be broken into multiple lines with \
print("My name is jon snow and \
not only do I know nothing but \
I also do nothing")

# \n can be used to print in multiple lines with
print("My name is jon snow\nI know nothing\nI also do nothing")

# \t can be used to introduce tabs in the lines
print("My name is jon snow\n \tI know nothing\n\t\tI also do nothing")

# \t usage elsewhere
print("My name is jon snow\n\tI know\t\tNOTHING\n\t\tI also DO nothing")

# \ can be used to escape the special character meaning
print("I'm using the \\n special character to create new lines")
