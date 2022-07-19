# 1번
menu = {'콜라' : 500, '사이다' : 700, '레모네이드' : 4500, '오렌지주스' : 2000, '초코우유' : 1200, '아메리카노' : 3600}

# 2번
money = 30000
change = money - (sum(menu.values()) + menu['사이다'] + menu['콜라'])

print(change)