from tkinter import *
import tkinter.messagebox
from tkinter.font import Font
from data_queries import query
import platform





def player_entry():	

	#  CONSTANTS
	DISTANCE_BETWEEN_BUTTONS = 80
	Y_CORD_OF_BUTTON = 580
	STANDARD_PUBLIC_MODE = "Standard public mode"
	WINDOW_WIDTH = 960
	WINDOW_HEIGHT = 675
	RED_CANVAS_X_PLACE = 200
	CANVAS_Y_PLACE = 32
	GREEN_CANVAS_X_PLACE = 500
	NUMBER_OF_ROWS = 15
	
	#creates 2d array for teams
	red_entries= [[None]*2 for i in range(NUMBER_OF_ROWS)]
	green_entries= [[None]*2 for i in range(NUMBER_OF_ROWS)]
	all_entries= [None]*(4*NUMBER_OF_ROWS)# one array to reference all int entries
	current_focus= [None]*2
	
	
	
	# returns string that created on rgb and can be used in bg or fg
	def from_rgb(rgb):
		return "#%02x%02x%02x" % rgb
	
	
	# Function that will called if we click F1
	def clear_key():
		"""
		Here should be returning in player input screen
		"""
		pass
	#functions to navigate widgets
	def next_widget(current_widget):
		i=0
		while (i < len(all_entries) and current_widget != all_entries[i]):
			i+=1
		if i==len(all_entries):#last widget
			i= -1
		return all_entries[i+1]

	def prev_widget(current_widget):
		i=0
		while (i < len(all_entries) and current_widget != all_entries[i]):
			i+=1
		return all_entries[i-1]
		
	def update_all_widgets(current_widget):#make sure same id have same name, most recently entered
		tmp = current_widget.get()
		for i in range(0,len(all_entries),2):
			if all_entries[i].get() == prev_widget(current_widget).get():
				all_entries[i+1].delete(0,END)
				all_entries[i+1].insert(0,tmp)
	
	def focus_in_handle(event):
		if window.focus_get().get() != None:
			print("progress")


	def focus_out_handle(event):
		if (window.focus_get() != None):
			current_focus[1]=current_focus[0]
			current_focus[0]=window.focus_get()
			if (current_focus[0]==current_focus[1]):
				return
			
			widget_name = str(current_focus[1])[-1]
			if (widget_name == "y"):
				widget_name = "1" #first widget ends in y, replace with 0 to avoid error
			if (ord(widget_name) % 2 == 1): #left
				widget_value = current_focus[1].get()
				if (widget_value == ''):
					next_widget(current_focus[1]).delete(0,END)
				if (widget_value.isnumeric()):
					db_codename=query(str(widget_value))
					
					if (db_codename != None):
						next_widget(current_focus[1]).delete(0,END)
						next_widget(current_focus[1]).insert(0,db_codename)
						current_focus[1].focus_set()
						current_focus[0].focus_set()
						#next_widget(next_widget(current_focus[1])).focus_set()
						entry=False
					
				elif widget_value != "":#allow tab between widgets, but no str
					current_focus[1].delete(0,END)
					tkinter.messagebox.showinfo("Invalid Input",  "Please enter a positive integer")
					current_focus[1].focus_set()
					
			else:
				widget_value = current_focus[1].get()
				if (prev_widget(current_focus[1]).get() != ""):#update databse/widgets
					query(prev_widget(current_focus[1]).get(),current_focus[1].get())
					current_focus[0].focus_set()
					#next_widget(current_focus[1]).focus_set()
					update_all_widgets(current_focus[1])
					
				elif current_focus[1].get() != "":
					tkinter.messagebox.showinfo("Invalid Input",  "Please enter ID first")
					prev_widget(current_focus[1]).focus_set()
					current_focus[1].delete(0,END)
					
		else:
			window.focus() #when coming back to window, reset focus
		
	def test_saved_entries(event):
		print("start")
		for i in range(len(red_entries)):
			print(red_entries[i][0].get() + " " + red_entries[i][1].get() + "\t" + green_entries[i][0].get() + " " + green_entries[i][1].get())
		print("end")
		print("start")
		for i in range(len(current_focus)):
			print(str(current_focus[i]))
		print("end")

	# Window settings
	window = Tk()
	window.title("Entry Terminal")
	window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
	window.configure(bg='black')
	window.bind("<F1>", clear_key)
	window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
	window.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)
	
	# Fonts
	helvetica8 = Font(family='Helvetica', size=8, weight='bold')
	helvetica9 = Font(family='Helvetica', size=9, weight='bold')
	helvetica11 = Font(family='Helvetica', size=11, weight='bold')
	helvetica14 = Font(family='Helvetica', size=14, weight='bold')
	helvetica20 = Font(family='Helvetica', size=20, weight='bold')
	
	# UI objects
	f1_button = Button(window, text="F1\nEdit\nGame", width=10, height=4, font=helvetica9, fg="green", bg="black")
	f1_button.place(x=DISTANCE_BETWEEN_BUTTONS * 0, y=Y_CORD_OF_BUTTON)
	
	f2_button = Button(window, text="F2\nGame\nParameters", width=10, height=4, font=helvetica9, fg="green", bg="black")
	f2_button.place(x=DISTANCE_BETWEEN_BUTTONS * 1, y=Y_CORD_OF_BUTTON)
	
	f3_button = Button(window, text="F3\nStart\nGame", width=10, height=4, font=helvetica9, fg="green", bg="black")
	f3_button.place(x=DISTANCE_BETWEEN_BUTTONS * 2, y=Y_CORD_OF_BUTTON)
	
	f5_button = Button(window, text="F5\nPreEntered\nGames", width=10, height=4, font=helvetica9, fg="green", bg="black")
	f5_button.place(x=DISTANCE_BETWEEN_BUTTONS * 4, y=Y_CORD_OF_BUTTON)
	
	f7_button = Button(window, text="F7", width=10, height=4, font=helvetica9, fg="green", bg="black")
	f7_button.place(x=DISTANCE_BETWEEN_BUTTONS * 6, y=Y_CORD_OF_BUTTON)
	
	f8_button = Button(window, text="F8\nView\nGame", width=10, height=4, font=helvetica9, fg="green", bg="black")
	f8_button.place(x=DISTANCE_BETWEEN_BUTTONS * 7, y=Y_CORD_OF_BUTTON)
	
	f10_button = Button(window, text="F10\nFlick\nSync", width=10, height=4, font=helvetica9, fg="green", bg="black")
	f10_button.place(x=DISTANCE_BETWEEN_BUTTONS * 9, y=Y_CORD_OF_BUTTON)
	
	f12_button = Button(window, text="F12\nClear\nGame", width=10, height=4, font=helvetica9, fg="green", bg="black")
	f12_button.place(x=DISTANCE_BETWEEN_BUTTONS * 11, y=Y_CORD_OF_BUTTON)
	
	info_label = Label(window, text="Delete ID to Remove Player, Select to Manually Insert or Edit Codename", width=106,
					   font=helvetica11, fg="black", bg="white")
	info_label.place(x=0, y=Y_CORD_OF_BUTTON + 71)
	
	game_mode_label = Label(window, text=f"Game mode: {STANDARD_PUBLIC_MODE}", font=helvetica11, fg="white", bg="grey")
	game_mode_label.place(x=WINDOW_WIDTH//2-125, y=Y_CORD_OF_BUTTON - 25)
	
	head_label = Label(window, text="Edit Current Game", font=helvetica20, fg="Blue", bg="black")
	head_label.place(x=WINDOW_WIDTH//2-115, y=0)
	
	# Canvases
	red_canvas = Canvas(window, width=300, height=515, bg=from_rgb((51, 0, 0)), highlightthickness=0)
	red_canvas.place(x=RED_CANVAS_X_PLACE, y=CANVAS_Y_PLACE)
	green_canvas = Canvas(window, width=300, height=515, bg=from_rgb((0, 51, 0)), highlightthickness=0)
	green_canvas.place(x=GREEN_CANVAS_X_PLACE, y=CANVAS_Y_PLACE)
	
	red_team_name = Button(red_canvas, text="Red Team", font=helvetica11, fg="white", width=15, bg=from_rgb((51, 0, 0)),
						   state=DISABLED)
	red_team_name.place(x=80, y=2)
	
	green_team_name = Button(green_canvas, text="Green Team", font=helvetica11, fg="white", width=15, bg=from_rgb((0, 51, 0)),
							 state=DISABLED)
	green_team_name.place(x=80, y=2)
	
	
	#  Entries and checkbuttons in Canvases
	for number_of_row in range(NUMBER_OF_ROWS):
	
		red_canvas_number_of_row_label = Label(red_canvas, text=str(number_of_row+1), font=helvetica8,
											   bg=from_rgb((51, 0, 0)), fg="white")
		red_canvas_number_of_row_label.place(x=23,  y=36 + number_of_row * 28)
		red_first_sv = StringVar()#store first entry
		red_canvas_first_entry = Entry(red_canvas, font=helvetica14, width=10, textvariable=red_first_sv)
		red_canvas_first_entry.place(x=40, y=35 + number_of_row * 28)
		red_second_sv = StringVar()#store second entry
		red_canvas_second_entry = Entry(red_canvas, font=helvetica14, width=12, textvariable=red_second_sv)
		red_canvas_second_entry.place(x=155, y=35 + number_of_row * 28)
	
		green_first_sv = StringVar()#store first entry
		green_canvas_first_entry = Entry(green_canvas, font=helvetica14, width=10, textvariable=green_first_sv)
		green_canvas_first_entry.place(x=40, y=35 + number_of_row * 28)
		green_second_sv = StringVar()
		green_canvas_second_entry = Entry(green_canvas, font=helvetica14, width=12, textvariable=green_second_sv)
		green_canvas_second_entry.place(x=155, y=35 + number_of_row * 28)
	
		green_canvas_number_of_row_label = Label(green_canvas, text=str(number_of_row+1), font=helvetica8,
												 bg=from_rgb((0, 51, 0)), fg="white")
		green_canvas_number_of_row_label.place(x=23,  y=36 + number_of_row * 28)
		#store widgets in array
		red_entries[number_of_row][0]=red_canvas_first_entry
		red_entries[number_of_row][1]=red_canvas_second_entry
		green_entries[number_of_row][0]=green_canvas_first_entry
		green_entries[number_of_row][1]=green_canvas_second_entry
		"""
			For next person:
				save values as you think better.
				I think you should save check_values, checkbuttons, first_entries and second_entries in 2d array.
		"""
		
	red_entries[0][0].focus_set()
	current_focus[0]=red_entries[0][0]
	
	for a in range(NUMBER_OF_ROWS):#set all_entries value
		all_entries[4*a]=red_entries[a][0]
		all_entries[4*a+1]=red_entries[a][1]
		all_entries[4*a+2]=green_entries[a][0]
		all_entries[4*a+3]=green_entries[a][1]
	
	#window.bind('<Return>', test_saved_entries)
	#window.bind('<FocusIn>', focus_in_handle)
	window.bind('<FocusOut>', focus_out_handle)
	
	
	return_all_entries=[[None]*4 for i in range(NUMBER_OF_ROWS)]
	def closing(key):
		tmp = window.focus_get()
		if platform.system() != 'Windows': #delete f5 character (only needed on mac)
			tmp.delete(len(tmp.get())-1,END)
		
		if tmp.get().isnumeric():
			next_widget(window.focus_get()).focus_set()
			focus_out_handle("event")
		for i in range (NUMBER_OF_ROWS):
			return_all_entries[i][0]=str(red_entries[i][0].get())
			return_all_entries[i][1]=str(red_entries[i][1].get())
			return_all_entries[i][2]=str(green_entries[i][0].get())
			return_all_entries[i][3]=str(green_entries[i][1].get())
		
		#remove 1 sided values (should already be gone) and move all as high as possible in array
		for i in range(NUMBER_OF_ROWS):
			if return_all_entries[i][0] == '' or return_all_entries[i][1] == '':
				return_all_entries[i][0] = None
				return_all_entries[i][1] = None
			if return_all_entries[i][2] == '' or return_all_entries[i][3] == '':
				return_all_entries[i][2] = None
				return_all_entries[i][3] = None
		
		for i in range(NUMBER_OF_ROWS):
			if return_all_entries[i][0]==None:
				for j in range(i,NUMBER_OF_ROWS):
					if return_all_entries[j][0] != None:
						return_all_entries[i][0] = return_all_entries[j][0]
						return_all_entries[i][1] = return_all_entries[j][1]
						return_all_entries[j][0]=None
						return_all_entries[j][1]=None
			if return_all_entries[i][2]==None:
				for j in range(i,NUMBER_OF_ROWS):
					if return_all_entries[j][2] != None:
						return_all_entries[i][2] = return_all_entries[j][2]
						return_all_entries[i][3] = return_all_entries[j][3]
						return_all_entries[j][2]=None
						return_all_entries[j][3]=None
		window.destroy()
					
			
	#window.protocol("WM_DELETE_WINDOW", closing)
	window.bind('<F5>', closing)
	window.mainloop()
	return return_all_entries
	
if __name__ == '__main__':
	player_entry()