class Valid:
    def __init__(self,id,races):
        self.id = id 
        self.races = races
    
    def start_valid(self):
        print(f"The valid {self.id} is starting...!")
        for race in self.races:
            race.start_race()
            race.choose_winner()