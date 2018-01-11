#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:48:47 2018
@author: angelichorsey

Problem Set 1
Part C: Finding the right amount to save away

In part B, you had a chance to explore how both the percentage of your salary
 that you save each month and your annaul raise affect how long it takes you
 to save for a down payment. This is nice, but suppose you want to set a
 particular goal, e.g. to be able to afford the down payment in three years.
 How much should you save each month to achieve this? In this problem, you are
 going to write a program to answer that question. To simplify things, assume:
     1. Your semi-annual raise is .07 (7%)
     2. Your investments have an annual return of 0.04 (4%)
     3. The down payment is 0.25 (25%) of the cost of the house.
     4. The cost of the house that you are saving for is $1M.

 You are now going to try to find the best rate of savings to achieve a down
 payment on a $1M house in 36 months. Since hitting this exactly is a
 challenge, we simply want your savings to be within $100 of the required down
 payment.

 Write a program to calculate the best savings rate, as a function of your
 starting salary. You should use [bisection search] to help you do this
 efficiently. You should keep track of the number of steps it takes your
 bisections search to finish.

 Limit floats to two decimals of accuracy (i.e., we may want to save at 7.04% -
 or 0.0704 in decimal - but we are not going to worry about the delta between
 7.041% and 7.039%). This means we can search for an integer between 0 and
 10000 (using integer division), and then convert it to a decimal percentage
 (using float division) to use when we are calculating the current_savings
 after 36 months. Using this range gives us only a finite number of numbers
 that we are searching over, as opposed to the infinite number of decimals
 between 0 and 1. This range will help prevent infinite loops. The reason we
 use 0 to 10000 is to account for two additional decimal places in the range
 0% to 100%. Your code should print out a decimal (e.g. 0.0704 for 7.04%).

 Keep in mind that it may not be possible to save on a down payment in a year
 and a half for some salaries. In this case your function should notify the
 user that it is not possible to save for the down payment in 36 months with a
 print statement.

 NOTE: There are multiple right ways to implement bisection search/number of
 steps so your results may not perectly match those of the test case.

HINTS

Retrieve user input.
Assume users enter valid input.
Initialize some state variables. You should decide what information you need.
Be careful about annual amount and monthly amounts
Be careful about WHEN you increase your salary. This should only happen AFTER
 months 6, 12, 18, and so on.
There are multiple savings rates that uield a savings amount that is within
 $100 of the required down payment on a $1M house. In this case, you can just
 return any of the possible values.
Stopping condition and computing a trial value for bisection search may vary
 number of steps from example output.
Watch out for integer division when calculating if a percentage saved is
 appropriate and when calculating final decimal percentage savings rate.
Remember to reset the appropriate variable(s) to their initial values for each
 iteration of bisection search.

EXAMPLE OUTPUT

Enter the starting salary: 150000
Best savings rate: 0.4411
Steps in bisection search: 12
"""

# user input
annual_salary = float(input('Enter your annual salary: '))

# static variables and initializers
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000
steps = 0
current_savings = 0
low = 0
high = 10000
guess_rate = (high + low)//2
# Use a while loop since we check UNTIL something happens.
while abs(current_savings - total_cost*portion_down_payment) >= 100:
    # Reset current_savings at the beginning of the loop
    current_savings = 0
    # Create a new variable for use within the for loop.
    for_annual_salary = annual_salary
    # convert guess_rate into a float
    rate = guess_rate/10000
    # Since we have a finite number of months, use a for loop to calculate
    # amount saved in that time.
    for month in range(36):
        # With indexing starting a zero, we need to calculate at the beginning
        # of the loop.
        if month % 6 == 0 and month > 0:
            for_annual_salary += for_annual_salary*semi_annual_raise
        # Set monthly_salary inside loop where annual_salary is modified
        monthly_salary = for_annual_salary/12
        # Calculate current savings
        current_savings += monthly_salary*rate+current_savings*r/12
    # The statement that makes this a bisection search
    if current_savings < total_cost*portion_down_payment:
        low = guess_rate
    else:
        high = guess_rate
    guess_rate = (high + low)//2
    steps += 1
    # The max amount of guesses needed is log base 2 of 10000 which is slightly
    # above 13. Once it gets to the 14th guess it breaks out of the while loop.
    if steps > 13:
        break

# output
if steps > 13:
    print('It is not possible to pay the down payment in three years.')
else:
    print('Best savings rate:', rate)
    print('Steps in bisection search:', steps)
