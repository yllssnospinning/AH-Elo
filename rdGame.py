
class reader:
    def __init__(self):
        pass

    def parseStr(self, string):
        list = []
        toParse = ''
        for i in range(0, len(string)):
            currentStr = string[i]
            if currentStr == ' ':
                list.append(toParse)
                toParse = ''
            else:
                toParse = toParse + currentStr
        if len(toParse) != 0:
            list.append(toParse)
        return list
    
    def parseGame(self, toParse):
        game = self.parseStr(toParse)
        t1, t2, result = [], [], -1
        phase = 1
        for i in game:
            if i == '/':
                phase += 1
            else:
                if phase == 1:
                    t1.append(i)
                elif phase == 2:
                    t2.append(i)
                else:
                    result = float(i)
                    break
        return [t1, t2, result]

