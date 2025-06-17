# class Bank:
#     band_name = "Islamic Bank"

#     def __init__(self, accholder):
#         self.accholder = accholder

#     @classmethod
#     def change_bank_name(cls, name):
#         cls.band_name = name

#     def show_details(self):
#         print(f"Account Holder: {self.accholder}, Bank Name: {self.band_name}")


# acc1 = Bank(input("Enter Name: "))

# acc1.show_details()
# change_bank = input("Enter The Bank: ")
# Bank.change_bank_name(change_bank)
# acc1.show_details()

# class Bank:
#     bank_name = "Islamic Bank"

#     def __init__(self, acc_holder):
#         self.acc_holder = acc_holder

#     @classmethod
#     def change_bank_name(cls, name):
#         cls.bank_name = name

#     def show_details(self):
#         print(f"Account Holder: {self.acc_holder}, Bank Name: {self.bank_name}")


# acc1 = Bank(input("Enter Name: "))

# acc1.show_details()
# change_bank = input("Change the Bank: ")
# Bank.change_bank_name(change_bank)
# acc1.show_details()


# class Bank:
#     bank_name = "Islamic Bank"

#     def __init__(self, acc_holder):
#         self.acc_holder = acc_holder

#     @classmethod
#     def change_bank_name(cls, name):
#         cls.name = name

#     def show_details(self):
#         print(f"Account Holder: {self.acc_holder}, Bank Name: {self.bank_name}")


# ac1 = Bank(input("Enter Name: "))

# ac1.show_details()
# change_bank = input("Change Bank: ")
# Bank.change_bank_name(change_bank)
# ac1.show_details()


class Bank:
    bank_name = "islamic bank"

    def __init__(self, acc_holder):
        self.acc_holder = acc_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.name = name

    def show_details(self):
        print(f"Account Holder: {self.acc_holder}, Bank: {self.bank_name}")

details = Bank(input("Enter Name: "))

details.show_details()
change_bank = input("Change Bank Name: ")
Bank.change_bank_name(change_bank)
details.show_details()

