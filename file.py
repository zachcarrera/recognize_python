num1 = 42  # variable declaration
num2 = 2.3  # variable declaration
boolean = True  # variable declaration
string = 'Hello World'  # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos',
                  'Cheese', 'Olives']  # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37,
          'is_balding': False}  # variable declaration, initialize dict
# variable declaration, initialize tuple
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))  # log type check
print(pizza_toppings[1])  # log statement, access list value
pizza_toppings.append('Mushrooms')  # add list value
print(person['name'])  # log statement, access dict value
person['name'] = 'George'  # change dict value
person['eye_color'] = 'blue'  # add dict value
print(fruit[2])  # access tuple value

if num1 > 45:  # if statement
    print("It's greater")  # log statement
else:  # else
    print("It's lower")  # log statement

if len(string) < 5:  # if statement, get string length
    print("It's a short word!")  # log statement
elif len(string) > 15:  # else if statement, get string length
    print("It's a long word!")  # log statement
else:  # else statment
    print("Just right!")  # log statement

for x in range(5):  # for loop start
    print(x)  # log statement
for x in range(2, 5):  # for loop start
    print(x)  # log statement
for x in range(2, 10, 3):  # for loop start, from 2 to 9 step by 3
    print(x)  # log statment
x = 0  # variable declaration
while (x < 5):  # while loop start
    print(x)  # log statement
    x += 1  # increment x

pizza_toppings.pop()  # list delete value at end
pizza_toppings.pop(1)  # list delete value at 1

print(person)  # log statement
person.pop('eye_color')  # dict remove key value pair
print(person)  # log statment

for topping in pizza_toppings:  # for loop start
    if topping == 'Pepperoni':  # if statement
        continue  # continue (start next loop immediately)
    print('After 1st if statement')  # log statement
    if topping == 'Olives':  # if statment
        break  # break loop


def print_hello_ten_times():  # function definition
    for num in range(10):  # for loop start
        print('Hello')  # log statement


print_hello_ten_times()  # function call


def print_hello_x_times(x):  # function definition with one parameter
    for num in range(x):  # fir loop start
        print('Hello')  # log statement


print_hello_x_times(4)  # function call with one argument


# function call with paramater with default value
def print_hello_x_or_ten_times(x=10):
    for num in range(x):  # for loop start
        print('Hello')  # log statement


print_hello_x_or_ten_times()  # function call
print_hello_x_or_ten_times(4)  # function call with one argument


"""
Bonus section
"""

# print(num3) ---- NameError: name <variable name> is not defined ----
# num3 = 72
# fruit[0] = 'cranberry' ---- TypeError: 'tuple' object does not support item assignment ----
# print(person['favorite_team']) ---- KeyError: 'favorite_team' ---
# print(pizza_toppings[7]) ----- IndexError: list index out of range ----
#   print(boolean) ---- IndentationError: unexpected indent ----
# fruit.append('raspberry') ---- AttributeError: 'tuple' object has no attribute 'append' ----
# fruit.pop(1) ---- AttributeError: 'tuple' object has no attribute 'pop' ----
