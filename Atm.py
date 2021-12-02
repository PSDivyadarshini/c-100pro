class atm(object):

  
  def __init__(self,pin,cardNumber):
    self.cardNumber=cardNumber
    self.pin=pin
    
  
  def cashWithDrawl(self):
    print("cash has been withdrawed")
    return "thankyou"

  def balanceEnquiry(self):
    print("we'll ensure that the account has sufficient funds for money transfer, cheque payment, etc.")
  
  
Atm=atm(60004,476508)

print(Atm.cashWithDrawl())

print(Atm.pin)
print(Atm.cardNumber)
print(Atm.cashWithDrawl())
print(Atm.balanceEnquiry())
