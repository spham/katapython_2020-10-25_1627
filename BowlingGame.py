class BowlingGame:
    def __init__(self):
        self.rolls = []
        
    def roll(self, pins):
        self.rolls.append(pins)
    
    def score(self):
        result = 0
        rollIndex = 0
        for i in range(10):
            if self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
            else:
                result += self.frameScore(rollIndex)
            rollIndex += 2
        return result
    
    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10
    def spareScore(self,rollIndex):
        return 10 + self.rolls[rollIndex + 2]
    
    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]