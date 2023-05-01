#!/usr/bin/env python3

print("Welcome to Tip Calculator")

number_of_people = int(input("[+] Input number of people: "))
total_bill = float(input("[+] Input total bill: "))
tip = int(input("input your tip amount: "))

tip_percentage = float(tip / 100)
tip_amount = total_bill * tip_percentage
total_bill = (total_bill + tip_amount) / number_of_people
print(round(total_bill, 2))
