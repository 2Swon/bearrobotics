import unittest
from Bank_System.bank_system import BankSystem
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TestBankSystemIntegration(unittest.TestCase):
    def setUp(self):
        # 테스트 시작 전 초기 설정
        self.bank_system = BankSystem()
        # 예제 계좌 설정
        self.example_accounts = [
            {'account_number': '123456789', 'pin': '1234', 'balance': 1000},
            {'account_number': '987654321', 'pin': '4321', 'balance': 2000}
        ]
        # 예제 계좌 추가
        for account in self.example_accounts:
            self.bank_system.add_account(account['account_number'], account['pin'], account['balance'])

    def test_atm_flow(self):
        # 카드 삽입(계좌 선택) 및 PIN 번호 검증
        selected_account = self.example_accounts[0]  # 예시로 첫 번째 계좌 선택
        account_number = selected_account['account_number']
        pin = selected_account['pin']

        # PIN 검증
        pin_verification_result = self.bank_system.verify_pin(account_number, pin)
        self.assertTrue(pin_verification_result, "PIN 검증 실패")
        logging.info(f"PIN 검증 성공: 계좌 번호 {account_number}")

        # 잔액 확인
        initial_balance = self.bank_system.get_balance(account_number)
        self.assertEqual(initial_balance, selected_account['balance'], "초기 잔액 조회 실패")
        logging.info(f"잔액 조회 성공: 계좌 번호 {account_number}, 현재 잔액 {initial_balance}")

        # 입금
        deposit_amount = 500
        self.bank_system.deposit(account_number, deposit_amount)
        expected_balance_after_deposit = initial_balance + deposit_amount
        balance_after_deposit = self.bank_system.get_balance(account_number)
        self.assertEqual(balance_after_deposit, expected_balance_after_deposit, "입금 후 잔액 오류")
        logging.info(f"입금 성공: 계좌 번호 {account_number}, 입금 후 잔액 {balance_after_deposit}")

        # 출금
        withdrawal_amount = 300
        self.bank_system.withdraw(account_number, withdrawal_amount)
        expected_balance_after_withdrawal = expected_balance_after_deposit - withdrawal_amount
        balance_after_withdrawal = self.bank_system.get_balance(account_number)
        self.assertEqual(balance_after_withdrawal, expected_balance_after_withdrawal, "출금 후 잔액 오류")
        logging.info(f"출금 성공: 계좌 번호 {account_number}, 출금 후 잔액 {balance_after_withdrawal}")


if __name__ == '__main__':
    unittest.main()