# -*- coding: utf-8 -*-
"""Credit score for working class.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15LWbhpw1ZX_LnladhRyyxxyiSBUTFU0W
"""

def payment_to_income_ratio():
    
    # prompt user to enter input variables
    monthly_income = float(input("Enter monthly net income: "))
    other_income_1 = float(input("Enter other income 1: "))
    other_income_2 = float(input("Enter other income 2: "))
    rent = float(input("Enter rent: "))
    fees = float(input("Enter fees: "))
    feeding = float(input("Enter feeding: "))
    medical = float(input("Enter medical: "))
    transport = float(input("Enter transport: "))
    utilities = float(input("Enter utilities: "))
    other_loan_payments = float(input("Enter other loan payments: "))
    social_events = float(input("Enter social events: "))
    other_expenses = float(input("Enter other expenses: "))
    monthly_instalment = float(input("Enter monthly installment: "))
    
    # calculate total income
    total_income = monthly_income + other_income_1 + other_income_2
    
    # calculate total expenses
    total_expenses = rent + fees + feeding + medical + transport + utilities + other_loan_payments + social_events + other_expenses
    
    # calculate debt-to-income ratio
    dti = total_expenses / total_income
    
    # calculate surplus income
    surplus = total_income - total_expenses
    
    # calculate payment-to-income ratio
    payment_to_income_ratio = monthly_instalment / total_income
 
    
    return payment_to_income_ratio

payment_to_income_ratio()

