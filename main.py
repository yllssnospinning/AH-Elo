from ahr import ahr


sys = ahr()
sys.loadGames('fileAddress')
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
