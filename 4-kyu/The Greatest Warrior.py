class Warrior:
    RANKS = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
    
    def __init__(self):
        self._level = 1
        self._experience = 100
        self._rank = self.RANKS[0]
        self.achievements = []

    def _update_level_and_rank(self):
        self._experience = min(self._experience, 10000)
        self._level = min(self._experience // 100, 100)
        self._rank = self.RANKS[min(self._level // 10, 10)]

    def battle(self, enemy_level):
        if enemy_level < 1 or enemy_level > 100:
            return "Invalid level"

        diff = enemy_level - self._level

        if diff <= -2:
            return "Easy fight"
        elif diff == -1:
            self._experience += 5
            self._update_level_and_rank()
            return "A good fight"
        elif diff == 0:
            self._experience += 10
            self._update_level_and_rank()
            return "A good fight"
        elif diff > 0:
            enemy_rank = self.RANKS[min(enemy_level // 10, 10)]
            if self.RANKS.index(enemy_rank) > self.RANKS.index(self._rank) and diff >= 5:
                return "You've been defeated"
            
            self._experience += 20 * diff * diff
            self._update_level_and_rank()
            return "An intense fight"

    def training(self, args):
        description, exp, min_level = args
        if self._level >= min_level:
            self._experience += exp
            self._update_level_and_rank()
            self.achievements.append(description)
            return description
        else:
            return "Not strong enough"

    @property
    def level(self):
        return self._level
    
    @property
    def experience(self):
        return self._experience
    
    @property
    def rank(self):
        return self._rank
    
    def __str__(self):
        return f"Level: {self._level}, Experience: {self._experience}, Rank: {self._rank}, Achievements: {self.achievements}"


bruce_lee = Warrior()
bruce_lee.level = 8
print(bruce_lee.battle(13))
print(bruce_lee.experience)