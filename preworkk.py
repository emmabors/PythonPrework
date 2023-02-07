# Question 1

def hello_name(user_name):
   """Prints hello_USERNAME"""
USERNAME = input("Enter your username:")
print("Hello_" + USERNAME + "!")

# Question 2

def first_odds():
   """Prints odd numbers from 1-100"""
numbers = list(range(0,101))
only_odd = [
   num for num in numbers if num % 2 == 1
   ]
print(only_odd)

first_odds()

# Question 3
def max_num_in_list(a_list):
   """return the max number of a given list"""
a_list = (1,2,3,4,5,6,7,8,9,10)
print(max(a_list))

max_num_in_list(a_list)

# Question 4
def is_leap_year(a_year):
   """Is the given year a leap year"""
given_year = (2023)
if given_year % 4 == 0 and given_year % 400 == 0 and given_year % 100 ==1:
    print('true')
else:
    print('false')

is_leap_year(given_year)

# Question 5
def is_consecutive(a_list):
   """does a list contain consecutive numbers"""
numbs = [1,2,3,4,5]
for num in a_list:
   if num == max(numbs) - 1:
        break
   print(num)