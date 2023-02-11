# Q1. What will the following code display?

numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])

# Can you debug and fix the output? The code should return the entire list

print(numbers[0:5])

# Q2. Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.

def sales_tracker():
  week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  tracker = {}
  for day in week:
    tracker[day] = int(input(f"Please enter the amount of sales for {day}: "))
  return tracker

tracker = sales_tracker()
print(tracker)

# Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
# alphabetical order

travel = ["Hawaii", "Paris", "Costa Rica", "Antartica", "France"]

#   ● Print your list in its original order.
print(travel)

#   ● Use the sort() function to arrange your list in order and reprint your list.
travel.sort()
print(travel)

#   ● Use the sort(reverse=True) and reprint your list.
travel.sort(reverse=True)
print(travel)

# Q4. Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.

number_room = {602:123, 605:256, 606:483, 607:523}
number_instructor_time = {602:["Schettini","6:00 PM EST"], 605:["Fulton", "6:30 PM EST"], 606:["Briar", "8:00 PM EST"], 607:["Catlin", "6:45 PM EST"]}

def course_summary():
  course_number = int(input("Please enter a course number: "))
  print(f"The course number {course_number} meets in room {number_room[course_number]} and has the instructor {number_instructor_time[course_number][0]} and meets at {number_instructor_time[course_number][1]}")

course_summary()

# Q5. Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. The program should then demonstrate the four options:
#   ● look up a person’s email address,
#   ● add a new name and email address,
#   ● change an existing email address, and
#   ● delete an existing name and email address.

name_email = {"Taha":"taha.ahmad25@sps.cuny"}
def name_email_call():
  actions = ["look up","add","change","delete"]
  user_input = input(f"Please choose an action out of {actions}: ")
  if user_input == "look up":
    print(name_email[input("Please enter the name whose email address you want to look up: ")])
  elif user_input == "add":
    new_name = input("Please enter the name of the user you would like to add: ")
    new_email_address = input(f"Please enter the email address of {new_name}: ")
    name_email[new_name] = new_email_address
    print(name_email)
  elif user_input == "change":
    change_name = input("Please enter the name of the user you would like to edit: ")
    change_email_address = input(f"Please enter the new email address of {change_name}: ")
    name_email[change_name] = change_email_address
    print(name_email)
  elif user_input == "delete":
    delete_name = input("Please enter the name of the user you would like to delete: ")
    del name_email[delete_name]
    print(name_email)
  else:
    print("That was an invalid command")
    exit()
name_email_call()