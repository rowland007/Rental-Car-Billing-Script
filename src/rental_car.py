'''
Program:		CapstoneProject
Author:			Randall Rowland
Class:			IT-140-Q3788 Introduction to Scripting 18EW3
Instructor:		Angel D. Cross
Date:			18 Jan 2018
Description:
Input:          stdin
Output:         stdout


Usage:
Known bugs/missing features:

Modifications:
Date                Comment
----    ------------------------------------------------
'''
import sys


'''
Section 1: Collect customer input
'''

##1)	Request Rental code:
# Prompt --> "(B)udget, (D)aily, or (W)eekly rental?"
# rentalCode = ?
rentalCode = raw_input('(B)udget, (D)aily, or (W)eekly rental?')


# 2)	Request time period the car was rented.

# Prompt --> "Number of Days Rented:"
# daysRented = ?
#	OR
# Prompt --> "Number of Weeks Rented:"
# weeksRented = ?
def budget():
    global rentalPeriod
    global rate
    rentalPeriod = raw_input('Number of Days Rented: ')
    rate = 40.00

def daily():
    global rentalPeriod
    global rate
    rentalPeriod = raw_input('Number of Days Rented: ')
    rate = 60.00


def weekly():
    global rentalPeriod
    global rate
    rentalPeriod = raw_input('Number of Weeks Rented: ')
    rate = 190.00


options = {'B' : budget,
           'D' : daily,
           'W' : weekly,
}

options[rentalCode]()

# CUSTOMER DATA CHECK 1
# ADD CODE HERE TO PRINT:
# rentalCode
# daysRented
print('rentalCode: ' + rentalCode)
print('daysRented: ' + rentalPeriod)


# 3) Set the base charge for the rental type as the variable baseCharge.
# The base charge is the rental period * the appropriate rate:

# budget_charge = 40.00
# daily_charge = 60.00
# weekly_charge = 190.00

# baseCharge = ?
baseCharge = float(rentalPeriod) * rate

# 4)Collect Mileage information:
# a)	Prompt the user to input the starting odometer reading and store it as the variable odoStart

# Prompt -->"Starting Odometer Reading:\n"
# odoStart = ?
odoStart = raw_input('Starting Odometer Reading:\n')

# b)	Prompt the user to input the ending odometer reading and store it as the variable odoEnd

# Prompt -->"Ending Odometer Reading:"
# odoEnd = ?
odoEnd = raw_input('Ending Odometer Reading:')

# CUSTOMER DATA CHECK 2
# ADD CODE HERE TO PRINT:
# odoStart
# odoEnd
# baseCharge
print('odoStart:   ' + odoStart)
print('odoEnd:     ' + odoEnd)
print('baseCharge: $' + str('%.2f' % baseCharge))

'''
Section 2: Calculate the costs from the customer input
'''

# 1)	Calculate the mileage.
# a)	Calculate the total mileage:
#   ending odometer reading  - starting odometer reading
#   and store it as the variable totalMiles

# totalMiles = ?
totalMiles = int(odoEnd) - int(odoStart)

# 2)	 Calculate the mileage charge and store it as
#     the variable mileCharge:

# a)	Code 'B' (budget) mileage charge: $0.25 for each mile driven
if rentalCode == 'B':
    global amountDue
    amountDue = float(totalMiles) * 0.25

# b)	Code 'D' (daily) mileage charge: no charge if the average
#   number of miles driven per day is 100 miles or less;
#   i)	Calculate the averageDayMiles (totalMiles/daysRented)

#   ii)	If averageDayMiles is above the 100 mile per day
#       limit:
#     (1)	calculate extraMiles (averageDayMiles  - 100)
#     (2)	mileCharge is the charge for extraMiles,
#         $0.25 for each mile
if rentalCode == 'D':
    averageDayMiles = totalMiles / int(rentalPeriod)
    if averageDayMiles > 100:
        extraMiles = averageDayMiles - 100
        mileCharge = float(extraMiles) * 0.25
        baseCharge += mileCharge

# c)	Code 'W' (weekly) mileage charge: no charge if the
#   average number of miles driven per week is
#   900 miles or less;

#   i)	Calculate the averageWeekMiles (totalMiles/ weeksRented)

#   ii)	mileCharge is $100.00 per week if the average number of miles driven per week exceeds 900 miles
if rentalCode == 'W':
    averageWeekMiles = totalMiles / int(rentalPeriod)
    if averageWeekMiles > 900:
        mileCharge = float(rentalPeriod) * 100.00
        baseCharge += mileCharge

'''
Section 3: Display the results to the customer
'''
# 1) Calculate the Amount Due as the variable amtDue
#   This is the base charge + mile charge

# 2. Display the results of the rental calculation:

# Customer Summary
# Rental Code:
# Days Rented:
# Starting Odometer:
# Ending Odometer:
# Miles Driven:
# Amount Due:
print('Customer Summary')
print('Rental Code:       ' + rentalCode)
print('Rental Period:     ' + rentalPeriod)
print('Starting Odometer: ' + odoStart)
print('Ending Odometer:   ' + odoEnd)
print('Miles Driven:      ' + str(totalMiles))
print('Amount Due:        $' + str('%.2f' % baseCharge))
