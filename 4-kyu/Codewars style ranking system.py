class User:
    RANKS = list(range(-8, 0)) + list(range(1, 9))

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, activity_rank):
        if activity_rank not in self.RANKS:
            raise ValueError("Invalid activity rank")

        rank_diff = self.RANKS.index(activity_rank) - self.RANKS.index(self.rank)

        if rank_diff == 0:
            progress = 3
        elif rank_diff == -1:
            progress = 1
        elif rank_diff > 0:
            progress = 10 * rank_diff * rank_diff
        else:
            progress = 0

        self.progress += progress
        print(self.RANKS.index(activity_rank))
        while self.progress >= 100:
            if self.rank == 8:
                self.progress = 0
                break
            else:
                self.rank = self.RANKS[self.RANKS.index(self.rank) + 1]
                self.progress -= 100

        if self.rank == 8:
            self.progress = 0

        return self.progress


      
            
                
            
user = User()
user.inc_progress(1)
user.inc_progress(1)
print(user.progress)