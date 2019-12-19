# 讀取檔案
moneybook = []
with open('moneybook.csv', 'r') as f:
    for line in f:
        if '商品,價格' in line:
            continue
        name, price = line.strip().split(',')
        moneybook.append([name, price])
while True:
    name = input('請輸入商品名稱：')
    if name == 'Q':
        break
    price = input('請輸入商品價格：')
    price = int(price)
    moneybook.append([name, price])
print(moneybook)
# 印出所有購買記錄
for p in moneybook:
    print(p[0], '的價格是', p[1])
#寫入檔案
with open ('moneybook.csv', 'w') as f:
    f.write('商品,價格\n')
    for p in moneybook:
        f.write(p[0] + ',' + str(p[1]) + '\n')