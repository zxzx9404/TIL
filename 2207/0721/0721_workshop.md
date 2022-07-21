# 220721_workshop

## 1. 간단한 N의 약수 (SWEA #1933)

```python
num = int(input('입력 : '))

for i in range(1, num+1): # 1부터 num 까지의 반복
    if num % i == 0:
        print(i, "", end="")

'''
입력값 예시 : 10
출력값 : 1 2 5 10
'''
```

## 2. List의 합 구하기

```python
def list_sum(scores):
    a = 0
    for i in scores:
        a += i
    return a

print(list_sum([1, 2, 3, 4, 5,])) # 출력값 : 15
```

- 누적합 계산을 위한 변수 a를 선언한 뒤,  for 반복문을 통해 합을 계산하여 리턴

## 3. Dictionary로 이루어진 List의 합 구하기

```python
def dict_list_sum(dicts):
    age = 0 #나이 누적합 계산을 위한 변수
    for i in range(len(dicts)):
        age += dicts[i]['age']
    return age

print(dict_list_sum([{'name' : 'kim', 'age' : 12},
                     {'name' : 'lee', 'age' : 4}])) # 출력값 16
```

## 4. 2차원 List의 전체 합 구하기

```python
def all_list_sum(a):
    sum = 0 #누적합 계산용 변수 선언
    for i in range(len(a)): #이중 for문을 통해 이차원 list로 진입
        for j in range(len(a[i-1])):
            sum += a[i-1][j-1] #각각의 값을 sum에 누적
    return sum

print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])) # 55 출력
```

## 5.숫자의 의미

```python
def get_secret_word(askii):
    for i in range(0, len(askii)):
        print(chr(askii[i]), end="") # 줄바꿈 없이 문자열 출력
        


get_secret_word([83, 115, 65, 102, 89])
```

- chr() -> 숫자에 해당하는 symbol 반환

- ord() -> symbol에 해당하는 숫자 반환

## 6. 내 이름은 몇일까?

```python
def get_secret_word(askii):
    sum = 0 # 누적합 계산을 위한 변수 선언
    for i in range(0, len(askii)): 
        sum += ord(askii[i]) # 아스키 코드를 숫자로 변환하여 덧셈
    print(sum)


get_secret_word('happy') # 출력 : 546
```

## 7. 강한 이름

```python
def get_strong_word(a, b):
    sum_a = sum_b = 0 #누적합 계산 및 비교를 위한 변수 선언
    for i in range(0, len(a)): # 단어 a의 합 계산
        sum_a += ord(a[i])
    for i in range(0, len(b)): # 단어 b의 합 계산
        sum_b += ord(b[i])
    if sum_a > sum_b:  #비교 후 높은 값 반환
        print(a)
    elif sum_a < sum_b:
        print(b)
    else:
        print(a, b)



get_strong_word('delilah', 'dixon') # 출력 : 'delilah'
```


