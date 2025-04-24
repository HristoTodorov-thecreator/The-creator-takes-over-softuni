
pin,balance,age = input().split(', ')
age = int(age)
balance = int(balance)

command = input()
class UnderageTransactionError(Exception):
    pass

class PINCodeError(Exception):
    pass

class MoneyNotEnoughError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass
AGE_NEEDED_FOR_ONLINE_TRANSACTIONS = 18
while command != 'End':

    splitted = command.split('#')

    if splitted[0] == 'Send Money':
        Money = int(splitted[1])
        pintry = splitted[2]
        if Money > balance:
            raise MoneyNotEnoughError('Insufficient funds for the requested transaction')
        if pin != pintry:
            raise PINCodeError('Invalid PIN code')
        if age < AGE_NEEDED_FOR_ONLINE_TRANSACTIONS:
            raise UnderageTransactionError('You must be 18 years or older to perform online transactions')

        balance -= Money
        print(f'Successfully sent {Money:.2f} money to a friend')
        print(f'There is {balance:.2f} money left in the bank account')
    if splitted[0] == 'Receive Money':
        Money = int(splitted[1])
        if Money < 0:
            raise MoneyIsNegativeError('The amount of money cannot be a negative number')
        if Money == 0:
            print(f'You cannot receive zero money')
            continue

        amount_of_money = Money / 2
        balance += amount_of_money
        print(f'{amount_of_money:.2f} money went straight into the bank account')



    command = input()