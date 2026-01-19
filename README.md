## bank-receipt-python

This project is a bank account simulation system developed in Python, focused on demonstrating Object-Oriented Programming (OOP) concepts such as inheritance, polymorphism, encapsulation, and composition.

## Project Objective

The goal of this project is to model different types of bank accounts and calculate their monthly returns according to specific business rules, such as taxes and investment rates.

Each account type applies a different calculation strategy, demonstrating polymorphism in practice.

## Main Concepts Applied

Object-Oriented Programming (OOP)

Inheritance

Polymorphism

Method overriding

Encapsulation

Separation of responsibilities

Modular project structure

## Class Responsibilities
# Banco

Manages all accounts registered in the system.

Responsibilities:

Store multiple accounts

Trigger the monthly return calculation

Print account balances

The bank does not need to know the concrete type of each account. It relies on polymorphism to call the correct return calculation method.

# ContaCliente (Base Class)

Base class for all account types.

Attributes:

Account number

IOF tax rate

Income tax rate (IR)

Invested value

Yield rate

Methods:

calcular_rendimento(): Applies yield and discounts taxes

extrato(): Prints the account balance

# ContaComum (Inherits from ContaCliente)

Represents a common account.

Behavior:

Applies yield

Discounts only IOF

Overrides the base return calculation method

# ContaRemunerada (Inherits from ContaCliente)

Represents a remunerated account.

Behavior:

Applies yield

Does not apply any taxes

Overrides the base return calculation method

# Execucao

Entry point of the application.

Responsibilities:

Instantiate the bank

Create different account types

Register accounts in the bank

Trigger monthly return calculation

Print final balances

## How to Run the Project

Make sure you have Python 3 installed

Clone the repository

Navigate to the project folder

Run:

python Execucao.py
