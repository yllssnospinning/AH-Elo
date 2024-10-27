

class ahr:
    def __init__(self):
        from eval import eval
        from rdGame import reader

        self.npElo = eval()
        self.rd = reader()
        self.l1, self.l2 = {}, {}
        self.db = []
    
    def getPlayer(self, playerName, source):
        ply = self.l1 if source == 1 else self.l2
        player = ply[playerName] if playerName in ply else [1500, 0.5]
        return player
    
    def getAdjustedPlayers(self, playerNames, focused):
        adjusted = []
        for i in range(0, len(playerNames)):
            source = i == focused if focused != -1 else 1
            adjusted.append(self.getPlayer(playerNames[i], source))
        return adjusted
    
    def teamToPlayers(self, t1, t2):
        players = []
        for i in t1:
            players.append(i)
        for i in t2:
            players.append(i)
        return players
    
    def playersToTeam(self, players, t1l, focused, gameResult):
        t1, t2 = [], []
        for i in range(0, len(players)):
            add = players[i]
            t1.append(players[i]) if i < t1l else t2.append(players[i])
        focusID = focused - t1l * (not focused < t1l)
        if not focused < t1l: # focused player in second team
            temp = t1
            t1 = t2
            t2 = temp
        t1.insert(0, t1.pop(focusID))
        result = gameResult if focused < t1l else 1 - gameResult
        return [t1, t2, result]

    def getTeamCompute(self, t1, t2, gameResult, type):
        players = self.teamToPlayers(t1, t2)
        adjustedPlayers = []
        adjustedTeams = []
        for i in range(0, len(players)):
            adjType = -1 if type == 0 else i
            adjustedPlayers = self.getAdjustedPlayers(players, adjType)
            adjustedTeams.append(self.playersToTeam(adjustedPlayers, len(t1), i, gameResult))
        return [adjustedTeams, players]
    
    def computeGame(self, t1, t2, result, type):
        compute = self.getTeamCompute(t1, t2, result, type)
        newPlayers = []
        pairs, playerNames = compute[0], compute[1]
        for i in pairs:
            newPlayers.append(self.npElo.evaluate(i[0], i[1], i[2]))
        for i in range(0, len(playerNames)):
            self.l1[playerNames[i]] = newPlayers[i]
    
    def loadGames(self, adderss):
        f = open(str(adderss))
        self.db = [self.rd.parseGame(i) for i in f]
    
    def computeDB(self, type, length):
        self.l1 = {}
        for ii in range(0, len(self.db)):
            if ii > length:
                break
            i = self.db[ii]
            self.computeGame(i[0], i[1], i[2], type)
    
    def iterate(self, length, depth):
        self.l1, self.l2 = {}, {}
        ratingEvolution = {}
        for i in range(0, depth):
            self.computeDB(not i == 0, length)
            for ii in self.l1:
                if not ii in ratingEvolution:
                    ratingEvolution[ii] = []
                ratingEvolution[ii].append(self.l1[ii][0])
            self.l2 = self.l1
        return ratingEvolution
       
        
