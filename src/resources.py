# Elliot Eriksson
# Teinf 20
# 2022-04-04
# Resources for Train Calculator 

from random import choice

class Train:

    def __init__(self, name : str, accelaration : int, speed : int, deceleration : int) -> None:
        self.name = name
        self.acceleration = accelaration
        self.speed = speed
        self.deceleration = deceleration

    def get_name(self):
        return self.name

    def get_acceleration(self):
        return self.acceleration
    
    def get_topSpeed(self):
        return self.speed

    def get_deceleration(self):
        return self.deceleration

    def get_stats(self):
        return self.name, self.acceleration, self.speed, self.deceleration

    def save_train(self):
        return f"{self.name}/{self.acceleration}/{self.speed}/{self.deceleration}"




def create_train():
    trains = []
    amount = int(input("How many trains do you want to make? "))
    for i in range(amount):
        name = input("What is the name of the train? ")
        acc = int(input("What is the trains acceleration (m/s2)? "))
        speed = int(input("What is the trains top speed (m/s)? "))
        dec = int(input("What is the trains deceleration (m/s2)? "))
        all_stats = Train(name, acc, speed, dec)
        trains.append(all_stats.save_train())
        print(trains)
    with open("trains.txt", "a", encoding="utf-8") as f:
        for list in trains:
            f.write('%s\n' % list)
   
def create_line():
    lines = []
    amount = int(input("How many train lines do you want to make? "))
    for i in range(amount):
        line = []
        name = input("What is the name of the line? ")
        line.append(name)
        station_amount = int(input("How many stations are there? "))
        x = 0
        for i in range(station_amount):
            distance = ""
            station_name = input("What is the name of the station? ")
            line.append(station_name)
            if x != station_amount - 1:
                distance = input("How far is it to the next station (m)? ")
                line.append(distance)
            x += 1
        lines.append(line)
    with open("lines.txt", "a", encoding="utf-8") as f:
        for list in lines:
            f.write('%s\n' % list)

def get_trains():
    number = 1
    with open("trains.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            print(f"({number}) {line}")
            number += 1


def get_lines():
    number = 1
    with open("lines.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            print(f"({number}) {line}")
            number += 1