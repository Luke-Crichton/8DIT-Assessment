import nbateams
from tkinter import *
import random
from tkinter import messagebox

"""Support class creates objects for each team. The players and their stats are imported from another file. 
The division variable is to be able to divide the teams into the 6 different divisions in the nba.
For each team, I created a wins and losses value so that each team can keep track of their wins and losses."""
class BasketballSupport:
    def __init__(self, name, division, players, wins, losses):
        self.name = name
        self.division = division
        self.players = players
        self.wins = wins
        self.losses = losses


class BasketballProgram:
    def __init__(self, parent):
        parent.option_add('*font', 'Roboto 12')     # Defaults for backgrond colour, font and font colour set here
        parent.option_add('*Foreground', '#000000')
        parent.option_add('*Background', '#ffffff')
        # I created 6 different frames for 6 different parts of my code.
        # This was extremely useful as being able to swtich between two frames was effecient.
        self.welcomeframe = Frame(parent)
        self.standingsframe = Frame(parent)
        self.choosingframe = Frame(parent)
        self.homeframe = Frame(parent)
        self.gameframe = Frame(parent)
        self.ppgframe = Frame(parent)

        # Below I created most of the instance variables here so I would be able to use them straight away.
        self.west_teams = []
        self.east_teams = []
        allnames = []
        self.allteams = []
        self.playervar = StringVar()
        self.playervar.set(" ")
        self.chosenteamvar = StringVar()
        self.schedule = []

        self.atlanticdiv = []       # Division lists for different teams
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
        self.west_teams.append(BasketballSupport("Dallas Mavericks", "Southwest", nbateams.PlayersAndTeams.dallas, 0, 0))
        self.west_teams.append(BasketballSupport("Houston Rockets", "Southwest", nbateams.PlayersAndTeams.houston, 0, 0))
        self.west_teams.append(BasketballSupport("Memphis Grizzlies", "Southwest", nbateams.PlayersAndTeams.memphis, 0, 0))
        self.west_teams.append(BasketballSupport("New Orleans Pelicans", "Southwest", nbateams.PlayersAndTeams.new_orleans, 0, 0))
        self.west_teams.append(BasketballSupport("San Antonio Spurs", "Southwest", nbateams.PlayersAndTeams.san_antonio, 0, 0))

        welcome_label = Label(self.welcomeframe, text = "Welcome to NBA simulator 2022")
        welcome_label.grid(row = 0, column = 0, padx = 10, pady = 20)
        sim_button = Button(self.welcomeframe, text = "Start Season", command = lambda: self.changeframe(self.welcomeframe, self.choosingframe))
        sim_button.grid(row =1, column=0, padx = 10, pady = 20)
        self.welcomeframe.pack()

        choose_label = Label(self.choosingframe, text = "Which team would you like to choose? ")
        choose_label.grid(row = 0, columnspan = 2, padx = 10, pady = 20)
        # The loop below adds teams to a list which contains every team as well as adding all team names to one list.
        # Unfortunately option menus can only display one dimensional lists so something like *self.allteams.names does not work.
        for i in range(len(self.east_teams)):
            allnames.append(self.east_teams[i].name)
            allnames.append(self.west_teams[i].name)
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

        choose_team_menu = OptionMenu(self.choosingframe, self.chosenteamvar, *allnames, command = lambda x: self.changetohome(0, 0))
        choose_team_menu.grid(row = 1, columnspan= 2, padx = 10, pady = 20)

        """I create any widget that contains an instance variable or changes here and then configure the widgets when they change.
        This way, I widgets don't pakc overthemselves everytime they change."""
        self.away_label = Label(self.gameframe)
        self.home_label = Label(self.gameframe)
        self.nextgame_label = Label(self.homeframe)

        self.tablebacktobhome = Button(self.standingsframe, text = "Back to Home", command = lambda: self.changeframe(self.standingsframe, self.homeframe))
        self.tablebacktobhome.grid(row = 0, column = 0, padx = 10, pady = 5)
        stats_east = Label(self.standingsframe, text = "Eastern Confrence", relief = RIDGE, bd = 5)
        stats_east.grid(row = 1, column=0, pady= 20)
        wins_east = Label(self.standingsframe, text = "Wins", relief = RIDGE, bd = 5)
        wins_east.grid(row = 1, column = 1, pady=20)
        loss_east = Label(self.standingsframe, text = "Losses", relief = RIDGE, bd = 5)
        loss_east.grid(row = 1, column = 2, pady = 20, padx = 10)
        pct_east = Label(self.standingsframe, text = "Winning PCT%", relief = RIDGE, bd = 5)
        pct_east.grid(row = 1, column = 3, pady = 20, padx = 10)
        self.east_team_rank = []
        for i in range(len(self.east_teams)):
            hold_for_big = []
            team_label = Label(self.standingsframe, text = str(i+1))
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

        stats_west = Label(self.standingsframe, text = "Western Confrence", relief=RIDGE, bd = 5)
        stats_west.grid(row = 18, column=0, pady= 20, padx = 10)
        wins_west = Label(self.standingsframe, text = "Wins", relief=RIDGE, bd = 5)
        wins_west.grid(row = 18, column = 1, pady=20, padx = 10)
        loss_west = Label(self.standingsframe, text = "Losses", relief=RIDGE, bd = 5)
        loss_west.grid(row = 18, column = 2)
        pct_west = Label(self.standingsframe, text = "Winning PCT%", relief=RIDGE, bd = 5)
        pct_west.grid(row = 18, column = 3, pady = 20, padx = 10)
        # I use lists to store dynamically created widgets, then cycle through the list and configure that way.

        self.west_team_rank = []
        for i in range(len(self.east_teams)):
            hold_for_big2 = []
            team_label = Label(self.standingsframe, text = str(i+1))
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
        self.ppg_label_holding_list = []

        for i in range(5):
            self.awayrb = Radiobutton(self.gameframe, variable=self.playervar, text = " ", command=self.showpct)
            self.awayrb.grid(row = i+1, column=0, padx = 5, pady = 10)
            self.away_rb_holding_list.append(self.awayrb)

        for i in range(5):
            self.homerb = Radiobutton(self.gameframe, variable = self.playervar, text = " ", command=self.showpct)
            self.homerb.grid(row = i+1, column = 1, padx= 5, pady = 10)
            self.home_rb_holding_list.append(self.homerb)

        for i in range(5):
            self.ppg_label = Label(self.ppgframe, text = " ")
            self.ppg_label.grid(row = i+12, columnspan= 3, padx = 5, pady=10)
            self.ppg_label_holding_list.append(self.ppg_label)

        self.threept = Button(self.gameframe, text = "3pt", command = lambda: self.addpoints(3))
        self.threept.grid(row = 7, column = 0, padx = 10, pady = 20)
        self.twopt = Button(self.gameframe, text = "2pt", command = lambda: self.addpoints(2))
        self.twopt.grid(row = 7, column = 1, padx = 10, pady = 20)
        self.freethrow = Button(self.gameframe, text = "Free Throw", command= lambda: self.addpoints(1))
        self.freethrow.grid(row = 8, column = 0, padx = 10, pady = 20)

    def nextteam(self):
        # This method finds the users selected team and equals it to self.userteam, which is used throughout my code.
        for t in self.allteams:
            if t.name == self.chosenteamvar.get():
                root.title(t.name)
                self.userteam = t
                self.teamplayers = t.players()
            else:
                # Everytime that isn't the users selected team is added to a schedule which the users team cycles through and plays.
                self.schedule.append(t)


    def leagueleaders(self, teams, widgets):
        # This method creates the league standings table. The standings table has it's own seperate frame.
        self.homeframe.pack_forget()
        self.standingsframe.pack()
        count = 0       # Keeps track of which tema is being placed where.
        for w in widgets:       # A list of widgets and a list of one of the two confrences are passed in and cycled through.
            w[0].configure(text = str(count+1) + ". " + teams[count].name)      # Displays the team name and position 
            w[1].configure(text = str(teams[count].wins))
            w[2].configure(text = str(teams[count].losses))
            if teams[count].wins + teams[count].losses != 0:
                w[3].configure(text = "{:.2f}".format(teams[count].wins/(teams[count].wins + teams[count].losses)))     # Displays the teams winning percentage which is the amount of wins / amount of games played
            count += 1

    def divisionleaders(self):
        # This method calculates the users teams position in their division.
        # The method first need to find the users teams' division and then sorts the list by wins then returns where the users team is 
        if self.userteam.division == "Atlantic":
            self.atlanticdiv.sort(key = lambda x: x.wins, reverse=TRUE)
            return self.atlanticdiv.index(self.userteam) + 1
        elif self.userteam.division == "Central":
            self.centraldiv.sort(key = lambda x: x.wins, reverse=TRUE)
            return self.centraldiv.index(self.userteam) + 1
        elif self.userteam.division == "Southeast":
            self.southeastdiv.sort(key = lambda x: x.wins, reverse=TRUE)
            return self.southeastdiv.index(self.userteam) + 1
        elif self.userteam.division == "Pacific":
            self.pacificdiv.sort(key = lambda x: x.wins, reverse=TRUE)
            return self.pacificdiv.index(self.userteam) + 1
        elif self.userteam.division == "Northwest":
            self.northwestdiv.sort(key = lambda x: x.wins, reverse=TRUE)
            return self.northwestdiv.index(self.userteam) + 1
        elif self.userteam.division == "Southwest":
            self.southwestdiv.sort(key = lambda x: x.wins, reverse=TRUE)
            return self.southwestdiv.index(self.userteam) + 1

    def changetohome(self, x, y):
        """ This method is the main method, hence the name home.
        The method displays the next game the user plays as well as their conference standings, division standings and their record.
        The user is also able to access the standings and their teams points per game leaders. 
        The method passes in 2 vairables. y is not used as it is a placeholder variable for the option menu. """
        self.choosingframe.pack_forget()
        self.homeframe.pack()
        if x == 0:      # x is used to prevent the game number to be reset and the schedule to be reset as well.
            self.gamenum = 0
            self.nextteam()
            random.shuffle(self.schedule)

        
        self.awayteam = self.schedule[self.gamenum]
        self.nextgame_label.grid(row = 0, columnspan=3, padx = 10, pady = 20)
        self.nextgame_label.configure(text = "Next game: {}".format(self.awayteam.name))

        self.div_pos = self.divisionleaders()
        self.record_label = Label(self.homeframe, text = "Regular Season Record: {} - {}".format(self.userteam.wins, self.userteam.losses))
        self.record_label.grid(row = 1, column = 0, padx = 10, pady = 20)
        self.division_label = Label(self.homeframe, text = "Division Standing: {}/5".format(self.div_pos))
        self.division_label.grid(row = 1, column = 1, padx = 10, pady = 20)

        self.confrence_label = Label(self.homeframe, text="")
        self.confrence_label.grid(row = 1, column=2, padx = 10, pady =20)
        self.west_teams.sort(key = lambda x: x.wins, reverse = TRUE)
        self.east_teams.sort(key = lambda x: x.wins, reverse = TRUE)

        if self.userteam in self.west_teams:
            self.confrence_label.configure(text = "Confrence Standing: {}/15".format(self.west_teams.index(self.userteam) + 1))
        elif self.userteam in self.east_teams:
            self.confrence_label.configure(text = "Confrence Standing: {}/15".format(self.east_teams.index(self.userteam) + 1))

        self.table = Button(self.homeframe, text = "League Standings", command= lambda: [self.leagueleaders(self.east_teams, self.east_team_rank), self.leagueleaders(self.west_teams, self.west_team_rank)])
        self.table.grid(row =2, column = 0, padx=10, pady = 20)
        self.stats_but = Button(self.homeframe, text = "Player Stats", command=self.ppg)
        self.stats_but.grid(row = 2, column=1, padx=10, pady =20)
        self.playgame = Button(self.homeframe, text = "Play Next Game", command= self.changetogame)
        self.playgame.grid(row = 2, column=2, padx = 10, pady=20)

    def ppg(self):
        # This method displays the user's teams' player's points per game averages. This is created by dividing their seasonal total by the amount of games they played.
        self.homeframe.pack_forget()
        self.ppgframe.pack()
        self.ppgbacktohome = Button(self.ppgframe, text = "Back to Home Frame", command = lambda: self.changeframe(self.ppgframe, self.homeframe))
        self.ppgbacktohome.grid(row = 0, column=0, padx = 5, pady = 5)
        self.stat_label = Label(self.ppgframe, text = "Points Per Game for the players of the {}".format(self.userteam.name))
        self.stat_label.grid(row = 1, columnspan=3, padx = 10, pady = 5)
        if self.userteam.wins + self.userteam.losses != 0:
            for i in self.teamplayers:
                self.ppg_label_holding_list[self.teamplayers.index(i)].configure(text = "{}: {:.2f} ppg".format(i.name, i.seasontotal/(self.userteam.wins+self.userteam.losses)))
        else:
            for i in self.teamplayers:
                self.ppg_label_holding_list[self.teamplayers.index(i)].configure(text = i.name + ": 0 PPG")

    def changeframe(self, f1, f2):
        # This is just a basic method to change frames dynamically without needing to create entirely different functions.
        f1.pack_forget()
        f2.pack()

    def changetogame(self):
        """This method is the game frame where the user plays the other team."""
        self.homeframe.pack_forget()
        self.gameframe.pack()
        self.homescore = 0          # The user's teams' score
        self.awayscore = 0
        self.awayteam = self.schedule[self.gamenum]
        self.awayteamplayers = self.schedule[self.gamenum].players()
        self.away_label.configure(text = "{}: {}".format(self.awayteam.name ,self.awayscore))       # Away teams score label
        self.away_label.grid(row=0, column=0, padx = 10, pady = 20)
        self.home_label.configure(text = "{}: {}".format(self.userteam.name, self.homescore))       # Home teams score label
        self.home_label.grid(row = 0, column=1, padx=10, pady =20)

        self.rb_refresh(self.awayteamplayers, self.away_rb_holding_list)
        
        self.rb_refresh(self.teamplayers, self.home_rb_holding_list)
        self.playervar.set(" ")

        self.threept.configure(text = "3pt")
        self.twopt.configure(text = "2pt")
        self.freethrow.configure(text = "Free Throw")

        self.finishgame = Button(self.gameframe, text = "Finish Game", command = self.refresher)
        self.finishgame.grid(row = 8, column = 1, padx = 10, pady = 20)

    def rb_refresh(self, players, widgets):
        # This method configures the players. The radiobuttons were already created but the method just configures it to the players name and their score. 
        count = 0
        for i in players:
            widgets[count].configure(text = "{}: {}".format(i.name, i.gametotal), value = i.name, variable = self.playervar)
            count += 1

    

    def addpoints(self, num):
        """This method calculates whether or not the player the user selected made the shot or not. The method passes in whatever shot the user tried.
        The method then creates a random interger and then loops through the users teams players first, checking if the user selected a home or away player.
        After finding the player, the method then determines the type of shot taken and then gets the selected players stat for that shot.
        If the random number generated earlier smaller or equal to the percentage of the shot, the method adds the points to the teams score and the players personal score.
        If the number isn't smaller or equal to their percentage, an error message box comes up, notifying the user that the player missed as well as their percentage."""
        inorout = random.randint(1, 100)
        print(inorout)      # Printing out the number for test purposes
        for a in self.teamplayers:
            if self.playervar.get() == a.name:
                if num == 3:
                    if inorout <= a.threepct:
                        self.homescore += num
                        a.gametotal += num
                        self.home_label.configure(text = "{}: {}".format(self.userteam.name, self.homescore))
                        self.rb_refresh(self.teamplayers, self.home_rb_holding_list)
                    else:
                        messagebox.showerror("Missed", "{} has a 3 point PCT of {}% and he missed.".format(a.name, a.threepct))
                elif num == 2:
                    if inorout <= a.fgpct:
                        self.homescore += num
                        a.gametotal += num
                        self.home_label.configure(text = "{}: {}".format(self.userteam.name, self.homescore))
                        self.rb_refresh(self.teamplayers, self.home_rb_holding_list)
                    else:
                        messagebox.showerror("Missed", "{} has a field goal PCT of {}% and he missed.".format(a.name, a.fgpct))
                elif num == 1:
                    if inorout <= a.ftpct:
                        self.homescore += num
                        a.gametotal += num
                        self.home_label.configure(text = "{}: {}".format(self.userteam.name, self.homescore))
                        self.rb_refresh(self.teamplayers, self.home_rb_holding_list)
                    else:
                        messagebox.showerror("Missed", "{} has a free throw PCT of {}% and he missed.".format(a.name, a.ftpct))
        # If the radiobutton value isn't in the home teams list, the method does the same for the away teams players.
        for t in self.awayteamplayers:
            if self.playervar.get() == t.name:
                if num == 3:
                    if inorout <= t.threepct:
                        self.awayscore += num
                        t.gametotal += num
                        self.away_label.configure(text = "{}: {}".format(self.awayteam.name, self.awayscore))
                        self.rb_refresh(self.awayteamplayers, self.away_rb_holding_list)
                    else:
                        messagebox.showerror("Missed", "{} has a 3 point PCT of {}% and he missed.".format(t.name, t.threepct))
                elif num == 2:
                    if inorout <= t.fgpct:
                        self.awayscore += num
                        t.gametotal += num
                        self.away_label.configure(text = "{}: {}".format(self.awayteam.name, self.awayscore))
                        self.rb_refresh(self.awayteamplayers, self.away_rb_holding_list)
                    else:
                        messagebox.showerror("Missed", "{} has a field goal PCT of {}% and he missed.".format(t.name, t.fgpct))
                elif num == 1:
                    if inorout <= t.ftpct:
                        self.awayscore += num
                        t.gametotal += num
                        self.away_label.configure(text = "{}: {}".format(self.awayteam.name, self.awayscore))
                        self.rb_refresh(self.awayteamplayers, self.away_rb_holding_list)
                    else:
                        messagebox.showerror("Missed", "{} has a free throw PCT of {}% and he missed.".format(t.name, t.ftpct))

    def showpct(self):
        # This method is called from the radiobuttons which shows the players. This configures the labels to show that players percentage for each shot.
        # This is to help the user to decided which shots to take with who.
        for a in self.teamplayers:
            if a.name == self.playervar.get():
                self.threept.configure(text = "3pt ({}%)".format(a.threepct))
                self.twopt.configure(text = "2pt ({}%)".format(a.fgpct))
                self.freethrow.configure(text = "Free Throw ({}%)".format(a.ftpct))
        for a in self.awayteamplayers:
            if a.name == self.playervar.get():
                self.threept.configure(text = "3pt ({}%)".format(a.threepct))
                self.twopt.configure(text = "2pt ({}%)".format(a.fgpct))
                self.freethrow.configure(text = "Free Throw ({}%)".format(a.ftpct))

    def refresher(self):
        """This method is called when the user wants to finish a certain game. The method then determines if the team was the last team in the schdeule.
        If not, the method calculates whether or not the user won or lost, adding whatever the outcome was to the user team's object and the team they just faced.
        However, if the user tries to finish the game as a draw, an error message will pop up telling them to keep playing until a winner.
        After that, the method then shuffles the list with everyteam and loops through the list, excluding the users and the awaytea
        adding wins to the first 14 teams in the list and adding losses to the rest. This evenly distributes wins and losses between all teams.
        From there, the method adds every home players game total to their seasonal total and clears their game total. Then, the game number is increased, going to the next time in the schdeule.
        If the method finds that the game just played was the last, the method executes the same actions, but doesn't increase the game number.
        Instead, the method determines if the user's team came first in their confrence, and if so, the user matchups up against the team that cam first in the other confrence.
        After the game is finished, the user is given the option to keep looking at the standings and ppg leaders or quit the game. If the users team doesn't come first,
        a prompt pops up asking if the user wants to keep looking at the stats or quit the game."""
        self.gamenum = 28       # For testing purposes
        if self.homescore == self.awayscore:
            messagebox.showerror("Tie", "In basketball, there are no ties. Play until there is a winner!")
        elif self.gamenum < len(self.schedule)-1:
            if self.homescore > self.awayscore:
                self.userteam.wins += 1
                self.awayteam.losses += 1
            elif self.homescore < self.awayscore:
                self.userteam.losses += 1
                self.awayteam.wins += 1

            random.shuffle(self.allteams)
            for a in self.allteams:
                if a.name != self.awayteam.name and a.name != self.userteam.name:
                    if self.allteams.index(a) < 14.5:
                        a.wins += 1
                    else:
                        a.losses += 1
            for i in self.teamplayers:
                i.seasontotal += i.gametotal
                i.gametotal = 0
            self.gameframe.pack_forget()
            self.gamenum += 1
            self.changetohome(1, 0)
