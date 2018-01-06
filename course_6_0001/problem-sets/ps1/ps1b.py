#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:31:49 2018
@author: angelichorsey


Problem Set 1
Part B: Saving, with a raise

In part A, we unrealistically assumed that your salary didn't change. But you
 are an MIT graduate, and clearly you are going to be worth more to your
 company over time! So we are going to build on your solution to Part A by
 factoring in a raise every six months. Copy Part A and modify with the
 following:
     Have the user input a semi-annual salary raise semi_annual_raise (as a
     decimal percentage).
     After every 6th month, increase your salary by that percentage.

 Write a program to calculate how many months it will take you to save up
 enough money for a down patment. Like before, assume that your investments
 earn a return of r - 0.04 (or 4%) an the required down patment percentage is
 0.25 (or 25%).

HINTS

Retrieve user input.
Assume users enter valid input.
Initialize some state variables. You should decide what information you need.
Be careful about annual amount and monthly amounts
Be careful about WHEN you increase your salary. This should only happen AFTER
 months 6, 12, 18, and so on.

EXAMPLE OUTPUT

Enter your starting annual salary: 120000
Enter the percent of your salary to save, as a decimal: .05
Enter the cost of your dream home: 500000
Enter the semi-annual raise, as a decimal: .03
Number of months: 142
"""

# Begin assigning user inputs
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a\
 decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

# Set state variables and initializers (?)
portion_down_payment = 0.25
r = 0.04
current_savings = 0.0
months = 0

# We are looping until something occurs so a while loop that executes until
# our current savings is greater than the down payment needed, which is
# calculated using the product of total_cost and portion_down_payment.
while current_savings < total_cost*portion_down_payment:
    # Set monthly_salary inside loop where annual_salary is modified
    monthly_salary = annual_salary/12
    # Increase current_savings by the portion saved each month and the ROI
    current_savings += monthly_salary*portion_saved+current_savings*r/12
    # Increment months...
    months += 1
    # Modify annual_salary last so it's applied to the month after
    if months % 6 == 0:
        annual_salary += annual_salary*semi_annual_raise

# Some comments are unnecessary
print('Number of months:', months)
