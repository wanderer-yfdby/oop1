#Определите класс `Account`, имитирующий банковский счет.
#Класс должен включать атрибуты для хранения идентификатора
#владельца, баланса счета и методы для депозита (пополнения)
#и снятия средств, если на счету достаточно средств.

class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет. Сумма на счете: {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"На счете недостаточно средств.")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} рублей. Остаток на счете: {self.balance}")

    def all_balance(self):
        print(f"Текущий баланс: {self.balance}")


man = Account("123214565", 600)

man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.deposit(23000)
