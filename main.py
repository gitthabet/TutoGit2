from BankAccount import CheckingAccount

chechacc = CheckingAccount(1000, 5)

chechacc.deposit(500)
print(chechacc.balance)

chechacc.withdraw(500, 50)
print(chechacc.balance)