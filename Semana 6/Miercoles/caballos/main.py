from horse import Horse
from race import Race
from valid import Valid

def create_horses(horse_list):
    horse_list.append(Horse("Tormenta china",1)) 
    horse_list.append(Horse("Rayo veloz",2)) 
    horse_list.append(Horse("McQueen",3)) 
    horse_list.append(Horse("Pegasus",4)) 
    horse_list.append(Horse("DoggyDut",5)) 
    horse_list.append(Horse("Alfredo",6)) 

def create_races(race_list, horse_list, quantity):
    for i in range(quantity):
        race_list.append(Race(i+1, horse_list))

def create_valid(race_list, valid_list):
    valid_list.append(Valid(5, race_list))
    valid_list.append(Valid(6, race_list))

def main():
    valid_list = []
    horse_list = []
    race_list = []
    quantity = int(input("How many races do you want in each valid\n-->"))

    create_horses(horse_list)
    create_races(race_list, horse_list, quantity)
    create_valid(race_list,valid_list)

    for valid in valid_list:
        valid.start_valid()

main()