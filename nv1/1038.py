cod, qt = map(int, input().split())

tbprice = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
    }

for x,y in tbprice.items():
    if x == cod:
        total = y*qt
        print(f"Total: R$ {total:.2f}")
