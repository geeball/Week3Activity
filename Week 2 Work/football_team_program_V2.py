total_pupils = input('Please Enter the Number Of Participants: ' + int)
players_per_team = 4
number_of_players = total_pupils // players_per_team   # // = "whole parts"
inactive_players = total_pupils % number_of_players    # % = "remainder"

print (total_pupils)
print (number_of_players)
print (inactive_players)