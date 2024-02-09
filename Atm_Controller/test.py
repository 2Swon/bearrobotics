import unittest
from Bank_System.bank_system import BankSystem
from Atm.atm_controller import ATMController
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestATMController(unittest.TestCase):
    def setUp(self):
        logging.info("테스트 케이스 시작: 은행 시스템 및 ATM 컨트롤러 초기화")
        self.bank_system = BankSystem()
        self.atm_controller = ATMController(self.bank_system)
        self.account_number = '123456789'
        self.pin = '1234'
        self.initial_balance = 1000
        self.bank_system.add_account(self.account_number, self.pin, self.initial_balance)
        logging.info(f"테스트 계좌 추가: 계좌 번호 {self.account_number}, 초기 잔액 {self.initial_balance}")

    def test_insert_card_and_enter_pin_success(self):
        logging.info("테스트 시작: 성공적인 카드 삽입 및 PIN 입력")
        result = self.atm_controller.insert_card_and_enter_pin(self.account_number, self.pin)
        self.assertTrue(result)
        logging.info("성공적인 PIN 입력 테스트 완료")

    def test_insert_card_and_enter_pin_failure(self):
        logging.info("테스트 시작: 실패한 카드 삽입 및 PIN 입력")
        result = self.atm_controller.insert_card_and_enter_pin(self.account_number, 'wrong_pin')
        self.assertFalse(result)
        logging.info("실패한 PIN 입력 테스트 완료")

    def test_check_balance(self):
        logging.info("테스트 시작: 잔액 확인")
        self.atm_controller.insert_card_and_enter_pin(self.account_number, self.pin)
        balance = self.atm_controller.check_balance()
        self.assertEqual(balance, self.initial_balance)
        logging.info(f"잔액 확인 테스트 완료: 확인된 잔액 {balance}")

    def test_deposit(self):
        logging.info("테스트 시작: 입금 테스트")
        self.atm_controller.insert_card_and_enter_pin(self.account_number, self.pin)
        deposit_amount = 500
        logging.info(f"입금되는 금액: {deposit_amount}")
        self.atm_controller.deposit(deposit_amount)
        final_balance = self.atm_controller.check_balance()
        logging.info(f"입금 후 잔액: {final_balance}")
        self.assertEqual(final_balance, self.initial_balance + deposit_amount)

    def test_withdraw_success(self):
        logging.info("테스트 시작: 출금 테스트 (성공 케이스)")
        self.atm_controller.insert_card_and_enter_pin(self.account_number, self.pin)
        withdrawal_amount = 500
        self.atm_controller.withdraw(withdrawal_amount)
        final_balance = self.atm_controller.check_balance()
        logging.info(f"출금 후 잔액: {final_balance}")
        self.assertEqual(final_balance, self.initial_balance - withdrawal_amount)


    def test_withdraw_failure_due_to_insufficient_funds(self):
        logging.info("테스트 시작: 출금 실패 테스트 - 잔액 부족")
        self.assertTrue(self.atm_controller.insert_card_and_enter_pin(self.account_number, self.pin), "PIN 검증 실패")
        with self.assertRaises(ValueError):
            self.atm_controller.withdraw(self.initial_balance + 500)  # 잔액 초과 금액 출금 시도
        logging.info("잔액 부족으로 인한 출금 실패 테스트 완료")

if __name__ == '__main__':
    unittest.main()