from tkinter import *
from tkinter.font import Font
from tkinter import messagebox 

# returns string that created on rgb and can be used in bg or fg
def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


# Function that will called if we click F1
def clear_key():
    """
    Here should be returning in player input screen
    """
    pass
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
	NUMBER_OF_ROWS = 16
	
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
	
	info_label = Label(window, text="<Del> to Delete Player, <ins> to Manually insert, or edit codename", width=106,
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
	
	a = [ [1]*4 for i in range(NUMBER_OF_ROWS)]
	print(a)
	
	#  Entries and checkbuttons in Canvases
	for number_of_row in range(NUMBER_OF_ROWS):
		'''red_canvas_check_value = IntVar()
		red_canvas_checkbutton = Checkbutton(red_canvas, variable=red_canvas_check_value, onvalue=1, offvalue=0,
											 bg=from_rgb((51, 0, 0)), activebackground=from_rgb((51, 0, 0)))
		red_canvas_checkbutton.place(x=5, y=32 + number_of_row * 28)
	
		green_canvas_check_value = IntVar()
		green_canvas_checkbutton = Checkbutton(green_canvas, variable=green_canvas_check_value, onvalue=1, offvalue=0,
											   bg=from_rgb((0, 51, 0)), activebackground=from_rgb((0, 51, 0)))
		green_canvas_checkbutton.place(x=5, y=32 + number_of_row * 28)'''
	
		red_canvas_number_of_row_label = Label(red_canvas, text=str(number_of_row), font=helvetica8,
											   bg=from_rgb((51, 0, 0)), fg="white")
		red_canvas_number_of_row_label.place(x=23,  y=36 + number_of_row * 28)
	
		red_canvas_first_entry = Entry(red_canvas, font=helvetica14, width=10)
		red_canvas_first_entry.place(x=40, y=35 + number_of_row * 28)
		red_canvas_second_entry = Entry(red_canvas, font=helvetica14, width=12)
		red_canvas_second_entry.place(x=155, y=35 + number_of_row * 28)
	
		green_canvas_first_entry = Entry(green_canvas, font=helvetica14, width=10)
		green_canvas_first_entry.place(x=40, y=35 + number_of_row * 28)
		green_canvas_second_entry = Entry(green_canvas, font=helvetica14, width=12)
		green_canvas_second_entry.place(x=155, y=35 + number_of_row * 28)
		
		a[number_of_row][0]=red_canvas_first_entry.get()
		print(a)
	
		green_canvas_number_of_row_label = Label(green_canvas, text=str(number_of_row), font=helvetica8,
												 bg=from_rgb((0, 51, 0)), fg="white")
		green_canvas_number_of_row_label.place(x=23,  y=36 + number_of_row * 28)
		"""
			For next person:
				save values as you think better.
				I think you should save check_values, checkbuttons, first_entries and second_entries in 2d array.
		"""
	
	def motion(event):
	  print("Mouse position: (%s %s)" % (event.x, event.y))
	  return
	  
	def something(event_exit_widget):
		'''
		if exiting index, call queries function, if codename returned != None, then insert it into the second box
		else, allow tab into box and once exiting that box, call queries with that index and codename to insert into DB
		'''
	window.bind('<Tab>',motion)
	window.bind('<1>',motion)
	window.mainloop()
	print(a)
