class BowlingGame:
    def __init__(self):
        self.rolls = []
        
    def roll(self, pins):
        self.rolls.append(pins)
    
    def score(self):
        result = 0
        for i in range(20):
            result += self.rolls[i]
        return result