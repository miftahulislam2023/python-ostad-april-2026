from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass
    
    def receipt(self):
        print("পেমেন্ট রিসিট তৈরি হচ্ছে...")

class Bkash(PaymentSystem):
    def pay(self, amount):
        print(f"বিকাশ দিয়ে {amount} টাকা পেমেন্ট করা হলো।")

class Nagad(PaymentSystem):
    def pay(self, amount):
        print(f"নগদ দিয়ে {amount} টাকা পেমেন্ট করা হলো।")

user1 = Bkash()
user1.pay(500)
user1.receipt()

user2 = Nagad()
user2.pay(1000)