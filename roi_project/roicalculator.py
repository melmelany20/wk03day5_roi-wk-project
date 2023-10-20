class MyROI:
    
    
    def __init__(self, income, expenses, cashFlow, ConC, Invest):
        self.income = income
        self.expenses = expenses
        self.cashFlow = cashFlow
        self.ConC = ConC
        self.Invest = Invest
        
        
    def Income(self):
        self.income = float(input('Please provide total rental income: '))
        
        
    def Expenses(self):
        self.expenses = float(input('Please provided detailed property expenses: '))
        
        
    def CashFlow(self):
        self.cashFlow = self.income - self.expenses
        print(f"Current cashflow is {self.cashFlow}")
   
        
    def Inv(self):
        dp = float(input('Please provide down payment '))
        self.Invest += dp
        close = float(input('Please provide current cost of living '))
        self.Invest += close
        repair = float(input('Please provide current repair total repair costs '))
        self.Invest += repair
        misc = float(input('Please provide any other investment info '))
        self.Invest += misc
        print(f'Your total investment is {self.Invest}')
        
        
    def ROI(self):
        acf = self.cashFlow * 12
        self.roi = acf/self.Invest * 100
        print(f'Estimated ROI is {self.roi}%.\nIf this does not look correct, please confirm information provided. ')
        
        
    def View(self):
        print(f'Rental Income: {self.income}')
        print(f'Property Expense: {self.expenses}')
        print(f'Cash Flow: {self.cashFlow}')
        print(f'Investment Value: {self.Invest}. \nThis value includes: \n - Down Payment \n - Total Closing Cost \n - Extra Expenses')
        print(f'Your Estimated ROI is {self.roi}% ')
        
        
def Driver():
    while True:
        print('Calculating... ')
        estimate.Income()
        estimate.Expenses()
        estimate.CashFlow()
        estimate.Inv()
        estimate.ROI()
        response = input('Please tell me what you would like to do: [Q]uit, [R]eview your info, or [S]tart over? ').upper
        if response == 'Q':
            break
        elif response == 'S':
            continue
        elif response == 'R':
            estamate.View()
            response_2 = input('Please tell me what you would like to do: [Q]uit, or [S]tart over? [C]hange my info? ').upper
            if response_2 == 'Q':
                break
            elif response_2 == 'S':
                continue
            elif response_2 == 'C':
                response_3 = input('Please tell me what you would like to do: \n[I]ncome, [E]xpenses, [T]otal investment ').upper
                if response_3 == 'I':
                    estamate.Income()
                    estamate.CashFlow()
                    response = input('Please tell me what you would like to do: [Q]uit, [R]eview your info, or [s]tart over? ').upper    
                elif response_3 == 'E':
                    estamate.Expenses()
                    estamate.CashFlow()
                    response = input('Please tell me what you would like to do: [Q]uit, [R]eview your info, or [S]tart over? ').upper
                elif response_3 == 'T':
                    estamate.TotalInv
                    response = input('Please tell me what you would like to do: [Q]uit, [R]eview your info, or [S]tart over? ').upper
        

estimate = MyROI(0, 0, 0, 0, 0)

Driver()
        