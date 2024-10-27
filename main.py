from ahr import ahr
import matplotlib.pyplot as plt
import csv

import pandas as pd
from lightweight_charts import Chart




def getohlc(prices, period):
    o, h, l, c = 0, 0, 10000000, 0
    num = 1
    time = 1
    writer.writerow(['time', 'open', 'high', 'low', 'close', 'volume'])
    for i in prices:
        if num == 1:
            o = i
        if i > h:
            h = i
        if i < l:
            l = i
        c = i
        num += 1
        t = '1/1/' + str(time + 2000)
        if num > period:
            writer.writerow([t, o, h, l, c, 1])
            num = 1
            time += 1
            o, h, l, c = 0, 0, 10000000, 0
    if num != 1:
        writer.writerow([t, o, h, l, c, 1])

sys = ahr()
sys.loadGames('C:\\Users\\PC\\Desktop\\Programming\\whrV1\\scores.txt')
inflation = []
db = {}
for i in range(0, len(sys.db) + 1):
#for i in [len(sys.db)]:
    num = 0
    print(i)
    gain = sys.iterate(i, 5)
    for ii in sys.l1:
        player = sys.l1[ii]
        if not ii in db:
            db[ii] = [], []
        db[ii][0].append(i)
        db[ii][1].append(player[0])



with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    getohlc(db['LYL'][1], 10)


if __name__ == '__main__':
    
    chart = Chart()
    
    # Columns: time | open | high | low | close | volume 
    df = pd.read_csv('data.csv')
    chart.set(df)
    
    chart.show(block=True)