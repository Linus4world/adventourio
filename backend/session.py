from time import sleep

class Session:
    MAX_WAIT = 50000
    playerIds = []
    playerNames = []
    playerAnswers = []
    readyQueue = 0
    readyToPlay = False
    placesCategory = dict()
    playerCharacters = dict()
    playerChallengeOutcome = dict()
    playerNextChapter = dict()

    def __init__(self, maxPlayers = 4):
        self.maxPlayers = maxPlayers

    def addPlayer(self, id, name, answer):
        self.playerIds.append(id)
        self.playerNames.append(name)
        self.playerAnswers.append(answer)

    def setCharacters(self, character_assignment):
        self.playerCharacters = character_assignment
        self.readyQueue = self.maxPlayers
        self.readyToPlay = True

    def isFull(self) -> bool:
        return len(self.playerIds) == self.maxPlayers

    def isReady(self) -> bool:
        return self.readyQueue == self.maxPlayers - 1

    def getPlayerIndex(self, id: str): 
        return self.playerIds.index(id)

    def getCharacter(self, id: str):
        if self.playerCharacters:
            return self.playerCharacters[id]
        return 'Adventurer'

    def setPlacesCategory(self, places):
        self.placesCategory = places

    def getPlacesCategory(self):
        return self.placesCategory

    def wait_for_session_ready(self):
        self.readyQueue += 1
        counter = 0
        while(counter < self.MAX_WAIT):
            if self.readyToPlay:
                self.leave()
                return True
            sleep(2)
            counter += 1
        return False

    def leave(self):
        self.readyQueue -= 1
        if self.readyQueue == 0:
            this.readyToPlay = False
