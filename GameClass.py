import random
import time
class Game:
    num_player = 0
    hunter = ""

    def introduction(self):
            nickname =[]
            print("Welcome to ......")
            print("This is an exciting social game!")
            self.num_player = int(input("How many players will be playing your game?"))
            x = 0
            while x < self.num_player:
                name = input("Please input the players' nickname one at a time")
                nickname.append(name)   #add input to list
                x = x+1

            self.hunter = random.choice(nickname)
            print("The hunter is: " + self.hunter)  #choose a random player from list
            print("Everyone else is the prey and you must reach the base")


    def countdown(self):
            minutes_time = int(input("Please input how many minutes you would like to hide"))
            while minutes_time != 0:    #start timer
                print(minutes_time, "time left to hide")
                time.sleep(60)  #wait 60 seconds before the minute decremets by one
                minutes_time -= 1
                if minutes_time == 0:
                    print("Time is up. The game is about to begin")

    def win_or_lose(self):
        prey = self.num_player-1
        if prey == 0:
            print("The Hunter has won!")
            print("congratulations: " + self.hunter)
        elif base_players == prey:
            print("The Runners have won!")


    introduction()
    countdown()