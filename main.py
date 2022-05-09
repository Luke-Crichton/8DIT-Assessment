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
        self.teamplayers = 0

        
        self.atlanticdiv = []
        self.centraldiv = []
        self.southeastdiv = []

        self.pacificdiv = []
        self.northwestdiv = []
        self.southwestdiv = []







        self.east_teams.append(BasketballSupport("Boston Celtics", "Atlantic", nbateams.PlayersAndTeams.boston, 0, 0))
        self.east_teams.append(BasketballSupport("Brooklyn Nets", "Atlantic", nbateams.PlayersAndTeams.brooklyn, 0, 0))
        self.east_teams.append(BasketballSupport("New York Knicks", "Atlantic", nbateams.PlayersAndTeams.newyork, 0, 0))
        self.east_teams.append(BasketballSupport("Philadelphia 76ers", "Atlantic", nbateams.PlayersAndTeams.philly, 0, 0))
        self.east_teams.append(BasketballSupport("Toronto Raptors", "Atlantic", nbateams.PlayersAndTeams.toronto, 0, 0))
        self.east_teams.append(BasketballSupport("Chicago Bulls", "Central", nbateams.PlayersAndTeams.chicago, 0, 0))
        self.east_teams.append(BasketballSupport("Cleveland Cavaliers", "Central", nbateams.PlayersAndTeams.cleveland, 0, 0))
        self.east_teams.append(BasketballSupport("Detroit Pistons", "Central", nbateams.PlayersAndTeams.detroit, 0, 0))
        self.east_teams.append(BasketballSupport("Indiana Pacers", "Central", nbateams.PlayersAndTeams.indiana, 0, 0))
        self.east_teams.append(BasketballSupport("Milwaukee Bucks", "Central", nbateams.PlayersAndTeams.milwaukee, 0, 0))
        self.east_teams.append(BasketballSupport("Atlanta Hawks", "Southeast", nbateams.PlayersAndTeams.atlanta, 0, 0))
        self.east_teams.append(BasketballSupport("Charlotte Hornets", "Southeast", nbateams.PlayersAndTeams.charlotte, 0, 0))
        self.east_teams.append(BasketballSupport("Miami Heat", "Southeast", nbateams.PlayersAndTeams.chicago, 0, 0))
        self.east_teams.append(BasketballSupport("Orlando Magic", "Southeast", nbateams.PlayersAndTeams.orlando, 0, 0))
        self.east_teams.append(BasketballSupport("Washington Wizards", "Southeast", nbateams.PlayersAndTeams.washington, 0, 0))

        self.west_teams.append(BasketballSupport("Golden State Warriors", "Pacific", nbateams.PlayersAndTeams.golden, 0, 0))
        self.west_teams.append(BasketballSupport("Los Angeles Clippers", "Pacific", nbateams.PlayersAndTeams.lac, 0, 0))
        self.west_teams.append(BasketballSupport("Los Angeles Lakers", "Pacific", nbateams.PlayersAndTeams.lal, 0, 0))
        self.west_teams.append(BasketballSupport("Pheonix Suns", "Pacific", nbateams.PlayersAndTeams.pheonix, 0, 0))
        self.west_teams.append(BasketballSupport("Sacramento Kings", "Pacific", nbateams.PlayersAndTeams.sac, 0, 0))
        self.west_teams.append(BasketballSupport("Denver Nuggets", "Northwest", nbateams.PlayersAndTeams.denver, 0, 0))
        self.west_teams.append(BasketballSupport("Minnesota Timberwolves", "Northwest", nbateams.PlayersAndTeams.min, 0, 0))
        self.west_teams.append(BasketballSupport("Oklahoma City Thunder", "Northwest", nbateams.PlayersAndTeams.oklahoma, 0, 0))
        self.west_teams.append(BasketballSupport("Portland Trail Blazers", "Northwest", nbateams.PlayersAndTeams.portland, 0, 0))
        self.west_teams.append(BasketballSupport("Utah Jazz", "Northwest", nbateams.PlayersAndTeams.utah, 0, 0))
        self.west_teams.append(BasketballSupport("Dallas Mavreicks", "Southwest", nbateams.PlayersAndTeams.dallas, 0, 0))
        self.west_teams.append(BasketballSupport("Houston Rockets", "Southwest", nbateams.PlayersAndTeams.houston, 0, 0))
        self.west_teams.append(BasketballSupport("Memphis Grizzlies", "Southwest", nbateams.PlayersAndTeams.memphis, 0, 0))
        self.west_teams.append(BasketballSupport("New Orleans Pelicans", "Southwest", nbateams.PlayersAndTeams.new_orleans, 0, 0))
        self.west_teams.append(BasketballSupport("San Antonio Spurs", "Southwest", nbateams.PlayersAndTeams.san_antonio, 0, 0))


        welcome_label = Label(self.welcomeframe, text = "Welcome to NBA simulator 2022")
        welcome_label.grid(row = 0, column = 0, padx =  10, pady = 20)
        sim_button = Button(self.welcomeframe, text = "Start Season", command = lambda: self.changeframe(self.welcomeframe, self.choosingframe))
        sim_button.grid(row =1, column=0, padx = 10, pady = 20)
        self.welcomeframe.pack()

        choose_label = Label(self.choosingframe, text = "Which team would you like to choose? ")
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
        choose_team_menu.grid(row = 1, columnspan= 2, padx = 10, pady = 20)
        
        



        
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
        self.east_team_rank = []
        winning = 0
        for i in range(len(self.east_teams)):
            hold_for_big = []
            winning+=1
            team_label = Label(self.standingsframe, text = str(winning))
            team_label.grid(row=2+i, column = 0, padx = 10)
            hold_for_big.append(team_label)
            wins_label = Label(self.standingsframe, text = "")
            wins_label.grid(row =2+i, column=1, padx = 10)
            hold_for_big.append(wins_label)
            loss_label = Label(self.standingsframe, text = "")
            loss_label.grid(row = 2+i, column = 2, padx = 10)
            hold_for_big.append(loss_label)
            pct_label = Label(self.standingsframe, text = "1")
            pct_label.grid(row = 2+i, column = 3, padx = 10)
            hold_for_big.append(pct_label)
            self.east_team_rank.append(hold_for_big)


        self.west_standing_count = 0
        stats_west = Label(self.standingsframe, text = "Western Confrence", relief=RIDGE, bd = 5)
        stats_west.grid(row = 18, column=0, pady= 20, padx = 10)
        wins_west = Label(self.standingsframe, text = "Wins", relief=RIDGE, bd = 5)
        wins_west.grid(row = 18, column = 1, pady=20, padx = 10)
        loss_west = Label(self.standingsframe, text = "Losses", relief=RIDGE, bd = 5)
        loss_west.grid(row = 18, column = 2)
        pct_west = Label(self.standingsframe, text = "Winning PCT%", relief=RIDGE, bd = 5)
        pct_west.grid(row = 18, column = 3, pady = 20, padx = 10)
        self.west_team_rank = []
        winning = 0
        for i in range(len(self.east_teams)):
            hold_for_big2 = []
            winning+=1
            team_label = Label(self.standingsframe, text = str(winning))
            team_label.grid(row=19+i, column = 0, padx = 10)
            hold_for_big2.append(team_label)
            wins_label = Label(self.standingsframe, text = "")
            wins_label.grid(row =19+i, column=1, padx = 10)
            hold_for_big2.append(wins_label)
            loss_label = Label(self.standingsframe, text = "")
            loss_label.grid(row = 19+i, column = 2, padx = 10)
            hold_for_big2.append(loss_label)
            pct_label = Label(self.standingsframe, text = "1")
            pct_label.grid(row = 19+i, column = 3, padx = 10)
            hold_for_big2.append(pct_label)
            self.west_team_rank.append(hold_for_big2)
        
        self.away_rb_holding_list = []
        self.home_rb_holding_list = []
        
        for i in range(5):
            self.awayrb = Radiobutton(self.gameframe, variable=self.playervar, text = " ")
            self.awayrb.grid(row = i+1, column=0, padx = 5, pady = 10)
            self.away_rb_holding_list.append(self.awayrb)
        for i in range(5):
            self.homerb = Radiobutton(self.gameframe, variable = self.playervar, text = " ")
            self.homerb.grid(row = i+1, column = 1, padx= 5, pady = 10)
            self.home_rb_holding_list.append(self.homerb)


    
        




    def nextteam(self):
        for t in self.allteams:
            if t.name == self.chosenteamvar.get():
                root.title(t.name)
                self.userteam = t
                self.teamplayers = t.players()
                
            else:
                self.schedule.append(t)







    

