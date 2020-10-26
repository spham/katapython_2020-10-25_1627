class BowlingGame:
    def __init__(self):
        self.rolls = []
        
    def roll(self, pins):
        self.rolls.append(pins)
    
    def score(self):
        result = 0
        rollIndex = 0
        for i in range(10):
            result += self.rolls[rollIndex]+self.rolls[rollIndex+1]
            rollIndex +=2
        return result