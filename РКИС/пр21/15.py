class BankAccount:
    __slots__ = ('balance',)

    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Пополнение {amount}. Баланс: {self.balance}")
        else:
            print("Сумма пополнения должна быть положительной")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Снятие {amount}. Баланс: {self.balance}")
            else:
                print("Недостаточно средств")
        else:
            print("Сумма снятия должна быть положительной")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)