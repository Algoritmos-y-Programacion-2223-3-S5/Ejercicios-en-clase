import random

class Race:
    def __init__(self, id, horses):
        self.id = id 
        self.horses = horses 

    def start_race(self):
        print("Partidaaaaaaaaaaaaaaaaaaaa salieron los competidores:")
        for horse in self.horses:
            print(f"{horse.id} - Horse: {horse.name}")
        

    def choose_winner(self):
        winner = random.choice(self.horses)
        print(f"********* The winner is {winner.name} *********")