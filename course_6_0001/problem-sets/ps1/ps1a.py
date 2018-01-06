#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:56:56 2018
@author: angelichorsey

Problem Set 1
Part A: House Hunting

You have graduated from MIT and now have a great job! You move to the San
 Francisco Bay Area and decide that you want to start saving to buy a house.
 As housing prices are very high in the Bay Area, you realize you are going to
 have to save for several years before you can afford to make the down payment
 on a house. In Part A, we are going to determine how long it will take you to
 save enough money to make the down payment. Write a program to calculate how
 many months it will take you to save up enough money for a down payment. You
 will want your main variables to be floats, so you should cast user inputs to
 floats.

HINTS

Retrieve user input.
Assume users enter valid input.
Initialize some state variables. You should decide what information you need.
Be careful about annual amount and monthly amounts

EXAMPLE OUTPUT

Enter your annual salary: 120000
Enter the percent of your salary to save, as a decimal: .10
Enter the cost of your dream home: 1000000
Number of months: 183
"""

# Begin assigning user inputs and also calculate monthly salary
annual_salary = float(input('Enter your annual salary: '))
monthly_salary = annual_salary/12

# Is 78 width still really PEP8 compliant in 2017? Variable below looks gross
portion_saved = float(input('Enter the percent of your salary to save, as a\
 decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

# Set state variables and initializers (?)
portion_down_payment = 0.25
r = 0.04
current_savings = 0.0
months = 0

# We are looping until something occurs so a while loop that executes until
# our current savings is greater than the down payment needed, which is
# calculated using the product of total_cost and portion_down_payment.
while current_savings < total_cost*portion_down_payment:
    # Increase current_savings by the portion saved each month and the ROI
    current_savings += monthly_salary*portion_saved+current_savings*r/12
    # Increment months...
    months += 1

# Some comments are unnecessary
print('Number of months:', months)