# Final game
        elif self.gamenum == len(self.schedule)-1:
            if self.homescore > self.awayscore:
                self.userteam.wins += 1
                self.schedule[self.gamenum].losses += 1
            elif self.homescore < self.awayscore:
                self.userteam.losses += 1
                self.schedule[self.gamenum].wins += 1
            random.shuffle(self.allteams)
            for a in self.allteams:
                if a.name != self.schedule[self.gamenum].name and a.name != self.userteam.name:
                    if self.allteams.index(a) < 14.5:
                        a.wins += 1
                    else:
                        a.losses += 1
            for i in self.teamplayers:
                i.seasontotal += i.gametotal
                i.gametotal = 0
            self.east_teams.sort(key = lambda x: x.wins, reverse=TRUE)
            self.west_teams.sort(key = lambda x: x.wins, reverse=TRUE)
# If users team is in the east
            if self.userteam in self.east_teams:
                if self.east_teams.index(self.userteam) == 0:
                    self.homeframe.pack()
                    self.gameframe.pack_forget()
                    self.nextgame_label.configure(text = "Final vs {}".format(self.west_teams[0].name))
                    self.playgame.configure(command = lambda: self.finishedfinal(self.west_teams))
                    self.record_label.configure(text = "Regular Season Record: {} - {}".format(self.userteam.wins, self.userteam.losses))
                    self.confrence_label.configure(text ="Confrence Standing: 1/15")
                    self.div_pos = self.divisionleaders()
                    self.division_label.configure(text = "Division Standing: {}/5".format(self.div_pos))
                else:
                    self.finishednofinal(self.east_teams)
            else:
                if self.west_teams.index(self.userteam) == 0:
                    self.homeframe.pack()
                    self.gameframe.pack_forget()
                    self.nextgame_label.configure(text = "Final vs {}".format(self.east_teams[0].name))
                    self.playgame.configure(command = lambda: self.finishedfinal(self.east_teams))
                    self.record_label.configure(text = "Regular Season Record: {} - {}".format(self.userteam.wins, self.userteam.losses))
                    self.confrence_label.configure(text ="Confrence Standing: 1/15")
                    self.div_pos = self.divisionleaders()
                    self.division_label.configure(text = "Division Standing: {}/5".format(self.div_pos))
