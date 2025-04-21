"""
Author: Cristian Alvarez
Assignment: Module 5 Assignment 1
Date: 4/21/2025
Verison: 1.0
"""
STATE = .05
COUNTY = .025


def totalSales():
    amount = float(input("Enter total sales for the month: $"))
    stateTax = amount * STATE
    print(f"Your state tax amount is: ${stateTax:.2f}")
    countyTax = amount * COUNTY
    print(f"Your state tax amount is: ${countyTax:.2f}")
    totalTax = countyTax + stateTax
    print(f"Your total tax is: ${totalTax:.2f}")

totalSales()



