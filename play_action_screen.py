from tkinter import *
import tkinter as tk
from tkinter.font import Font
from datetime import datetime
import time
import math
import random
from player_action_team_score import red_score, green_score
from player_live_action import red_action, green_action
from udp_socket import get_recent_hits, udp_socket_receive, udp_socket_send
import threading
import webbrowser


top_left=0;top_right=0;bottom_left=0;bottom_right=0;start_time=0;timer_string=0;middle_frame=0
	
	


def play_action(arr):
	global start_time
	window = Tk()
	WINDOW_WIDTH = 1100
	WINDOW_HEIGHT = 750
	window.title("Player Action")
	window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
	window.configure(bg='black')
	window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
	window.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)
	
	images = [PhotoImage(file="jimmy.png"), PhotoImage(file="rohit.png"), PhotoImage(file="ahmed.png"), PhotoImage(file="fortynite.png")]#create images
		
	
	countdown_string = StringVar()
	countdown_label = Label(window, bg='black', fg='white', textvariable = countdown_string, font=Font(family='Helvetica', size=500, weight='bold'))
	start_time = datetime.now()
	countdown_length=30          ###################################################
	
	def get_codename_team(player_id):
		for i in arr:
			if i[0] is not None:
				if int(i[0]) == player_id:
					return i[1], False #false means red
			if i[2] is not None:
				if int(i[2]) == player_id:
					return i[3], True #true means green
			
		print("player does not exist")
		return None, None
	
	def create_frames():
		global top_left;global top_right;global bottom_left; global bottom_right;global start_time;global timer_string;global middle_frame; global ad_button
		
		a=Label(window, text="ALPHA RED", bg='black', fg='red', font=Font(family='Helvetica', size=30, weight='bold'), anchor='n')
		a.grid(row=0, column = 0)
		b=Label(window, text="ALPHA GREEN", bg='black', fg='green', font=Font(family='Helvetica', size=30, weight='bold'), anchor='n')
		b.grid(row=0, column = 2)
		
		ad_width=150
		frame_height=(WINDOW_HEIGHT-(Font(font=("Helvetica",30)).metrics("linespace")+3))//2
		frame_width=WINDOW_WIDTH//2-ad_width//2
		
		top_left = red_score(window,frame_height,frame_width, arr, [])
		top_right = green_score(window,frame_height,frame_width, arr, [])
		bottom_left = red_action(window,frame_height,frame_width, [])
		bottom_right = green_action(window,frame_height,frame_width, [])
		
		start_time = datetime.now()#get time for timer
		top_left.grid(row=1,column=0, sticky='nw')
		top_right.grid(row=1,column=2, sticky='ne')
		bottom_left.grid(row=2,column=0,sticky='sw')
		bottom_right.grid(row=2,column=2,sticky='se')
		
		
		middle_frame=tk.Frame(master=window,width=ad_width,height=WINDOW_HEIGHT,bg='black')
		
		timer_string = StringVar()
		timer_string.set('6:00')
		timer_label = Label(middle_frame, bg='black', fg='gray80', textvariable = timer_string, font=Font(family='Helvetica', size=20, weight='bold'))
		timer_label.place(x=ad_width/2,y=25, anchor="center")
		
		def when_clicked():
			global ad_button, ad_image1, ad_image2
			if ad_button.image == images[0]:
				webbrowser.open("https://www.artcollectivegallery.com", new=2, autoraise=True)
			elif ad_button.image == images[1]:
				webbrowser.open("https://na.op.gg/summoner/userName=Dragon%20Crossing", new=2, autoraise=True)
			elif ad_button.image == images[2]:
				webbrowser.open("https://na.op.gg/summoner/userName=DeNoobStomper", new=2, autoraise=True)
			elif ad_button.image == images[3]:
				webbrowser.open("https://www.amazon.com/Fort-nite-T-Shirt-Sleeve-Sweatshirt-Hoodie/dp/B09BFKND4R", new=2, autoraise=True)

		
		ad_button=Button(middle_frame, command = when_clicked, borderwidth=0)
		ad_button.place(x=ad_width/2,y=(WINDOW_HEIGHT+50)/2, anchor="center")
		#ad_button.pack(side=BOTTOM,borderwidth=0)

		
		middle_frame.grid(row=0,column=1,rowspan=3)
		
		def regrid(new_frame, old_frame):#redraws frames
			row=old_frame.grid_info().get("row")
			column=old_frame.grid_info().get("column")
			old_frame.grid_remove()
			new_frame.grid(row=row,column=column)
			
			return new_frame
			
		#update functions //////////. call from udp to do real time
		def update_frames():
			global top_left;global top_right;global bottom_left; global bottom_right

			#call udp stuff
			players = get_recent_hits()
			shooters = [None]*len(players)
			shot_players = [None]*len(players)
			shooter_shot_red = []
			shooter_shot_green = []
			for i in range(len(players)):
				players[i][0] = int(players[i][0])
				players[i][1] = int(players[i][1])
				shooter, shooter_team = get_codename_team(players[i][0])
				if shooter == None and shooter_team == None:
					return
				shot, tmp = get_codename_team(players[i][1])
				shooters[i] = shooter
				shot_players[i] = shot
				if shooter_team:
					shooter_shot_green.append((shooter,shot))
				else:
					shooter_shot_red.append((shooter,shot))
				
			
			tmp=red_score(window, frame_height, frame_width, arr, shooters)
			top_left=regrid(tmp, top_left)
			
			tmp = green_score(window, frame_height, frame_width, arr, shooters)
			top_right=regrid(tmp,top_right)
			
			tmp=red_action(window, frame_height, frame_width, shooter_shot_red, bottom_left)
			bottom_left=regrid(tmp, bottom_left)
			
			
			tmp = green_action(window, frame_height, frame_width, shooter_shot_green, bottom_right)
			bottom_right=regrid(tmp,bottom_right)
				
			
			window.after(200, update_frames)
			
		def update_clock():
			global start_time; global timer_string
			curr_time = datetime.now()
			difference = (curr_time - start_time)
			tmp=360-math.floor(difference.total_seconds())
			if tmp < 0:
				print('done')
				window.destroy()
				return
			minute = str(tmp // 60)
			second = str(tmp % 60)
			if len(second) == 1:
				second = '0' + second

			timer_string.set('{a}:{b}'.format(a=minute,b=second))
			window.after(500, update_clock)
			
		def update_ads():
			global middle_frame; global ad_button
			new_ad = random.choice(images)#random new ad
			ad_button.configure(image = new_ad)
			ad_button.image = new_ad
			ad_button.update()

			window.after(15000, update_ads)
		
		
		update_frames()
		update_clock()
		update_ads()
		
		
		

	
	def countdown():
		curr_time = datetime.now()
		difference = (curr_time - start_time)
		countdown_string.set(str(countdown_length-math.floor(difference.total_seconds())))
		countdown_label.update()
		if (int(countdown_string.get()) == 0): #start of everything else
			countdown_label.destroy()
			t1 = threading.Thread(target=udp_socket_receive, daemon = True)#udp socket
			t1.start()
			create_frames()
			
			return
		else:
			window.after(250, countdown)
	
	countdown()
	countdown_label.pack()
	label_x = (WINDOW_WIDTH/2)
	label_y = (WINDOW_HEIGHT/2)
	countdown_label.place(x=label_x,y=label_y, anchor="center")
	
	
	window.mainloop()



if __name__ == '__main__':
	play_action([[1,'Opus',3,'Justin'],[2,'Ahmed',4,'Rohit']])
