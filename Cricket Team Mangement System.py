class Player:

    def __init__(self, name, jersey_number, runs):
        self.name = name
        self.jersey_number = jersey_number
        self.runs = runs

    def category(self):
        if self.runs >= 10000:
            return "Excellent"
        elif self.runs >= 5000:
            return "Good"
        else:
            return "Average"

    def display(self):
        print("Player Name:", self.name)
        print("Jersey Number:", self.jersey_number)
        print("Runs:", self.runs)
        print("Category:", self.category())
        print()


class Team:

    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_all(self):
        for player in self.players:
            player.display()


# Create team
team = Team()

# Add players
team.add_player(Player("Virat Kohli", 18, 13848))
team.add_player(Player("KL Rahul", 1, 7500))
team.add_player(Player("Shubman Gill", 77, 2300))

# Display all player details
team.display_all()