#standings
    def leagueleaders(self, teams, widgets):
        self.homeframe.pack_forget()
        self.standingsframe.pack()
        teams.sort(key = lambda x: x.wins, reverse = TRUE)
        count = 0
        for w in widgets:
            w[0].configure(text = str(count+1) + ". " + teams[count].name)
            w[1].configure(text = str(teams[count].wins))
            w[2].configure(text = str(teams[count].losses))
            if teams[count].wins + teams[count].losses != 0:
                w[3].configure(text = str(round(teams[count].wins/(teams[count].wins + teams[count].losses), 3)))
            count+=1
        
        




    

    def divisionleaders(self):
        if self.userteam.division == "Atlantic":
            self.atlanticdiv.sort(key = lambda x:x.wins, reverse=TRUE)
            return self.atlanticdiv.index(self.userteam)
        elif self.userteam.division == "Central":
            self.centraldiv.sort(key = lambda x:x.wins, reverse=TRUE)
            return self.centraldiv.index(self.userteam)
        elif self.userteam.division == "Southeast":
            self.southeastdiv.sort(key = lambda x:x.wins, reverse=TRUE)
            return self.southeastdiv.index(self.userteam)
        elif self.userteam.division == "Pacific":
            self.pacificdiv.sort(key = lambda x:x.wins, reverse=TRUE)
            return self.pacificdiv.index(self.userteam)
        elif self.userteam.division == "Northwest":
            self.northwestdiv.sort(key = lambda x:x.wins, reverse=TRUE)
            return self.northwestdiv.index(self.userteam)
        elif self.userteam.division == "Southwest":
            self.southwestdiv.sort(key = lambda x:x.wins, reverse=TRUE)
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
        self.west_teams.sort(key = lambda x:x.wins, reverse = TRUE)
        self.east_teams.sort(key = lambda x:x.wins, reverse=TRUE)
        
        if self.userteam in self.west_teams:
            self.confrence_label.configure(text ="Confrence Standing: "+ str(self.west_teams.index(self.userteam) + 1) +"/15")
        elif self.userteam in self.east_teams:
            self.confrence_label.configure(text = "Confrence Standing: " +str(self.east_teams.index(self.userteam) + 1)+ "/15")
        
        
        self.table = Button(self.homeframe, text = "League Standings", command= lambda: [self.leagueleaders(self.east_teams, self.east_team_rank), self.leagueleaders(self.west_teams, self.west_team_rank)])
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
        self.awayteamplayers = self.schedule[self.gamenum].players()
        self.away_label.configure(text = self.schedule[self.gamenum].name + ": " + str(self.awayscore))
        self.away_label.grid(row=0, column=0, padx = 10, pady = 20)
        self.home_label.configure(text = self.userteam.name +  ": " + str(self.homescore))
        self.home_label.grid(row = 0, column=1, padx=10, pady =20)
        
        self.awayrb_refresh()
        
            
        

        
        self.home_rb_refresh()
        self.playervar.set(" ")

        self.threept = Button(self.gameframe, text = "3pt", command = lambda: self.addpoints(3))
        self.threept.grid(row = 7, column = 0, padx = 10, pady = 20)
        self.twopt = Button(self.gameframe, text = "2pt", command = lambda: self.addpoints(2))
        self.twopt.grid(row = 7, column = 1, padx = 10, pady = 20)
        self.freethrow = Button(self.gameframe, text = "Free Throw", command= lambda: self.addpoints(1))
        self.freethrow.grid(row = 8, column = 0, padx = 10, pady = 20)
        self.finishgame = Button(self.gameframe, text = "Finish Game", command = self.refresher)
        self.finishgame.grid(row = 8, column=1, padx = 10, pady = 20)

    def awayrb_refresh(self):
        self.awayrb_count = 0
        for i in self.awayteamplayers:
            self.away_rb_holding_list[self.awayrb_count].configure(text = i.name + ": " + str(i.gametotal), value = i.name, variable = self.playervar)
            self.awayrb_count+=1
    def home_rb_refresh(self):
        self.homerb_count = 0
        for i in self.teamplayers:
            self.home_rb_holding_list[self.homerb_count].configure(text = i.name + ": " + str(i.gametotal), value = i.name, variable = self.playervar)
            self.homerb_count+=1


    
    def addpoints(self, num):
        inorout = random.randint(1,100)
        print(inorout)
        for a in self.teamplayers:
            if self.playervar.get() == a.name:
                if num == 3:
                    if inorout <= a.threepct:
                        self.homescore+=num
                        a.gametotal += num
                        self.home_label.configure(text = self.userteam.name +  ": " + str(self.homescore))
                        self.home_rb_refresh()
                    else:
                        messagebox.showerror("Missed", a.name + " has a 3 point PCT of " + str(a.threepct) + "% and he missed!")
                elif num == 2:
                    if inorout <= a.fgpct:
                        self.homescore+=num
                        a.gametotal += num
                        self.home_label.configure(text = self.userteam.name +  ": " + str(self.homescore))
                        self.home_rb_refresh()
                    else:
                        messagebox.showerror("Missed", a.name + " has a Field goal PCT of " + str(a.fgpct) + "% and he missed!")
                elif num == 1:
                    if inorout <= a.ftpct:
                        self.homescore+=num
                        a.gametotal += num
                        self.home_label.configure(text = self.userteam.name +  ": " + str(self.homescore))
                        self.home_rb_refresh()
                    else:
                        messagebox.showerror("Missed", a.name + " has a Free Throw point PCT of " + str(a.ftpct) + "% and he missed!")
        for t in self.awayteamplayers:
            if self.playervar.get() == t.name:
                if num == 3:
                    if inorout <= t.threepct:
                        self.awayscore+=num
                        t.gametotal += num
                        self.away_label.configure(text = self.schedule[self.gamenum].name +  ": " + str(self.awayscore))
                        self.awayrb_refresh()
                    else:
                        messagebox.showerror("Missed", t.name + " has a 3 point PCT of " + str(t.threepct) + "% and he missed!")
                elif num == 2:
                    if inorout <= t.fgpct:
                        self.awayscore+=num
                        t.gametotal += num
                        self.away_label.configure(text = self.schedule[self.gamenum].name +  ": " + str(self.awayscore))
                        self.awayrb_refresh()
                    else:
                        messagebox.showerror("Missed", t.name + " has a 3 point PCT of " + str(t.fgpct) + "% and he missed!")
                elif num == 1:
                    if inorout <= a.ftpct:
                        self.awayscore+=num
                        t.gametotal += num
                        self.away_label.configure(text = self.schedule[self.gamenum].name +  ": " + str(self.awayscore))
                        self.awayrb_refresh()
                    else:
                        messagebox.showerror("Missed", t.name + " has a 3 point PCT of " + str(t.ftpct) + "% and he missed!")


    def refresher(self):
        if self.homescore > self.awayscore:
            self.userteam.wins += 1
            self.schedule[self.gamenum].losses +=1
            self.gameframe.pack_forget()
            self.homeframe.pack()
            random.shuffle(self.allteams)
            for a in self.allteams:
                if a.name != self.schedule[self.gamenum].name and a.name != self.userteam.name:
                    if self.allteams.index(a)+1 < 15.5:
                        a.wins+=1
                    else:
                        a.losses += 1
            for i in self.teamplayers:
                i.seasontotal = i.gametotal
                i.gametotal = 0
            for i in self.awayteamplayers:
                i.seasontotal = i.gametotal
                i.gametotal = 0
            self.gamenum +=1
            

            
            self.nextgame_label.configure(text = "Next game: " + self.schedule[self.gamenum].name)
            self.away_label.configure(text = self.schedule[self.gamenum].name + ": " + str(self.awayscore))
            self.home_label.configure(text = self.userteam.name +  ": " + str(self.homescore))
            self.changetohome(0)        
        elif self.homescore < self.awayscore:
            self.userteam.losses += 1
            self.schedule[self.gamenum].wins+=1
            self.gameframe.pack_forget()
            self.homeframe.pack()
            random.shuffle(self.allteams)
            for a in self.allteams:
                if a.name != self.schedule[self.gamenum].name and a.name != self.userteam.name:
                    if self.allteams.index(a)+1 < 15.5:
                        a.wins+=1
                    else:
                        a.losses += 1
            for i in self.teamplayers:
                i.seasontotal = i.gametotal
                i.gametotal = 0
            for i in self.awayteamplayers:
                i.seasontotal = i.gametotal
                i.gametotal = 0
            self.gamenum +=1
            

            
            self.nextgame_label.configure(text = "Next game: " + self.schedule[self.gamenum].name)
            self.away_label.configure(text = self.schedule[self.gamenum].name + ": " + str(self.awayscore))
            self.home_label.configure(text = self.userteam.name +  ": " + str(self.homescore))
            self.changetohome(0)
        else:
            messagebox.showerror("Tie", "In basketball, there are no ties. Play until there is a winner!")
        
        
if __name__ == "__main__":
    root = Tk()
    bball = BasketballProgram(root)
    root.mainloop()