from cProfile import label
import nbateams
from tkinter import *


class BasketballSupport:
    def __init__(self, name, division, players, wins, losses):
        self.name = name
        self.division = division
        self.players = players
        self.wins = wins
        self.losses = losses
        

class BasketballProgram:
    def __init__(self, parent):
        self.welcomeframe = Frame(parent)
        self.standingsframe = Frame(parent)
        self.west_teams = []
        self.east_teams = []

        self.east_teams.append(BasketballSupport("Boston Celtics", "Atlantic", nbateams.boston, 0, 0))
        self.east_teams.append(BasketballSupport("Brooklyn Nets", "Atlantic", nbateams.brooklyn, 0, 0))
        self.east_teams.append(BasketballSupport("New York Knicks", "Atlantic", nbateams.newyork, 0, 0))
        self.east_teams.append(BasketballSupport("Philadelphia 76ers", "Atlantic", nbateams.philly, 0, 0))
        self.east_teams.append(BasketballSupport("Toronto Raptors", "Atlantic", nbateams.toronto, 0, 0))
        self.east_teams.append(BasketballSupport("Chicago Bulls", "Central", nbateams.chicago, 0, 0))
        self.east_teams.append(BasketballSupport("Cleveland Cavaliers", "Central", nbateams.cleveland, 0, 0))
        self.east_teams.append(BasketballSupport("Detroit Pistons", "Central", nbateams.detroit, 0, 0))
        self.east_teams.append(BasketballSupport("Indiana Pacers", "Central", nbateams.indiana, 0, 0))
        self.east_teams.append(BasketballSupport("Milwaukee Bucks", "Central", nbateams.milwaukee, 0, 0))
        self.east_teams.append(BasketballSupport("Atlanta Hawks", "Southeast", nbateams.atlanta, 0, 0))
        self.east_teams.append(BasketballSupport("Charlotte Hornets", "Southeast", nbateams.charlotte, 0, 0))
        self.east_teams.append(BasketballSupport("Miami Heat", "Southeast", nbateams.chicago, 0, 0))
        self.east_teams.append(BasketballSupport("Orlando Magic", "Southeast", nbateams.orlando, 0, 0))
        self.east_teams.append(BasketballSupport("Washington Wizards", "Southeast", nbateams.washington, 0, 0))

        self.west_teams.append(BasketballSupport("Golden State Warriors", "Pacific", nbateams.golden, 0, 0))
        self.west_teams.append(BasketballSupport("Los Angeles Clippers", "Pacific", nbateams.lac, 0, 0))
        self.west_teams.append(BasketballSupport("Los Angeles Lakers", "Pacific", nbateams.lac, 0, 0))
        self.west_teams.append(BasketballSupport("Pheonix Suns", "Pacific", nbateams.pheonix, 0, 0))
        self.west_teams.append(BasketballSupport("Sacramento Kings", "Pacific", nbateams.sac, 0, 0))
        self.west_teams.append(BasketballSupport("Denver Nuggets", "Northwest", nbateams.denver, 0, 0))
        self.west_teams.append(BasketballSupport("Minnesota Timberwolves", "Northwest", nbateams.min, 0, 0))
        self.west_teams.append(BasketballSupport("Oklahoma City Thunder", "Northwest", nbateams.oklahoma, 0, 0))
        self.west_teams.append(BasketballSupport("Portland Trail Blazers", "Northwest", nbateams.portland, 0, 0))
        self.west_teams.append(BasketballSupport("Utah Jazz", "Northwest", nbateams.utah, 0, 0))
        self.west_teams.append(BasketballSupport("Dallas Mavreicks", "Southwest", nbateams.dallas, 0, 0))
        self.west_teams.append(BasketballSupport("Houston Rockets", "Southwest", nbateams.houston, 0, 0))
        self.west_teams.append(BasketballSupport("Memphis Grizzlies", "Southwest", nbateams.memphis, 0, 0))
        self.west_teams.append(BasketballSupport("New Orleans Pelicans", "Southwest", nbateams.new_orleans, 0, 0))
        self.west_teams.append(BasketballSupport("San Antonio Spurs", "Southwest", nbateams.san_antonio, 0, 0))


        welcome_label = Label(self.welcomeframe, text = "Welcome to NBA simulator 2022")
        welcome_label.grid(row = 0, column = 0, padx =  10, pady = 20)
        sim_button = Button(self.welcomeframe, text = "Start Season", command = self.newseason)
        sim_button.grid(row =1, column=0, padx = 10, pady = 20)
        self.welcomeframe.pack()
        standing_count = 0
        stats_east = Label(self.standingsframe, text = "Eastern Confrence")
        stats_east.grid(row = 0, column=0, pady= 20)
        
        """for i in range(self.east_teams):
            self.east_teams[]"""


        for i in range(len(self.east_teams)):
            standing_count += 1
            label_east = Label(self.standingsframe, text = str(i+ 1) + ". " + self.east_teams[i].name + str(self.east_teams[i].wins) + str(self.east_teams[i].losses), anchor = W)
            label_east.grid(row = i+1, column = 0)
        stats_west = Label(self.standingsframe, text = "Western Confrence")
        stats_west.grid(row = standing_count + 1, column=0, pady = 20)

        for i in range(len(self.west_teams)):
            standing_count += 1
            label_west = Label(self.standingsframe, text = self.west_teams[i].name, anchor = W)
            label_west.grid(row = standing_count+ 1, column = 0)
        
        

    def newseason(self):
        self.welcomeframe.pack_forget()
        self.standingsframe.pack()


if __name__ == "__main__":
    root = Tk()
    bball = BasketballProgram(root)
    root.mainloop()