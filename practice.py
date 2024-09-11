# first_name = input  ('Enter first name: ')
# last_name = input ('What is your lastname: ')
# # print ('Hello, ' + first_name.capitalize()  + ' ' +last_name.capitalize() )
# fullname = f'Hello, {first_name} {last_name}'
# print (fullname)


# Getting user input for first name and last name
# first_name = input('Enter first name: ')
# last_name = input('What is your last name: ')

# Using an f-string to format the output
# output = f'Hello, {first_name} {last_name}'

# # # Printing the formatted output
# # print(output)


# days_in_Feb = 28

# print(str(days_in_Feb ) +  ' total days in Feb')

# #date and time library
# from datetime import datetime
# current_time = datetime.now()
# print('the time and date is: ' + str(current_time))


# birthday = input('What is your birthday')

# province = input ('what state do you live in?: ')
# # tax = 0

# if province == 'Alberta' or province == 'Nunavut':
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15
#     print(tax)

#Complex conditions and using And - both conditions ave to be true
 # if gpa >= .85 and lowest_grade >= .70:
        #        print('Well Done')


gpa = float (input('Waht is your Grade Point Average? '))
lowest_grade = float(input('What is your lowest grade? '))


# nested if
# if gpa >= .85:
#     if lowest_grade >= .70:
#         print('you made the honour roll')


if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False 

if honour_roll:
 print('you made the honour roll')
       

#boolean flags
# can be = to true or false
# else
# example honour_roll = True
# honour_roll = False
# if gpa >= .85 and lowest_grade >= .70:


