"""
Program:		CapstoneProject
Author:			Randall Rowland
Class:			IT-140-Q3788 Introduction to Scripting 18EW3
Instructor:		Angel D. Cross
Date:			18 Jan 2018
Description:    A program that takes the INPUT from a user on rental car
                information and calculates mileage used and cost. Finally,
                the program OUTPUTS a summary of the data INPUT'd and calculations
Input:          stdin
Output:         stdout


Known bugs/missing features:
    There is currently no input validation - User are capable of
    entering data that could break the code or produce erroneous data

Modifications:
Date                Comment
----    ------------------------------------------------
"""

# Global variables
budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00

'''
Section 1: Collect customer input
'''
rentalCode = raw_input('(B)udget, (D)aily, or (W)eekly rental?\n')

"""
Created functions to lump like data and variables together. This 
prevents several nested IF statements and prevents extra IF
statements later on within the calculation section. Otherwise
the calculation section would have to use nested IF statements
to determine rental time and assign correct rate/charge to the
calculations.
"""


def budget():
    global rentalPeriod
    global rate
    rentalPeriod = raw_input('Number of Days Rented:\n')
    rate = budget_charge


def daily():
    global rentalPeriod
    global rate
    rentalPeriod = raw_input('Number of Days Rented:\n')
    rate = daily_charge


def weekly():
    global rentalPeriod
    global rate
    rentalPeriod = raw_input('Number of Weeks Rented:\n')
    rate = weekly_charge


options = {'B' : budget,
           'D' : daily,
           'W' : weekly,
}

options[rentalCode]()


odoStart = raw_input('Starting Odometer Reading:\n')
odoEnd = raw_input('Ending Odometer Reading:\n')


'''
Section 2: Calculate the costs from the customer input
'''
baseCharge = float(rentalPeriod) * rate
totalMiles = int(odoEnd) - int(odoStart)

"""
Budget Category:
    To calculate the cost for a budget rental is the base rate per day
    plus $0.25 per mile driven
"""
if rentalCode == 'B':
    mileCharge = float(totalMiles) * 0.25
    baseCharge += mileCharge
"""
Daily Category:
    This calculation is only ran if the daily rental is driven over 100
    miles per day. $0.25 per mile is added to the cost of the daily price
    for every mile driven over the 100 miles.
"""
if rentalCode == 'D':
    averageDayMiles = totalMiles / int(rentalPeriod)
    if averageDayMiles > 100:
        extraMiles = averageDayMiles - 100
        mileCharge = float(extraMiles) * 0.25 * float(rentalPeriod)
        baseCharge += mileCharge
"""
Weekly Category:
    This calculation is only ran if the weekly rental is driven over 900
    miles per Week. $100 per week is added to the cost of the weekly price
    for every week the rental is driven over 900 miles
"""
if rentalCode == 'W':
    averageWeekMiles = totalMiles / int(rentalPeriod)
    if averageWeekMiles > 900:
        mileCharge = float(rentalPeriod) * 100.00 * float(rentalPeriod)
        baseCharge += mileCharge

'''
Section 3: Display the results to the customer
'''
print('Customer Summary')
print('Rental Code:       ' + rentalCode)
print('Rental Period:     ' + rentalPeriod)
print('Starting Odometer: ' + odoStart)
print('Ending Odometer:   ' + odoEnd)
print('Miles Driven:      ' + str(totalMiles))
print('Amount Due:        $' + str('%.2f' % baseCharge))
