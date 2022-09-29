"""
This project is a solution to the following problem:

Gas Income You own a gas station that sells premium and regular gas. You are going to calculate total
sales for the month, total gas taxes collected and your business’ income (total sales less gas taxes).
"""
import os
from sys import platform
import pandas as pd
import matplotlib.pyplot as plt
from tkinter.filedialog import asksaveasfile

df = pd.DataFrame(columns=['Month', 'Cost of Premium', 'Premium Sold/g', 'Cost of Regular', 'Regular Sold/g', 'Market Rate Premium', 'Market Rate Regular', 'Tax Rate', 'Premium Profit', 'Regular Profit'])

class BusinessSummary:
    # While these functions could be condensed, the instructions asked specifically for individual functions
    def __init__(self,premiumCost,premiumGasSold,regularCost,regularSold,marketPremium,marketRegular,taxRate,breakPoint,month):
        self.pc = premiumCost
        self.pgs = premiumGasSold
        self.rc = regularCost
        self.rs = regularSold
        self.mr = marketRegular
        self.mp = marketPremium
        self.tr = taxRate
        self.br = breakPoint
        self.m = month
        
    def calculatePremiumIncome(self):
        return ((self.mp - self.pc) * self.pgs)
    def calculateRegularIncome(self):
        return ((self.mr - self.rc) * self.rs)
    def totalSales(self):
        return (self.calculateRegularIncome() + self.calculatePremiumIncome())
    def totalTaxes(self):
        return (self.totalSales() * self.tr)
    def businessIncome(self):
        return self.totalSales() - self.totalTaxes()
    def incomeReport(self):
        print('For month of: ', self.m)
        print(self.br)
        print("Cost Per Gallon of Premium Gas = ", round(self.pc),2)
        print("Cost Per Gallon of Regular Gas = ", round(self.rc),2)
        print('Market Rate for Regular Gas: ', round(self.mr),2)
        print('Market Rate for Premium Gas: ', round(self.mp),2)
        print("Gallons of Premium Gas Sold = ", round(self.pgs),2)
        print("Gallons of Regular Gas Sold = ", round(self.rs),2)
        print("Gas Tax Rate: %", round(self.tr*100),2)
        print("Total Premium Gas Profit = ", round(self.calculatePremiumIncome()),2)
        print("Total Regular Gas Profit = ", round(self.calculateRegularIncome()),2)
        print("Total Gas Sales = ", round(self.totalSales()),2)
        print("Total Taxes on Sales = ", round(self.totalTaxes()),2)
        print('Total Business Profit: ', round(self.businessIncome()),2)
        print(self.br)

        data = {'Month': self.m,       
                'Cost of Premium': self.pc,
                'Premium Sold/g': self.pgs,
                'Cost of Regular': self.rc,
                'Regular Sold/g': self.rs,
                'Market Rate Premium': self.mp,
                'Market Rate Regular': self.mr,
                'Tax Rate': self.tr*100,
                'Premium Profit': self.calculatePremiumIncome(),
                'Regular Profit': self.calculateRegularIncome() }
        update(data)

def title():
    print('\n')
    print(r' _|      _|                                              _|      _|            _|                          ')
    print(r' _|_|  _|_|    _|_|_|    _|_|_|    _|_|    _|_|_|          _|  _|    _|_|_|  _|_|_|_|    _|_|      _|_|_|  ')
    print(r' _|  _|  _|  _|    _|  _|_|      _|    _|  _|    _|          _|    _|    _|    _|      _|_|_|_|  _|_|      ')
    print(r' _|      _|  _|    _|      _|_|  _|    _|  _|    _|          _|    _|    _|    _|      _|            _|_|  ')
    print(r' _|      _|    _|_|_|  _|_|_|      _|_|    _|    _|          _|      _|_|_|      _|_|    _|_|_|  _|_|_|    ')
    print(r'___________________________________________________________________________________________________________')
    print('\n')

def clear_console():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        return os.system('clear')
    elif platform == "win32":
        return os.system('cls')

#This function is to check the conversion of input values to int or float so we can operate on them. Not included in Main class because it is outside class scope.   
def check_num(str): 
    while True:
        num = input(str)
        try:
            val = int(num)
            print("✅", val)
            return val
        except ValueError:
            try:
                val = float(num)
                print("✅", val)
                return val
            except ValueError:
                print("❌Invlaid entry. Please enter a number")

#This function is to check the result of input values to char so we can operate on them. Not included in Main class because it is outside class scope.
def check_char(str):
    while True:
        char = input(str)[0] #Only allows for one character response.
        try:
            if(char.lower() == 'y'):
                return True
            elif(char.lower() == 'n'):
                return False
            else:
                print('Invalid entry. Please enter either y or n')
        except ValueError:
            print("An exception occured" + ValueError)

def update(data):
    global df
    df = df.append(data, ignore_index=True)
    return print(df)

def show():
    global df

    plt.xlabel('Month')
    plt.ylabel('Amount in Dollars')
    plt.title('Profits by Month')
    plt.bar(df['Month'], df['Premium Profit'], label='Premium')
    plt.bar(df['Month'], df['Regular Profit'], bottom=df['Premium Profit'], label='Regular')
    plt.grid(color='#95a5a6', linestyle='-', linewidth=2, axis='y', alpha=0.5)
    plt.legend()
    
    return plt.show()

def next_step():
    if(check_char("Would you like to enter more data? (y/n)") == True):
        clear_console()
        return start()
    elif(check_char("Would you like to see your profits? (y/n)") == True):
        return show()
    elif(check_char('Would you like to save your results to a spreadsheet? (y/n)') == True):
        return export()
    else:
        return print('Goodbye 😁')

def export():
    files = [('All Files', '*.*'), 
             ('CSV Files', '*.csv'),
             ('Text Document', '*.txt')]
    path = asksaveasfile(filetypes = files, defaultextension = files)
    return df.to_csv(path, index=False)

#The start function will initialize the program and hold our inputs/class instances to return our result
def start():

    title()
    #Put your prompt in the argument
    month = input('Please enter the month of this report:')
    print(break_point := '===============================================')
    costR = check_num('Please enter your cost per gallon of regular grade fuel (87) wihtout a dollar sign: ')
    print(break_point)
    costP = check_num('Please enter your cost per gallon of premium grade fuel (91) wihtout a dollar sign:')
    print(break_point)
    marketR = check_num('Please enter your market sale price per gallon of regular grade fuel (87) wihtout a dollar sign:')
    print(break_point)
    marketP = check_num('Please enter your market sale price per gallon of premium grade fuel (91) wihtout a dollar sign:')
    print(break_point)
    soldR = check_num('Please enter the total gallons of regular gas sold this month')
    print(break_point)
    soldP = check_num('Please enter the total gallons of premium gas sold this month')
    print(break_point)
    tax = check_num('Please enter your states current gas tax rate as a decimal (ex. 3.2% is .032):')


    instance = BusinessSummary(costP,soldP,costR,soldR,marketP,marketR,tax,break_point,month)
    instance.incomeReport()
    
    next_step()

#Initialize program
start()