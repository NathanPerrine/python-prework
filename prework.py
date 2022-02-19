# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below. def hello_name(user_name):
def hello_username(user_name):
    """Take user_name, add to string and make it upper"""
    print(f"hello_{user_name.upper()}!")

hello_username("Nathan")
print("-----------")

# Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 
# and returns nothing def first_odds():
def first_odds():
    #either works, first counts by 2 starting at 1, second checks for a remainder if divided by 2
    #for num in range(1, 101, 2):
    #    print(num)
    for num in range(1, 101):
        if num % 2 == 1:
            print(num)

first_odds()
print("-----------")

# Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below. def max_num_in_list(a_list):
def max_num_in_list(a_list):
    print(max(a_list))

max_num = [1, 2, 3, 4, 555, 6, 7, 99, 10]
max_num_in_list(max_num)
print("-----------")

# Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):
def is_leap_year(a_year):
    # divisible by 4,       not divisible by 100, or is divisble by 400
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
        return True
    else:
        return False

print(is_leap_year(2000))
print(is_leap_year(2001))
print(is_leap_year(2002))
print(is_leap_year(2003))
print(is_leap_year(2004))
print(is_leap_year(2020))
print("-----------")

# Question 5
#Write a function to check to see if all numbers in the list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    # Checking for gaps also determins if the numbers are consecutive
    x = 0
    consecutive = False
    # Iterate over list
    for num in a_list: 
        # Check to see if going out of bounds
        # Since we're checking x + 1, we can't go past x - 1
        if x < len(a_list)-1:
            if num == a_list[x+1] - 1:
                consecutive = True
            else:
                consecutive = False
        x += 1
    return consecutive

num_list = [0, 1, 2, 3, 4, 5]
num_list0 = [1, 2, 3, 4, 5, 7]
print(is_consecutive(num_list))
print(is_consecutive(num_list0))