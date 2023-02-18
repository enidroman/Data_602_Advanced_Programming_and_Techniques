'''
Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.
'''

# The below structure can be modified to answer this question.

def meal_suggestion():
  actions = ["breakfast", "lunch", "dinner"]
  user_input = input(f"What meal will you be having out of {actions}?: ")
  if user_input == "breakfast":
    print("Perhaps you should try a meal of boiled eggs with black coffee")
  elif user_input == "lunch":
    print("Perhaps you should try a meal of a ham and cheese sandwich")
  elif user_input == "dinner":
    print("Perhaps you should try a meal of smoked salmon over rice")
  else:
    print("That meal doesn't exist, please try again.")

meal_suggestion()
## What meal will you be having out of ['breakfast', 'lunch', 'dinner']?: lunch
## Perhaps you should try a meal of a ham and cheese sandwich

'''
Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20. 
You should take in the user’s input for the number of hours worked, and their rate of pay.
'''

def payroll(hours_worked = -1, pay_rate = -1):
  if hours_worked == -1 and pay_rate == -1:
    hours_worked = float(input("Please enter your hours worked: "))
    pay_rate = float(input("Please enter your rate of pay: "))
  if hours_worked > 20:
    pay = (1.5 * (hours_worked-20) * pay_rate) + (20 * pay_rate)
    print(f"Your pay for this week is {pay}")
  else:
    pay = hours_worked * pay_rate
    print(f"Your pay for this week is {pay}")

payroll(25,10)
## Your pay for this week is 275.0
payroll()
## Please enter your hours worked: 4
## Please enter your rate of pay: 19
## Your pay for this week is 76.0

'''
Q3: Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.
'''

def times_ten(argument):
  print(argument*10)

times_ten(10)
## 100


'''
SQ4: Find the errors, debug the program, and then execute to show the output.

def main()
      Calories1 = input( "How many calories are in the first food?")
      Calories2 = input( "How many calories are in the first food?")
      showCalories(calories1, calories2)

def showCalories()   
   print(“The total calories you ate today”, format(calories1 + calories2,.2f))
'''

## Moved indents within main back twice as they were too far out and python is indent sensitive.
## Changed calories 2 to display second food in the input prompt.
## Python is case sensitive so calories in showCalories need to be capitalized.
## Changed calories to integers since input returns strings.
## Fixed the format of how the format method should be used. Including removing the .2f.
## Fixed the psuedo-quotation marks that were not the typical ones used to create a string.
## Added colons to fix the function definitions.
## Called main() to run the function.
## Added arguments to showCalories
def main():
  Calories1 = int(input("How many calories are in the first food? "))
  Calories2 = int(input("How many calories are in the second food? "))
  showCalories(Calories1, Calories2)

def showCalories(Calories1,Calories2):
   print("The total calories you ate today {}".format(Calories1 + Calories2))

main()
## How many calories are in the first food? 10
## How many calories are in the second food? 20
## The total calories you ate today 30

'''
Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
         1/30 + 2/29 + 3/28 ............. + 30/1
'''

def sum_of_fractions(min,max):
  summation = 0
  # series = [0 for x in range(min,max+1)]
  for x in range(min,max+1):
    # series[x-1] += (x)/(max-(x-1))
    summation += (x)/(max-(x-1))
  # return series
  return summation

min = 1
max = 30

# series = sum_of_fractions(min,max)
# print(summation)
# [0.03333333333333333, 0.06896551724137931, 0.10714285714285714, 0.14814814814814814, 0.19230769230769232, 0.24, 0.2916666666666667, 0.34782608695652173, 0.4090909090909091, 0.47619047619047616, 0.55, 0.631578947368421, 0.7222222222222222, 0.8235294117647058, 0.9375, 1.0666666666666667, 1.2142857142857142, 1.3846153846153846, 1.5833333333333333, 1.8181818181818181, 2.1, 2.4444444444444446, 2.875, 3.4285714285714284, 4.166666666666667, 5.2, 6.75, 9.333333333333334, 14.5, 30.0]
# print(sum(summation))
# 93.84460105853213

summation = sum_of_fractions(min,max)
print(summation)
## 93.84460105853213
print(round(summation,2))
## 93.84

'''
Q6: Write a function that computes the area of a triangle given its base and height.
The formula for an area of a triangle is:
AREA = 1/2 * BASE * HEIGHT

For example, if the base was 5 and the height was 4, the area would be 10.
triangle_area(5, 4)   # should print 10
'''

# The function below can be modified to only display the area

def triangle_calc(base = 0,height = 0):
    if base == 0 and height == 0:
      base = float(input("Please enter the base of your triangle: "))
      height = float(input("Please enter the height of your triangle: "))
    area = (1/2)*base*height
    print(f"A {base} by {height} triangle has an area of {area}")

triangle_calc(5,4)
## A 5 by 4 triangle has an area of 10.0
triangle_calc()
## Please enter the base of your triangle: 1.5
## Please enter the height of your triangle: 5.5
## A 1.5 by 5.5 rectangle has an area of 4.125