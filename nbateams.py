class SupportAndStats:
    def __init__(self, name, gametotal, seasontotal, threepct, fgpct, ftpct):
        self.name = name
        self.gametotal = gametotal
        self.seasontotal = seasontotal
        self.threepct = threepct
        self.fgpct = fgpct
        self.ftpct = ftpct
        

class PlayersAndTeams:

    def boston():
        boston_list = []
        boston_list.append(SupportAndStats("Marcus Smart", 0, 0, 33, 42, 79))
        boston_list.append(SupportAndStats("Jaylen Brown", 0, 0, 36, 47, 76))
        boston_list.append(SupportAndStats("Jayson Tatum", 0, 0, 35, 45, 85))
        boston_list.append(SupportAndStats("Robert Williams III", 0, 0, 0, 74, 72))
        boston_list.append(SupportAndStats("Al Hordford", 0, 0, 34, 47, 79))
        return boston_list

    def brooklyn():
        brooklyn_list = []
        brooklyn_list.append(SupportAndStats("Kyrie Irving", 0, 0, 42, 45, 92))
        brooklyn_list.append(SupportAndStats("Seth Curry", 0, 0, 42, 49, 87))
        brooklyn_list.append(SupportAndStats("Kevin Durant", 0, 0, 38, 52, 91))
        brooklyn_list.append(SupportAndStats("Ben Simmons", 0, 0, 15, 56, 60))
        brooklyn_list.append(SupportAndStats("Andre Drummond", 0, 0, 13, 57, 52))
        return brooklyn_list

    def newyork():
        newyork_list = []
        newyork_list.append(SupportAndStats("Immanuel Quickley", 0, 0, 35, 39, 88))
        newyork_list.append(SupportAndStats("Quentin Grimes", 0, 0, 38, 40, 68))
        newyork_list.append(SupportAndStats("RJ Barrett", 0, 0, 34, 44, 71))
        newyork_list.append(SupportAndStats("Obi Toppin", 0, 0, 31, 66, 76))
        newyork_list.append(SupportAndStats("Mitchell Robinson", 0, 0, 0, 76, 49))
        return newyork_list

    def philly():
        philly_list = []
        philly_list.append(SupportAndStats("Tyrese Maxey", 0, 0, 43, 49, 87))
        philly_list.append(SupportAndStats("James Harden", 0, 0, 32, 40, 90))
        philly_list.append(SupportAndStats("Matisse Thybulle", 0, 0, 25, 47, 30))
        philly_list.append(SupportAndStats("Tobias Harris", 0, 0, 39, 51, 86))
        philly_list.append(SupportAndStats("Joel Embiid", 0, 0, 19, 51, 83))
        return philly_list

    def toronto():
        toronto_list = []
        toronto_list.append(SupportAndStats("Fred Van Vleet", 0, 0, 37, 40, 87))
        toronto_list.append(SupportAndStats("Gary Trent Jr.", 0, 0, 38, 41, 85))
        toronto_list.append(SupportAndStats("OG Anunoby", 0, 0, 36, 44, 75))
        toronto_list.append(SupportAndStats("Scottie Barnes", 0, 0, 30, 49, 74))
        toronto_list.append(SupportAndStats("Pascal Siakam", 0, 0, 38, 40, 87))
        return toronto_list

    def chicago():
        chicago_list = []
        chicago_list.append(SupportAndStats("Lonzo Ball", 0, 0, 42, 42, 75))
        chicago_list.append(SupportAndStats("Alex Caruso", 0, 0, 33, 40, 80))
        chicago_list.append(SupportAndStats("Zach LaVine", 0, 0, 39, 48, 85))
        chicago_list.append(SupportAndStats("DeMar DeRozan", 0, 0, 35, 50, 88))
        chicago_list.append(SupportAndStats("Nikola Vucevic", 0, 0, 31, 47, 76))
        return chicago_list

    def cleveland():
        cleveland_list = []
        cleveland_list.append(SupportAndStats("Darius Garland", 0, 0, 38, 46, 89))
        cleveland_list.append(SupportAndStats("Isaac Okoro", 0, 0, 35, 48, 77))
        cleveland_list.append(SupportAndStats("Caris LaVert", 0, 0, 31, 44, 75))
        cleveland_list.append(SupportAndStats("Evan Mobley", 0, 0, 25, 50, 67))
        cleveland_list.append(SupportAndStats("Jarrett Allen", 0, 0, 10, 68, 71))
        return cleveland_list

    def detroit():
        detroit_list = []
        detroit_list.append(SupportAndStats("Cade Cunningham", 0, 0, 31, 42, 85))
        detroit_list.append(SupportAndStats("Hamidou Diallo", 0, 0, 25, 50, 65))
        detroit_list.append(SupportAndStats("Saddiq Bey", 0, 0, 35, 40, 83))
        detroit_list.append(SupportAndStats("Jerami Grant", 0, 0, 36, 43, 84))
        detroit_list.append(SupportAndStats("Isaiah Stewart", 0, 0, 33, 51, 72))
        return detroit_list

    def indiana():
        indiana_list = []
        indiana_list.append(SupportAndStats("Malcom Brogdon", 0, 0, 31, 45, 86))
        indiana_list.append(SupportAndStats("Tyrese Haliburton", 0, 0, 42, 50, 85))
        indiana_list.append(SupportAndStats("Buddy Hield", 0, 0, 36, 45, 89))
        indiana_list.append(SupportAndStats("T.J. Warren", 0, 0, 36, 51, 78))
        indiana_list.append(SupportAndStats("Myles Turner", 0, 0, 35, 49, 77))
        return indiana_list

    def milwaukee():
        milwaukee_list = []
        milwaukee_list.append(SupportAndStats("Jrue Holiday", 0, 0, 41, 40, 76))
        milwaukee_list.append(SupportAndStats("Grayson Allen", 0, 0, 41, 45, 87))
        milwaukee_list.append(SupportAndStats("Khris Middleton", 0, 0, 37, 44, 89))
        milwaukee_list.append(SupportAndStats("Giannis Antetokounmpo", 0, 0, 29, 55, 72))
        milwaukee_list.append(SupportAndStats("Brook Lopez", 0, 0, 36, 47, 87))
        return milwaukee_list

    def atlanta():
        atlanta_list = []
        atlanta_list.append(SupportAndStats("Trae Young", 0, 0, 38, 46, 90))
        atlanta_list.append(SupportAndStats("Kevin Huerter", 0, 0, 39, 45, 81))
        atlanta_list.append(SupportAndStats("De'Andre Hunter", 0, 0, 38, 44, 77))
        atlanta_list.append(SupportAndStats("John Collins", 0, 0, 36, 53, 79))
        atlanta_list.append(SupportAndStats("Clint Capela", 0, 0, 0, 61, 47))
        return atlanta_list

    def charlotte():
        charlotte_list = []
        charlotte_list.append(SupportAndStats("LaMelo Ball", 0, 0, 39, 43, 87))
        charlotte_list.append(SupportAndStats("Terry Rozier III", 0, 0, 37, 44, 85))
        charlotte_list.append(SupportAndStats("Kelly Oubre Jr.", 0, 0, 35, 44, 67))
        charlotte_list.append(SupportAndStats("Miles Bridges", 0, 0, 33, 49, 80))
        charlotte_list.append(SupportAndStats("Mason Plumlee", 0, 0, 0, 64, 39))
        return charlotte_list

    def miami():
        miami_list = []
        miami_list.append(SupportAndStats("Kyle Lowry", 0, 0, 38, 44, 85))
        miami_list.append(SupportAndStats("Duncan Robinson", 0, 0, 37, 40, 84))
        miami_list.append(SupportAndStats("Jimmy Butler", 0, 0, 23, 48, 87))
        miami_list.append(SupportAndStats("P.J. Tucker", 0, 0, 42, 48, 74))
        miami_list.append(SupportAndStats("Bam Adebayo", 0, 0, 0, 56, 75))
        return miami_list

    def orlando():
        orlando_list = []
        orlando_list.append(SupportAndStats("Cole Anthony", 0, 0, 34, 39, 85))
        orlando_list.append(SupportAndStats("Jalen Suggs", 0, 0, 21, 36, 78))
        orlando_list.append(SupportAndStats("Franz Wagner", 0, 0, 35, 47, 86))
        orlando_list.append(SupportAndStats("Wendell Carter Jr.", 0, 0, 33, 53, 69))
        orlando_list.append(SupportAndStats("Mo Bamba", 0, 0, 38, 48, 78))
        return orlando_list

    def washington():
        washington_list = []
        washington_list.append(SupportAndStats("Ish Smith", 0, 0, 36, 46, 60))
        washington_list.append(SupportAndStats("Bradley Beal", 0, 0, 30, 45, 83))
        washington_list.append(SupportAndStats("Corey Kispert", 0, 0, 35, 46, 87))
        washington_list.append(SupportAndStats("Kyle Kuzma", 0, 0, 34, 45, 71))
        washington_list.append(SupportAndStats("Kristaps Porzingis", 0, 0, 37, 48, 87))
        return washington_list

    def golden():
        golden_list = []
        golden_list.append(SupportAndStats("Stephen Curry", 0, 0, 38, 44, 92))
        golden_list.append(SupportAndStats("Klay Thompson", 0, 0, 39, 43, 90))
        golden_list.append(SupportAndStats("Andrew Wiggins", 0, 0, 39, 47, 63))
        golden_list.append(SupportAndStats("Draymond Green", 0, 0, 30, 53, 66))
        golden_list.append(SupportAndStats("Kevon Looney", 0, 0, 0, 57, 60))
        return golden_list

    def lac():
        lac_list = []
        lac_list.append(SupportAndStats("Reggie Jackson", 0, 0, 33, 39, 85))
        lac_list.append(SupportAndStats("Paul George", 0, 0, 35, 42, 86))
        lac_list.append(SupportAndStats("Terance Mann", 0, 0, 37, 48, 78))
        lac_list.append(SupportAndStats("Kawhi Leonard", 0, 0, 38, 49, 86))
        lac_list.append(SupportAndStats("Ivica Zubac", 0, 0, 0, 63, 73))
        return lac_list

    def lal():
        lal_list = []
        lal_list.append(SupportAndStats("Russell Westbrook", 0, 0, 30, 44, 67))
        lal_list.append(SupportAndStats("Malik Monk", 0, 0, 39, 47, 80))
        lal_list.append(SupportAndStats("LeBron James", 0, 0, 36, 53, 76))
        lal_list.append(SupportAndStats("Anthony Davis", 0, 0, 19, 53, 71))
        lal_list.append(SupportAndStats("Dwight Howard", 0, 0, 53, 61, 66))
        return lal_list

    def pheonix():
        pheonix_list = []
        pheonix_list.append(SupportAndStats("Chris Paul", 0, 0, 32, 49, 84))
        pheonix_list.append(SupportAndStats("Devin Booker", 0, 0, 38, 47, 87))
        pheonix_list.append(SupportAndStats("Mikal Bridges", 0, 0, 37, 53, 83))
        pheonix_list.append(SupportAndStats("Jae Crowder", 0, 0, 35, 40, 79))
        pheonix_list.append(SupportAndStats("Deandre Ayton", 0, 0, 37, 63, 75))
        return pheonix_list

    def sac():
        sac_list = []
        sac_list.append(SupportAndStats("De'Aaron Fox", 0, 0, 30, 47, 75))
        sac_list.append(SupportAndStats("Davion Mitchell", 0, 0, 32, 42, 66))
        sac_list.append(SupportAndStats("Harrison Barnes", 0, 0, 39, 47, 83))
        sac_list.append(SupportAndStats("Domantas Sabonis", 0, 0, 24, 55, 74))
        sac_list.append(SupportAndStats("Richaun Holmes", 0, 0, 40, 67, 78))
        return sac_list

    def denver():
        denver_list = []
        denver_list.append(SupportAndStats("Jamal Murray", 0, 0, 37, 45, 88))
        denver_list.append(SupportAndStats("Monte Morris", 0, 0, 40, 48, 87))
        denver_list.append(SupportAndStats("Micheal Porter Jr.", 0, 0, 42, 52, 80))
        denver_list.append(SupportAndStats("Aaron Gordon", 0, 0, 34, 52, 74))
        denver_list.append(SupportAndStats("Nikola Jokic", 0, 0, 34, 58, 81))
        return denver_list

    def min():
        min_list = []
        min_list.append(SupportAndStats("De'Angelo Russell", 0, 0, 34, 41, 83))
        min_list.append(SupportAndStats("Patrick Beverly", 0, 0, 34, 41, 72))
        min_list.append(SupportAndStats("Anthony Edwards", 0, 0, 36, 44, 79))
        min_list.append(SupportAndStats("Jarred Vanderbilt", 0, 0, 14, 58, 66))
        min_list.append(SupportAndStats("Karl-Anthony Towns", 0, 0, 41, 53, 82))
        return min_list

    def oklahoma():
        oklahoma_list = []
        oklahoma_list.append(SupportAndStats("Shai Gilgeous-Alexander", 0, 0, 30, 45, 81))
        oklahoma_list.append(SupportAndStats("Josh Giddey", 0, 0, 26, 42, 71))
        oklahoma_list.append(SupportAndStats("Luguentz Dort", 0, 0, 33, 41, 84))
        oklahoma_list.append(SupportAndStats("Darius Bazley", 0, 0, 30, 42, 69))
        oklahoma_list.append(SupportAndStats("Derrick Favours", 0, 0, 13, 52, 64))
        return oklahoma_list

    def portland():
        portland_list = []
        portland_list.append(SupportAndStats("Damian Lillard", 0, 0, 32, 40, 88))
        portland_list.append(SupportAndStats("Josh Hart", 0, 0, 37, 50, 77))
        portland_list.append(SupportAndStats("Joe Ingles", 0, 0, 41, 45, 77))
        portland_list.append(SupportAndStats("Nassir Little", 0, 0, 33, 46, 73))
        portland_list.append(SupportAndStats("Jusuf Nurkic", 0, 0, 27, 54, 69))
        return portland_list

    def utah():
        utah_list = []
        utah_list.append(SupportAndStats("Mike Conley", 0, 0, 41, 44, 80))
        utah_list.append(SupportAndStats("Donovan Mitchell", 0, 0, 36, 45, 85))
        utah_list.append(SupportAndStats("Bojan Bogdanovic", 0, 0, 39, 46, 86))
        utah_list.append(SupportAndStats("Royce O'Neale", 0, 0, 39, 46, 80))
        utah_list.append(SupportAndStats("Rudy Gobert", 0, 0, 0, 71, 69))
        return utah_list

    def dallas():
        dallas_list = []
        dallas_list.append(SupportAndStats("Luka Doncic", 0, 0, 35, 46, 74))
        dallas_list.append(SupportAndStats("Jalen Brunson", 0, 0, 37, 50, 84))
        dallas_list.append(SupportAndStats("Reggie Bullock", 0, 0, 36, 40, 83))
        dallas_list.append(SupportAndStats("Dorian Finney-Smith", 0, 0, 40, 47, 68))
        dallas_list.append(SupportAndStats("Dwight Powell", 0, 0, 35, 67, 78))
        return dallas_list

    def houston():
        houston_list = []
        houston_list.append(SupportAndStats("Kevin Porter Jr.", 0, 0, 38, 42, 64))
        houston_list.append(SupportAndStats("Jalen Green", 0, 0, 34, 43, 80))
        houston_list.append(SupportAndStats("Eric Gordon", 0, 0, 41, 48, 78))
        houston_list.append(SupportAndStats("Alpren Sengun", 0, 0, 25, 47, 71))
        houston_list.append(SupportAndStats("Christian Wood", 0, 0, 39, 50, 62))
        return houston_list

    def memphis():
        memphis_list = []
        memphis_list.append(SupportAndStats("Ja Morant", 0, 0, 34, 49, 76))
        memphis_list.append(SupportAndStats("Desmond Bane", 0, 0, 44, 46, 90))
        memphis_list.append(SupportAndStats("Ziare Williams", 0, 0, 31, 45, 78))
        memphis_list.append(SupportAndStats("Jaren Jackson Jr.", 0, 0, 32, 42, 82))
        memphis_list.append(SupportAndStats("Steven Adams", 0, 0, 0, 55, 54))
        return memphis_list

    def new_orleans():
        new_orleans_list = []
        new_orleans_list.append(SupportAndStats("Devonte' Graham", 0, 0, 34, 36, 84))
        new_orleans_list.append(SupportAndStats("C.J. McCollum", 0, 0, 39, 49, 67))
        new_orleans_list.append(SupportAndStats("Brandon Ingram", 0, 0, 33, 46, 83))
        new_orleans_list.append(SupportAndStats("Zion Williamson", 0, 0, 33, 60, 68))
        new_orleans_list.append(SupportAndStats("Jonas Valamciunas", 0, 0, 36, 54, 82))
        return new_orleans_list

    def san_antonio():
        san_antonio_list = []
        san_antonio_list.append(SupportAndStats("Dejounte Murray", 0, 0, 33, 46, 79))
        san_antonio_list.append(SupportAndStats("Devin Vassell", 0, 0, 36, 43, 84))
        san_antonio_list.append(SupportAndStats("Doug McDermott", 0, 0, 42, 46, 78))
        san_antonio_list.append(SupportAndStats("Keldon Johnson", 0, 0, 40, 47, 76))
        san_antonio_list.append(SupportAndStats("Jakob Poeltl", 0, 0, 100, 62, 50))
        return san_antonio_list


if __name__ == "__main__":
    setup = PlayersAndTeams