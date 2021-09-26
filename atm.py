class Atm(object):
    def __init__(self,card_number,pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
        
    def CashWithdrawl(self):
        print("Cash withdrawn")

    def BalanceEnquiry(self):
        print("Balance Enquired")

    def CashDeposit(self):    
        print("Cash Deposited")

hdfc = Atm("2148","2323")
print(hdfc.card_number)
print(hdfc.pin_number)                    
