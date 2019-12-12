auzerib = set() #küme {1,2,3,4}
for a in range(2,101):
    for b in range(2,101):
        auzerib.add(a**b)
print(len(auzerib))
input()
