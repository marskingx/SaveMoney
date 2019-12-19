moneybook = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'Q':
        break
    price = input('請輸入商品價格：')
    moneybook.append([name, price])
print(moneybook)

for p in moneybook:
    print(p[0], '的價格是', p[1])

with open ('moneybook.csv', 'w') as f:
    for p in moneybook:
        f.write(p[0] + ',' + p[1] + '\n')
