import time
import random


class Game:
    num_players = 0
    hunter = ""
    base_players = 0
    nicknames = []
    player_obj = []
    locations = {51.457040: -0.019570,
                 51.456967: -0.019921,
                 51.456943: -0.020951,
                 51.457622: -0.020168,
                 51.458207: -0.019074
                 }

    def introduction(self):
            print("Welcome to Pigeon Run")
            print("This is an exciting social game!")
            print("Game Rules: Run as far away from each other as possible in the initial time given"
                  "When the game begins one or more of \n you will be randomly chosen to be the Hunters and the rest "
                  "are Pigeons. \n Hunters must chase the Pigeons while the Pigeons attempt to get to the Base which is"
                  " a well known landmark in London.\n If a Pigeon gets caught they become a Hunter and must also Hunt "
                  "the Pigeons. \n For the Hunters to win they must catch all the Pigeons. For the Pigeons to win they"
                  "must all reach the Base. \nGood Luck! ")
            self.num_player = int(input("How many players will be playing your game?"))
            x = 0
            if self.num_player > 2:
                while x < self.num_player:
                    self.base_players = self.num_players-1
                    name = input("Please input the players' nickname one at a time")
                    self.nicknames.append(name)   #add input to list
                    x = x+1
            else:
                print("You need more than 2 people to play")

    def choose_hunter(self):
            self.hunter = random.choice(self.nicknames)
            print("The hunter is: " + self.hunter)  #choose a random player from list
            print("Everyone else is a Pigeon and you must reach the base")

    def create_players(self):
            for name in self.nicknames:
                latitude, longitude = random.choice(self.locations.items)
                if name == self.hunter:
                    self.current_player = Player(name, latitude, longitude, True)
                    self.player_obj.append(current_player)

                else:
                    self.current_player = Player(name, latitude, longitude, False)
                    self.player_obj.append(current_player)

    def countdown(self):
            minutes_time = int(input("Please input how many minutes you would like to hide"))
            while minutes_time != 0:    #start timer
                print(minutes_time, " minutes left to hide")
                time.sleep(5)  #wait 60 seconds before the minute decrements by one
                minutes_time -= 1
                if minutes_time == 0:
                    print("Time is up. The game is about to begin")
                    current_base.choose_base()

    def player_moved(self):
        for players in self.nicknames:
            is_moved = current_player.has_moved()
            #if is_moved:
                #GPS.hunterRadius() ##NEED HUNTER RADIUS METHOD NAME

    def game_over(self):
        game_ends = False
        prey = self.num_player-1
        if prey == 0:
            print("The Hunter has won!")
            print("congratulations: " + self.hunter)
            game_ends = True
        elif self.base_players == prey:
            print("The Pigeons have won!")
            game_ends = True
        return game_ends


class Base:
    base_options = ["London Bridge","Waterloo Bridge","Big Ben","Buckingham Palace","London Eye", ]

    def choose_base(self):
        base = random.choice(self.base_options)
        print("The base the Pigeons must get to in order to win is: " + base)

    def player_count(self):

        return
            #"somehow keep track of no. of players that have reached the base"


class Player:

    def __init__(self, player_name, lat, long, is_hunter):
        name = player_name
        current_lat = lat
        current_long = long
        self.is_hunter = is_hunter

    def has_moved(self):  # if the player has moved, return true.
        return
        #return GPS.haveIMoved(self.name)

    def set_hunter(self):  # switch from prey to hunter when caught
        if not self.is_hunter:
            self.is_hunter = True
            current_game.base_players -= 1
            Notifications.caught_prey()

    def is_prey_nearby(self):
        Notifications.prey_is_in_area()
        return GPS.preyInRange(self.name)

    def is_hunter_nearby(self):
        Notifications.hunter_is_in_area()
        return GPS.preyInRange(self.name)


class Notifications:

    def hunter_is_in_area(self):
        print('There is a Hunter in the area!')

    def prey_is_in_area(self):
        print('There is a Pigeon in the area!')

    def arrived_base(self):
        print("One of the pigeons have reached the Base")

    def caught_prey(self):
        print("One of the Pigeons has been caught.")


current_game = Game()
current_game.introduction()
current_game.choose_hunter()
current_base = Base()
current_player = Player("", 0, 0, False)
current_game.countdown()

if current_game.game_over():
    print("The game is over. Thank you for playing")
else:
    while not current_game.game_over():
        current_game.player_moved()
        #call gps class to check if player has made it to the base
        #base_reached = GPS.basemethod
        #if reached:
            #base_players += 1
