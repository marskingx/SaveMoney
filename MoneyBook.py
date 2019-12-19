#讀取檔案
with open('moneybook.csv', 'r') as f:
    for line in f:
        name, price = line.strip().split(',')
        print(name, price )
moneybook = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'Q':
        break
    price = input('請輸入商品價格：')
    price = int(price)
    moneybook.append([name, price])
print(moneybook)

for p in moneybook:
    print(p[0], '的價格是', p[1])

with open ('moneybook.csv', 'w') as f:
    f.write('商品,價格\n')
    for p in moneybook:
        f.write(p[0] + ',' + str(p[1]) + '\n')