from time import sleep

class Session:
    MAX_WAIT = 60000
    playerIds = []
    playerNames = []
    playerAnswers = []

    def __init__(self, maxPlayers = 4):
        self.maxPlayers = maxPlayers

    def addPlayer(self, id, name, answer):
        self.playerIds.append(id)
        self.playerNames.append(name)
        self.playerAnswers.append(answer)

    def isFull(self) -> bool:
        return len(self.playerIds) == self.maxPlayers

    def getPlayerIndex(self, id: str): 
        return self.playerIds.index(id)

    def wait_for_full_session(self):
        counter = 0
        while(counter < self.MAX_WAIT):
            if self.isFull():
                return True
            sleep(2)
            counter += 1
        return False
