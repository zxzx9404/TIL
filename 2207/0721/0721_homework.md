# 220721_homework

## 1. 위치 인자와 키워드 인자

```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

ssafy('가흔') #정상 실행
ssafy(location = '부울경', name = '승현') # 정상 실행
ssafy('지우', location = '서울') #정상 실행
ssafy(name = '승호', '광주')  #에러 발생
```

1. ssafy함수의 파라미터 중 location은 default값이 설정되어 있으므로, 1개의 name값만을 입력하여도 정상 실행 가능

2. 모두 키워드 인자값으로 입력하였으므로, 순서와 무관하게 정상 실행

3. 함수 인자 입력의 기본 원칙은 positional하므로, '지우'값은 정상 위치에 입력, 이후 keyword를 통해 location을 입력하였으므로 정상 실행

4. 한번 keyword를 통해 인자를 입력하면, positional의 개념이 사라짐. 그러므로 에러 발생

## 2. 가변 인자 리스트

```python
def my_avg(*score):
    score_list = [*score] #점수들을 리스트 형태로 변환
    print(sum(score_list)/len(score_list)) #점수들의 평균 구하기

my_avg(77, 83, 95, 80, 70) # 81.0 출력
```

## 3. 반환값

```python
def my_func(a, b):
    c = a + b
    print(c)

result = my_func(3, 7) # 10 출력

print(result) # None 출력
```

- 정의한 my_func 함수는 값을 더한 뒤 출력 함수를 실행 할 뿐, 특정 값을 return하지 않기 때문에 변수 result에는 값이 저장되지 않음.

## 4. 이름 공간

- **L**ocal - **E**nclose - **G**lobal - **B**uilt in

## 5. 매개변수와 인자, 그리고 반환

- 오답 (1). 하나의 객체만 반환할 수 있는 것은 사실이나, 'return a, b'와 같이 설정하여 리턴값을 하나의 tuple로 출력 할 수 있다.

```python
def ssafy(a, b):
    return(a+b, a-b)

print(ssafy(5, 2)) # (7, 3)
print(type(ssafy(5,2))) # <class 'tuple'>
```

## 6. 재귀 함수

- 장점
  
  - 피보나치, 팩토리얼 등 재귀함수의 사용이 자연스러운 경우 반복문보다 훨씬 쉬운 코드로 작성이 가능하다.
  
  - 작성된 코드를 이해가기 편리핟.

- 단점
  
  - 스택 오버플로우의 가능성이 있다
  
  - 오류가 나기 쉬우며, 반복문보다 메모리 소모가 심하다.
