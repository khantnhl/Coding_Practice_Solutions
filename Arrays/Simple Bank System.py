class Bank:
    def __init__(self, balance: List[int]):
        self.arr = balance
        self.numAccounts = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        available = False
        if(account1 <= self.numAccounts and account2 <= self.numAccounts and self.arr[account1 - 1] >= money):
            available = True

            self.arr[account1 - 1] -= money
            self.arr[account2 - 1] += money
        return available

    def deposit(self, account: int, money: int) -> bool:
        available=False
        if(account <= self.numAccounts):
            available = True

            self.arr[account - 1] += money
        return available

    def withdraw(self, account: int, money: int) -> bool:
        result = False
        if(account <= self.numAccounts and self.arr[account-1]>=money):
            result = True

            self.arr[account-1] -= money 
        return result
            