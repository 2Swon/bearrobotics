class BankSystem:
    def __init__(self):
        self.accounts = {}

    #계좌 추가
    def add_account(self, account_number, pin, balance):
        if account_number in self.accounts:
            return False
        else:
            self.accounts[account_number] = {'pin': pin, 'balance': balance}
            return True

    def verify_pin(self, account_number, pin):
        #제공된 PIN이 계좌의 PIN과 일치하는지 검증합니다.
        account = self.accounts.get(account_number)
        if account and account['pin'] == pin:
            return True
        return False

    def get_balance(self, account_number):
        #계좌의 현재 잔액을 조회합니다.
        account = self.accounts.get(account_number)
        if account:
            return account['balance']
        else:
            raise ValueError("Account not found.")

    def deposit(self, account_number, amount):
        #계좌에 금액을 입금합니다.
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        account = self.accounts.get(account_number)
        if account:
            account['balance'] += amount
        else:
            raise ValueError("Account not found.")

    def withdraw(self, account_number, amount):
        #계좌에서 금액을 출금합니다.
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        account = self.accounts.get(account_number)
        if account:
            if account['balance'] >= amount:
                account['balance'] -= amount
            else:
                raise ValueError("Insufficient funds.")
        else:
            raise ValueError("Account not found.")