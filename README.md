# bearrobotics

bank_system.py 와 atm_controller.py 로 코드 분리 하였습니다.

BankSystem 클래스는 은행 계좌 시스템을 모델링하며, 계좌 추가, PIN 검증, 잔액 조회, 입금, 출금 등의 기능을 제공합니다.

ATMController 클래스는 실제 ATM 컨트롤러의 동작을 모델링하며, 사용자가 카드를 삽입하고 PIN을 입력하여 계좌에 접근하는 과정을 구현합니다. 

## 1. BankSystem
BankSystem 클래스는 은행 계좌 시스템을 모델링하며, 계좌 추가, PIN 검증, 잔액 조회, 입금, 출금 등의 기능을 제공합니다.

## 2. ATMController 
ATMController 클래스는 실제 ATM 컨트롤러의 동작을 모델링하며, 사용자가 카드를 삽입하고 PIN을 입력하여 계좌에 접근하는 과정을 구현합니다. 

## 3. test.py
* 성공적인 카드 삽입 및 PIN 입력: 사용자가 올바른 계좌 번호와 PIN을 입력했을 때의 시나리오를 테스트합니다.
* 실패한 카드 삽입 및 PIN 입력: 잘못된 PIN을 사용하여 접근을 시도했을 때의 시나리오를 테스트합니다.
* 잔액 확인: 올바른 인증 후 사용자 계좌의 잔액을 확인하는 시나리오를 테스트합니다.
* 입금 테스트: 올바른 인증 후 사용자 계좌에 금액을 입금하는 시나리오를 테스트합니다.
* 출금 테스트 (성공 케이스): 충분한 잔액이 있는 상태에서 출금을 시도하는 시나리오를 테스트합니다.
* 출금 실패 테스트 - 잔액 부족: 출금하려는 금액이 계좌 잔액을 초과하는 경우를 테스트하여, 예외 처리가 올바르게 작동하는지 검증합니다.


## test 방법

```python
git clone https://github.com/2Swon/bearrobotics.git

cd Atm_Controller

python test.py
```
