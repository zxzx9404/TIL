# 220721_practice

## 1.updown

```python
import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
    while is_playing: #게임 안에서의 숫자맞추기 루프
        num = int(input('1이상 10000 이하의 숫자를 입력하세요 : '))
        if num < 1 or num > 10001:
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요')
            continue
        counts += 1 #입력값이 올바를경우 카운트 +1
        if num < answer:
            print('Up!!!')
            continue
        elif num > answer:
            print('Down!!!')
            continue
        elif num == answer:
            print(f'Correct!!! {counts}회 만에 정답을 맞히셨습니다.')
            break
    y_n = input('게임을 재시작 하시려면 y, 종료하시려면 n을 입력하세요 : ')
    if y_n == 'y':
        continue
    elif y_n == 'n':
        print('이용해주셔서 감사합니다. 게임을 종료합니다.')
        break
    else:
        print('잘못된 값을 입력하셨습니다. 게임을 종료합니다.')
        break
```

## 2.vending_machine

```python
print('=================================')
print('         Vending Machine         ')
print('=================================')
print('[Menu]')
print('1. 콜라 500원')
print('2. 사이다 700원')
print('3. 레모네이드 4500원')
print('4. 오렌지주스 2000원')
print('5. 초코우유 1200원')
print('6. 아메리카노 3600원')
print('=================================')

menus = ['콜라', '사이다', '레모네이드', '오렌지주스', '초코우유', '아메리카노']  # 메뉴 이름
costs = [500, 700, 4500, 2000, 1200, 3600]  # 메뉴 가격
budget = 0  # 자판기에 넣은 총 누적 금액

while True:
    print()
    money = int(input('금액을 넣어주세요.(그만 넣으시려면 0을 입력하세요.) : '))
    
    # 여기부터 코드를 작성하세요.
    if money == 0: # 1. 금액 넣기
        break

    elif money > 0 :
        budget += money
        print(f'현재 누적 금액은 {budget}원 입니다.')
        continue

    elif money < 0 :
        print('금액은 1원 이상 넣어주세요.')
        continue

while True: # 2. 메뉴 출력
    if budget < min(costs):
        print(f'{budget}원으로 구매 가능한 메뉴가 없습니다.')
    else:
        print(f'{budget}원으로 구매 가능한 메뉴는 다음과 같습니다.')
        for i in range(len(menus)):
         if budget >= costs[i]:
                print(f'{i+1}. {menus[i]} {costs[i]}원')
        print('')
        break
while True:  # 3. 메뉴 선택
    choice = int(input('구매하실 메뉴의 번호를 입력하세요. : '))
    if choice > len(menus) or choice < 1 or budget < costs[choice-1] :
        print('구매할 수 없는 메뉴입니다.')
        print('')
        continue
    else: # 4. 거스름돈 반환
        print(f'{menus[choice-1]}를 구매하셨습니다.')
        print(f'거스름돈은 {budget-costs[choice-1]}원 입니다. 감사합니다.')
        break
```






































