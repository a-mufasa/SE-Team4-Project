from splash_screen import splash_screen
from player_entry_screen import player_entry
from play_action_screen import play_action
from udp_socket import udp_socket_send




splash_screen()
players=player_entry() #array of player ids and
while len(players) > 0 and players[-1][0] == None and players[-1][1] == None: #remove None values
	players.pop()
#print(players)
play_action(players)

