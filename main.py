import nbateams
from tkinter import *
import random


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
        self.choosingframe = Frame(parent)
        self.homeframe = Frame(parent)
        self.gameframe = Frame(parent)


        self.west_teams = []
        self.east_teams = []
        self.allnames = []
        self.allteams = []
        self.chosenteamvar = StringVar()
        self.schedule = []
        
        self.atlanticdiv = []
        self.centraldiv = []
        self.southeastdiv = []

        self.pacificdiv = []
        self.northwestdiv = []
        self.southwestdiv = []







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
        self.west_teams.append(BasketballSupport("Los Angeles Lakers", "Pacific", nbateams.lal, 0, 0))
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
        sim_button = Button(self.welcomeframe, text = "Start Season", command = lambda: self.changeframe(self.welcomeframe, self.choosingframe))
        sim_button.grid(row =1, column=0, padx = 10, pady = 20)
        self.welcomeframe.pack()

        choose_label = Label(self.choosingframe, text = "Would you like to follow a team or just watch? ")
        choose_label.grid(row = 0, columnspan = 2, padx = 10, pady = 20)
        for i in range(len(self.east_teams)):
            self.allnames.append(self.east_teams[i].name)
            self.allnames.append(self.west_teams[i].name)
            self.allteams.append(self.east_teams[i])
            self.allteams.append(self.west_teams[i])
        for d in self.allteams:
            if d.division == "Atlantic":
                self.atlanticdiv.append(d)
            elif d.division == "Central":
                self.centraldiv.append(d)
            elif d.division == "Southeast":
                self.southeastdiv.append(d)
            elif d.division == "Pacific":
                self.pacificdiv.append(d)
            elif d.division == "Northwest":
                self.northwestdiv.append(d)
            else:
                self.southwestdiv.append(d)
        




        choose_team_menu = OptionMenu(self.choosingframe, self.chosenteamvar, *self.allnames, command = self.changetohome)
        choose_team_menu.grid(row = 1, column= 0, padx = 10, pady = 20)
        simall = Button(self.choosingframe, text = "Simulate whole league", command=self.wholeleague)
        simall.grid(row=1, column=1, padx = 10, pady = 20)
        
        self.gamenum = 0
        



        
        self.standing_count = 1
        self.tablebacktobhome = Button(self.standingsframe, text = "Back to Home Frame", command = lambda:self.changeframe(self.standingsframe, self.homeframe))
        self.tablebacktobhome.grid(row = 0, column=0, padx=10, pady = 5)
        stats_east = Label(self.standingsframe, text = "Eastern Confrence", relief=RIDGE, bd = 5)
        stats_east.grid(row = 1, column=0, pady= 20)
        wins_east = Label(self.standingsframe, text = "Wins", relief=RIDGE, bd = 5)
        wins_east.grid(row = 1, column = 1, pady=20)
        loss_east = Label(self.standingsframe, text = "Losses", relief=RIDGE, bd = 5)
        loss_east.grid(row = 1, column = 2, pady = 20, padx = 10)
        pct_east = Label(self.standingsframe, text = "Winning PCT%", relief=RIDGE, bd = 5)
        pct_east.grid(row = 1, column = 3, pady = 20, padx = 10)
        self.leagueleaders(self.east_teams)


        stats_west = Label(self.standingsframe, text = "Western Confrence", relief=RIDGE, bd = 5)
        stats_west.grid(row = self.standing_count+1, column=0, pady= 20, padx = 10)
        wins_west = Label(self.standingsframe, text = "Wins", relief=RIDGE, bd = 5)
        wins_west.grid(row = self.standing_count+1, column = 1, pady=20, padx = 10)
        loss_west = Label(self.standingsframe, text = "Losses", relief=RIDGE, bd = 5)
        loss_west.grid(row = self.standing_count+1, column = 2)
        pct_west = Label(self.standingsframe, text = "Winning PCT%", relief=RIDGE, bd = 5)
        pct_west.grid(row = self.standing_count+1, column = 3, pady = 20, padx = 10)
        self.standing_count+=1
        self.leagueleaders(self.west_teams)


    def wholeleague(self):
        pass




    def nextteam(self):
        for t in self.allteams:
            if t.name == self.chosenteamvar.get():
                root.title(t.name)
                return t

            else:
                self.schedule.append(t)

    


    def leagueleaders(self, teams):
        teams.sort(key = lambda x: x.wins)
        winning = 0
        for t in teams:

            self.standing_count +=1
            winning+=1
            team_label = Label(self.standingsframe, text = str(winning) + ". " + t.name)
            team_label.grid(row=self.standing_count, column = 0, padx = 10)
            wins_label = Label(self.standingsframe, text = str(t.wins))
            wins_label.grid(row = self.standing_count, column=1, padx = 10)
            loss_label = Label(self.standingsframe, text = str(t.losses))
            loss_label.grid(row = self.standing_count, column = 2, padx = 10)
            if t.wins + t.losses > 0:

                pct_label = Label(self.standingsframe, text = str(t.wins/(t.wins+t.losses)),)
                pct_label.grid(row = self.standing_count, column= 3, padx = 10)
            else:
                pct_label = Label(self.standingsframe, text = "1")
                pct_label.grid(row = self.standing_count, column = 3, padx = 10)
    

    def divisionleaders(self):
        if self.userteam.division == "Atlantic":
            self.atlanticdiv.sort(key = lambda x:x.wins)
            return self.atlanticdiv.index(self.userteam)
        elif self.userteam.division == "Central":
            self.centraldiv.sort(key = lambda x:x.wins)
            return self.centraldiv.index(self.userteam)
        elif self.userteam.division == "Southeast":
            self.southeastdiv.sort(key = lambda x:x.wins)
            return self.southeastdiv.index(self.userteam)
        elif self.userteam.division == "Pacific":
            self.pacificdiv.sort(key = lambda x:x.wins)
            return self.pacificdiv.index(self.userteam)
        elif self.userteam.division == "Northwest":
            self.northwestdiv.sort(key = lambda x:x.wins)
            return self.northwestdiv.index(self.userteam)
        elif self.userteam.division == "Southwest":
            self.southwestdiv.sort(key = lambda x:x.wins)
            return self.southwestdiv.index(self.userteam)


            


  
    def changetohome(self, x):
        self.choosingframe.pack_forget()
        self.homeframe.pack()
        self.userteam = self.nextteam()
        random.shuffle(self.schedule)
        self.nextgame_label = Label(self.homeframe, text = "Next game: " + self.schedule[self.gamenum].name)
        self.nextgame_label.grid(row = 0, columnspan=3, padx = 10, pady = 20)
        self.div_pos = self.divisionleaders()
        self.record_label = Label(self.homeframe, text = "Record: " + str(self.userteam.wins) + " - " + str(self.userteam.losses))
        self.record_label.grid(row = 1, column = 0, padx = 10, pady = 20)
        self.division_label = Label(self.homeframe, text = "Division Standing: " +str(self.div_pos+1)+"/5") 
        self.division_label.grid(row = 1, column = 1, padx = 10, pady = 20)

        self.confrence_label = Label(self.homeframe, text="")
        self.confrence_label.grid(row = 1, column=2, padx = 10, pady =20)
        if self.userteam.division == "Pacific" or self.userteam.division == "Northwest" or self.userteam.division == "Southwest":
            self.westcon_pos = self.west_teams.index(self.userteam)
            self.confrence_label.configure(text ="Confrence Standing: "+ str(self.westcon_pos+1) +"/15")
        else:
            self.eastcon_pos = self.east_teams.index(self.userteam)
            self.confrence_label.configure(text = "Confrence Standing: " +str(self.eastcon_pos+1)+ "/15")
        self.table = Button(self.homeframe, text = "League Standings", command=lambda: self.changeframe(self.homeframe, self.standingsframe))
        self.table.grid(row =2, column = 0, padx=10, pady = 20)
        self.stats_but = Button(self.homeframe, text = "Player Stats", command=lambda: self.changeframe(self.homeframe, self.standingsframe))
        self.stats_but.grid(row = 2, column=1, padx=10, pady =20)
        self.playgame = Button(self.homeframe, text = "Play Next Game", command= self.changetogame)
        self.playgame.grid(row = 2, column=2, padx = 10, pady=20)
    


    def changeframe(self, f1, f2):
        f1.pack_forget()
        f2.pack()

  
    
    def changetogame(self):
        self.homeframe.pack_forget()
        self.gameframe.pack()
        self.homescore = 0
        self.awayscore = 0
        self.away_label = Label(self.gameframe, text = self.schedule[self.gamenum].name + ": " + str(self.awayscore))
        self.away_label.grid(row=0, column=0, padx = 10, pady = 20)
        self.home_label = Label(self.gameframe, text = self.userteam.name +  ": " + str(self.homescore))
        self.home_label.grid(row = 0, column=1, padx=10, pady =20)
        
        self.playervar = StringVar()
        self.playervar.set(" ")
        awayrb_count = 1
        for i in self.schedule[self.gamenum].players():
            awayrb = Radiobutton(self.gameframe,value = i, text=i, variable=self.playervar)
            awayrb.grid(row = awayrb_count, column=0, padx = 5, pady = 10)
            awayrb_count+=1
        

        
        homerb_count = 1
        for i in self.userteam.players():
            homerb = Radiobutton(self.gameframe, value = i, text = i, variable=self.playervar)
            homerb.grid(row = homerb_count, column=1, padx = 5, pady=10)
            homerb_count+=1
        


        self.threept = Button(self.gameframe, text = "3pt", command = self.addpoints)
        self.threept.grid(row = homerb_count+1, column = 0, padx = 10, pady = 20)
    
    def addpoints(self, num):
        print("Hello World")
        print(self.playervar.get())
        if self.playervar.get() in self.userteam.players():
            self.homescore+=num
            self.home_label.configure(text = self.userteam.name +  ": " + str(self.homescore))
        elif self.playervar.get() in self.schedule[self.gamenum].players():
            self.awayscore+=num
            self.away_label.configure(text = self.schedule[self.gamenum].name + ": " + str(self.awayscore))

if __name__ == "__main__":
    root = Tk()
    bball = BasketballProgram(root)
    root.mainloop()