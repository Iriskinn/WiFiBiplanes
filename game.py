import random


class Game:
    teams = [[], []]
    roles = [['s', 'p'], ['s', 'p']]
    ingame = set([])


    def __init__(self):
        random.shuffle(self.roles[0])
        random.shuffle(self.roles[1]) 


    def login(self, username):
        if username in self.ingame or len(self.teams[0]) == len(self.teams[1]) == 2:
            return False
        elif len(self.teams[0]) == 2:
            self.teams[1].append(username)
        elif len(self.teams[1]) == 2:
            self.teams[0].append(username)
        else:
            r = random.randint(0, 1)
            self.teams[r].append(username)
        self.ingame.add(username)
        print(self.teams)


    def getRole(self, username):
        if username in self.teams[0]:
            return self.roles[0][self.teams[0].index(username)]
        elif username in self.teams[1]:
            return self.roles[1][self.teams[1].index(username)]
        else:
            return '-'


    def attack(self, username):
        pass


    def recharge(self, username):
        pass


    def time_step(self, delta_time):
        pass