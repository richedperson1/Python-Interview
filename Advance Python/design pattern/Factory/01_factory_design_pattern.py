
from abc import ABC,abstractmethod

class Payment_methods(ABC):
    @abstractmethod
    def payment_notification(self,*arg,**kwargs):
        pass
    
    @abstractmethod
    def payment_debit(self,*arg,**kwargs):
        pass
    
    
    @abstractmethod
    def payment_credit(self,*arg,**kwargs):
        pass
    
    

class credit_card(Payment_methods):
    
    
    def payment_notification(self,*arg,**kwargs):
        print("Payment is sucessfull using credit card")
    
    def payment_debit(self,money=500):
        print(f"Payment of {money}$ is debit from your account using credit card")
    
    def payment_credit(self,money):
        print(f"Payment of {money}$ is credit to your account using credit card")
        
class debit_card(Payment_methods):
    
    
    def payment_notification(self,*arg,**kwargs):
        print("Payment is sucessfull using debit card")
    
    def payment_debit(self,money=500):
        print(f"Payment of {money}$ is debit from your account using debit card")
    
    def payment_credit(self,money):
        print(f"Payment of {money}$ is credit to your account using debit card")
        

    

class upi(Payment_methods):
    
    
    def payment_notification(self,*arg,**kwargs):
        print("Payment is sucessfull using upi")
    
    def payment_debit(self,money=500):
        print(f"Payment of {money}$ is debit from your account using upi")
    
    def payment_credit(self,money):
        print(f"Payment of {money}$ is credit to your account using upi")
        

    
    
    
class payment_factory:
    def payment_choice(self,payment_mode):
        
        payment_choices = {
            "credit":credit_card(),
            "debit":debit_card(),
            "upi":upi(),
            }
        return payment_choices[payment_mode]
    
    

def main():
    fac_pay = payment_factory()
    pay = fac_pay.payment_choice("credit")
    
    pay.payment_debit(2560)
    

main()
    
        