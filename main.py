'''from BankAccount import CheckingAccount


if __name__=="__main__":
    chechacc = CheckingAccount(1000, 5)
    chechacc.deposit(500)
    print(chechacc.balance)
    chechacc.withdraw(500, 50)
    print(chechacc.balance)

'''
# from BankAccount import CheckingAccount

from BetterDate import BetterDate

if __name__=="__main__":
    b = BetterDate(2000,10,9)
    print(b.day)

    b2 = BetterDate.from_str('2029-10-06')
    print(b2)
    # print(b.from_str('2029-10-06'))




