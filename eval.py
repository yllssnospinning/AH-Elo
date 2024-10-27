import math as m


class eval:
    def __init__(self):
        t = 0
    
    def getTeam(self, team):
        elo, vol = [], []
        for i in team:
            elo.append(i[0])
            vol.append(i[1])
        return [elo, vol]
    
    def getProb(self, a, b):
        return 1 / (1 + 10 ** ((b - a) / 400))
    
    def evaluate(self, t1, t2, result): 
        team1 = self.getTeam(t1)
        team2 = self.getTeam(t2)
        t1r, t1u = team1[0], team1[1]
        t2r, t2u = team2[0], team2[1]
        t1ar, t2ar = sum(t1r) / len(t1r), sum(t2r) / len(t2r)
        t1ap, t2ap = sum(t1u) / len(t1u), sum(t2u) / len(t2u)
        t1wr = len(t1r) / (len(t1r) + len(t2r))
        t2ar += 400 * m.log10((1 - t1wr) / t1wr)
        kFactor = 10 + ((t1ap + t2ap) / 2) * 90 * max(len(t1), len(t2))
        totDelta = result - self.getProb(t1ar, t2ar)
        totReward = kFactor * totDelta
        totalProb = sum(self.getProb(i, t2ar) for i in t1r)
        totReward = totReward * self.getProb(t1r[0], t2ar) / totalProb
        newUncertainty = t1u[0]
        newUncertainty += (abs(totDelta) - newUncertainty) / 5
        return [t1r[0] + totReward, newUncertainty]