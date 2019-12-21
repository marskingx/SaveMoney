# 檢查檔案是否存在
import os  # 載入作業系統

def read_file(filename):
    moneybook = []
    with open(filename, 'r') as f:
        for line in f:
            if '商品,價格' in line:
                continue  # 繼續
            name, price = line.strip().split(',')
            moneybook.append([name, price])
    return moneybook


# 讓使用者輸入
def user_input(moneybook):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'Q':
            break
        price = input('請輸入商品價格：')
        price = int(price)
        moneybook.append([name, price])
    print(moneybook)
    return moneybook


# 印出所有購買記錄
def print_moneybook(moneybook):
    for p in moneybook:
        print(p[0], '的價格是', p[1])
    return moneybook


# 寫入檔案
def write_file(filename, moneybook):
    with open(filename, 'w') as f:
        f.write('商品,價格\n')
        for p in moneybook:
            f.write(p[0] + ',' + str(p[1]) + '\n')
    return filename


def main():
    filename = 'moneybook.csv'
    if os.path.isfile('moneybook.csv'):  # 檢查檔案是否存在
        print('YA!有檔案')
        moneybook = read_file('moneybook.csv')
    else:
        print('靠!竟然沒檔案')

    moneybook = user_input(moneybook)
    print_moneybook(moneybook)
    write_file('moneybook.csv', moneybook)

main()