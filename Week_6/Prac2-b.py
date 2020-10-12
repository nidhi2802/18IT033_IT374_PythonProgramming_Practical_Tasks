class Team:
   def show_Team(self):
      print("This is our Team:")

# Player class inherited from Team
class Player(Team):
   PlayerName = ""

   def show_Player(self):
      print(self.PlayerName)
 
# Sports class inherited from Team
class Sports(Team):
   SportsName = ""

   def show_Sports(self):
      print(self.SportsName) 
 
# Sprint class inherited from Player and Sports classes
class Sprint(Player, Sports):
   def show_parent(self):
      print("Player :", self.PlayerName)
      print("Sports :", self.SportsName)

s1 = Sprint()  # Object of Sprint class
s1.PlayerName = "Ellyse Perry"
s1.SportsName = "Cricket"
s1.show_Team()
s1.show_parent()