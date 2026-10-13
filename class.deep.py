''' CLASS deep diving!
  (1) ENCAPSULATION
  (2) INHERITENCE
  (3) POLYMORPHISM
'''

print("================ ENCAPSULATION ======================")


class Account():
    # state
    discription = "The class makes bank acounts"

    # constructor
    def __init__(self, owner, amount):
        # Private atributlar (enkapsulyatsiya)
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        # Attribute nomlari __ bilan chaqirilishi kerak
        print(f"The Owner {self.__owner} has {self.__amount} USD")

    def deposit(self, amount):
        print("Deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("Withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.__owner = new_owner


my_account = Account("Nick", 1000)
my_account.get_balance()

print("---------")

my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

try:

    result = my_account.__amount
    print("result:", result)

except Exception as err:
    print("No target state found:", err)

# getter vs setter
print("owner_before:", my_account.holder)  # state
my_account.holder = "Martin"
print("owner_after:", my_account.holder)
