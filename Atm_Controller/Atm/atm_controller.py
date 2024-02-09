from Bank_System.bank_system import BankSystem

class ATMController:

    #Bank system 사용
    def __init__(self, bank_system: BankSystem):
        self.bank_system = bank_system
        self.current_account = None

    def insert_card_and_enter_pin(self, account_number, pin):
        #카드를 삽입하고 PIN 번호를 입력하여 계좌 접근을 시도합니다.
        if self.bank_system.verify_pin(account_number, pin):
            self.current_account = account_number
            return True
        else:
            self.current_account = None
            return False

    def select_account(self, account_number):
        #사용자가 다중 계좌 중 하나를 선택합니다.
        if account_number in self.accounts:
            self.current_account = account_number
            return True
        else:
            raise ValueError("Account does not exist or access denied.")

    def check_balance(self):
        #선택한 계좌의 잔액을 확인합니다.
        if not self.current_account:
            raise ValueError("No account selected.")
        return self.bank_system.get_balance(self.current_account)

    def deposit(self, amount):
        #계좌에 금액을 입금합니다.
        if not self.current_account:
            raise ValueError("No account selected.")
        self.bank_system.deposit(self.current_account, amount)

    def withdraw(self, amount):
        #계좌에서 금액을 출금합니다.
        if not self.current_account:
            raise ValueError("No account selected.")
        self.bank_system.withdraw(self.current_account, amount)