# If users team wins confrence
                else:
                    self.finishednofinal(self.west_teams)
# If they don't

    def finishednofinal(self, list):
        # This method prompts the user if they'd like to keep looking at stats or quit if they aren't in the finals.
        # The method configures labels to show the finals matchup and to update the users teams standings.
        reply = messagebox.askquestion("Finished Game", "{} finished {}/15, not making the Finals, would you like to see your standings?".format(self.userteam.name, list.index(self.userteam)+1))
        if reply == "no":
            root.destroy()
        else:
            self.gameframe.pack_forget()
            self.homeframe.pack()
            self.nextgame_label.configure(text = "Finals: {} vs {}".format(self.east_teams[0].name, self.west_teams[0].name))
            self.div_pos = self.divisionleaders()
            self.division_label.configure(text = "Division Standing: {}/5".format(self.div_pos))
            self.record_label.configure(text = "Regular Season Record: {} - {}".format(self.userteam.wins, self.userteam.losses))
            self.confrence_label.configure(text ="Confrence Standing: {}/15".format(list.index(self.userteam) + 1))
            self.playgame.configure(command=lambda: root.destroy(), text = "Finish Playing")

    def finishedfinal(self, list):
        # This method prepares the final by changing the scores back to 0 and by creating the finals opponent
        self.homeframe.pack_forget()
        self.gameframe.pack()
        self.homescore = 0
        self.awayscore = 0
        self.gamenum = self.schedule.index(list[0])
        self.changetogame()
        self.finishgame.configure(command=self.winner)

    def winner(self):
        # This method is simlar to the method where the user does not make the finals, prompting the user to either look at stats or quit.
        if self.homescore > self.awayscore:
            end = messagebox.askquestion("Finished", "The {} won the NBA championship! Would you like to finish playing?".format(self.userteam.name))
            if end == "no":
                self.homeframe.pack()
                self.gameframe.pack_forget()
                self.nextgame_label.configure(text = "Season has Finished, the {} won the title!".format(self.userteam.name))
                self.playgame.configure(command = lambda: root.destroy(), text = "Finish Playing")
            else:
                root.destroy()
        elif self.homescore < self.awayscore:
            end = messagebox.askquestion("Finished", "The {} lost to the {} in the NBA championship final, would you like to finish playing?".format(self.userteam.name, self.awayteam.name))
            if end == "no":
                self.homeframe.pack()
                self.gameframe.pack_forget()
                self.nextgame_label.configure(text = "Season has Finished, the {} won the title!".format(self.awayteam.name))
                self.playgame.configure(command = lambda: root.destroy(), text = "Finish Playing")
            else:
                root.destroy()
        else:
            messagebox.showerror("Tie", "In basketball, there are no ties. Play until there is a winner!")

if __name__ == "__main__":
    root = Tk()
    bball = BasketballProgram(root)
    root.mainloop()
