# 4. Class Variables and Class Methods

class Bank:
    print("Bank name:")
    bank_name = "SBP"
    def change_bank_name(cls, name):
        cls.bank_name = name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
b1 = Bank()
print(b1.bank_name)
b2 = Bank()
Bank.change_bank_name("SBI")
print(b2.bank_name)