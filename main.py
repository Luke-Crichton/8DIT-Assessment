import nbateams
from tkinter import *
import random
from tkinter import messagebox

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
        self.playervar = StringVar()
        self.playervar.set(" ")
        self.chosenteamvar = StringVar()
        self.schedule = []
        self.westcon_pos = 0
        self.eastcon_pos = 0
        self.away_label = Label(self.gameframe)
        self.home_label = Label(self.gameframe)
        self.nextgame_label = Label(self.homeframe)
        self.confrence_label = Label(self.homeframe)
        self.awayrb = Radiobutton(self.gameframe, variable=self.playervar)
        self.homescore = 0
        self.awayscore = 0

        
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
        
        



        
        self.east_standing_count = 1
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


        self.west_standing_count = 0
        stats_west = Label(self.standingsframe, text = "Western Confrence", relief=RIDGE, bd = 5)
        stats_west.grid(row = 18, column=0, pady= 20, padx = 10)
        wins_west = Label(self.standingsframe, text = "Wins", relief=RIDGE, bd = 5)
        wins_west.grid(row = 18, column = 1, pady=20, padx = 10)
        loss_west = Label(self.standingsframe, text = "Losses", relief=RIDGE, bd = 5)
        loss_west.grid(row = 18, column = 2)
        pct_west = Label(self.standingsframe, text = "Winning PCT%", relief=RIDGE, bd = 5)
        pct_west.grid(row = 18, column = 3, pady = 20, padx = 10)
        
        
        self.rb_holding_list = []
        
        for i in range(5):
            self.awayrb = Radiobutton(self.gameframe, variable=self.playervar, text = " ")
            self.awayrb.grid(row = i+1, column=0, padx = 5, pady = 10)
            self.rb_holding_list.append(self.awayrb)


    def wholeleague(self):
        pass


    
        




    def nextteam(self):
        for t in self.allteams:
            if t.name == self.chosenteamvar.get():
                root.title(t.name)
                self.userteam = t
                
            else:
                self.schedule.append(t)

    


    def leagueleaders(self, teams, count):
        self.homeframe.pack_forget()
        self.standingsframe.pack()
        teams.sort(key = lambda x: x.wins, reverse = TRUE)
        winning = 0
        for t in teams:


            count +=1
            winning+=1
            team_label = Label(self.standingsframe, text = str(winning) + ". " + t.name)
            team_label.grid(row=count, column = 0, padx = 10)
            wins_label = Label(self.standingsframe, text = str(t.wins))
            wins_label.grid(row =count, column=1, padx = 10)
            loss_label = Label(self.standingsframe, text = str(t.losses))
            loss_label.grid(row =count, column = 2, padx = 10)
            if t.wins + t.losses > 0:

                pct_label = Label(self.standingsframe, text = str(t.wins/(t.wins+t.losses)),)
                pct_label.grid(row = count, column= 3, padx = 10)
            else:
                pct_label = Label(self.standingsframe, text = "1")
                pct_label.grid(row = count, column = 3, padx = 10)
        
    

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
        self.gamenum = 0
        self.nextteam()

        random.shuffle(self.schedule)
        self.nextgame_label.grid(row = 0, columnspan=3, padx = 10, pady = 20)
        self.nextgame_label.configure(text = "Next game: " + self.schedule[self.gamenum].name)
        
        self.div_pos = self.divisionleaders()
        self.record_label = Label(self.homeframe, text = "Record: " + str(self.userteam.wins) + " - " + str(self.userteam.losses))
        self.record_label.grid(row = 1, column = 0, padx = 10, pady = 20)
        self.division_label = Label(self.homeframe, text = "Division Standing: " +str(self.div_pos+1)+"/5") 
        self.division_label.grid(row = 1, column = 1, padx = 10, pady = 20)

        self.confrence_label = Label(self.homeframe, text="")
        self.confrence_label.grid(row = 1, column=2, padx = 10, pady =20)
        
        if self.userteam.division == "Pacific" or self.userteam.division == "Northwest" or self.userteam.division == "Southwest":
            self.westcon_pos = self.west_teams.index(self.userteam) + 1
            self.confrence_label.configure(text ="Confrence Standing: "+ str(self.westcon_pos) +"/15")
            
        else:
            self.eastcon_pos = self.east_teams.index(self.userteam) + 1
            self.confrence_label.configure(text = "Confrence Standing: " +str(self.eastcon_pos)+ "/15")
        
        
        self.table = Button(self.homeframe, text = "League Standings", command= lambda: [self.leagueleaders(self.east_teams, 2), self.leagueleaders(self.west_teams, 19)])
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
        self.away_label.configure(text = self.schedule[self.gamenum].name + ": " + str(self.awayscore))
        self.away_label.grid(row=0, column=0, padx = 10, pady = 20)
        self.home_label.configure(text = self.userteam.name +  ": " + str(self.homescore))
        self.home_label.grid(row = 0, column=1, padx=10, pady =20)
        
        self.awayrb_refresh()
        
            
        

        
        self.homerb_count = 1
        for i in self.userteam.players():
            self.homerb = Radiobutton(self.gameframe, value = i, text = i, variable=self.playervar)
            self.homerb.grid(row = self.homerb_count, column=1, padx = 5, pady=10)
            self.homerb_count+=1
        


        self.threept = Button(self.gameframe, text = "3pt", command = lambda: self.addpoints(3))
        self.threept.grid(row = self.homerb_count+1, column = 0, padx = 10, pady = 20)
        self.twopt = Button(self.gameframe, text = "2pt", command = lambda: self.addpoints(2))
        self.twopt.grid(row = self.homerb_count+1, column = 1, padx = 10, pady = 20)
        self.freethrow = Button(self.gameframe, text = "Free Throw", command= lambda: self.addpoints(1))
        self.freethrow.grid(row = self.homerb_count+2, column = 0, padx = 10, pady = 20)
        self.finishgame = Button(self.gameframe, text = "Finish Game", command = self.refresher)
        self.finishgame.grid(row = self.homerb_count+2, column=1, padx = 10, pady = 20)
    def awayrb_refresh(self):
        self.awayrb_count = 0
        for i in self.schedule[self.gamenum].players():
            self.rb_holding_list[self.awayrb_count].configure(text = i, value = i, variable = self.playervar)
            self.awayrb_count+=1


    
    def addpoints(self, num):
        if self.playervar.get() in self.userteam.players():
            self.homescore+=num
            self.home_label.configure(text = self.userteam.name +  ": " + str(self.homescore))
        elif self.playervar.get() in self.schedule[self.gamenum].players():
            self.awayscore+=num
            self.away_label.configure(text = self.schedule[self.gamenum].name + ": " + str(self.awayscore))

    def refresher(self):
        if self.homescore > self.awayscore:
            self.userteam.wins += 1
            self.schedule[self.gamenum].losses +=1
        elif self.homescore < self.awayscore:
            self.userteam.losses += 1
            self.schedule[self.gamenum].wins+=1
        else:
            messagebox.showerror("Tie", "In basketball, there are no ties. Play until there is a winner!")
        
        self.gameframe.pack_forget()
        self.homeframe.pack()
        random.shuffle(self.allteams)
        for a in self.allteams:
            if a.name != self.schedule[self.gamenum].name and a.name != self.userteam.name:
                if self.allteams.index(a)+1 < 15.5:
                    a.wins+=1
                else:
                    a.losses += 1
        self.gamenum +=1
        self.changetohome(0)
        if self.userteam.division == "Pacific" or self.userteam.division == "Northwest" or self.userteam.division == "Southwest":
            self.westcon_pos = self.west_teams.index(self.userteam) + 1
            self.confrence_label.configure(text ="Confrence Standing: "+ str(self.westcon_pos) +"/15")
            
        else:
            self.eastcon_pos = self.east_teams.index(self.userteam) + 1
            self.confrence_label.configure(text = "Confrence Standing: " +str(self.eastcon_pos)+ "/15")

        
        self.nextgame_label.configure(text = "Next game: " + self.schedule[self.gamenum].name)
        self.away_label.configure(text = self.schedule[self.gamenum].name + ": " + str(self.awayscore))
        self.home_label.configure(text = self.userteam.name +  ": " + str(self.homescore))
if __name__ == "__main__":
    root = Tk()
    bball = BasketballProgram(root)
    root.mainloop()