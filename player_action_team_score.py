from tkinter import *
from tkinter.font import Font

#the frame
frame = Frame

#empty arrays to be appended later
#red team
Red_Scores = []         #scores of each player
Red_Score_Labels = []   #labels of those scores
Red_Team_Names = []     #each players name
Red_Name_Labels = []    #labels of those names
Red_High = 0              #index of the high score on red team
Red_Total = 0             #red teams total score
Red_Team_Label = Label  #label for team score

#green team
Green_Scores = []       #Same as above but for the green team
Green_Score_Labels = []       
Green_Team_Names = []
Green_Name_Labels = []
Green_High = 0
Green_Total = 0
Green_Team_Names_Label = Label


#change font size/space between labels
font_size=12
font_buff=3

#indexes for flashers and color arrays
flash_scores = 0
flash_team = 0
flash_red = ["black", "red"]
flash_green = ["black","green"]


def red_score(window, width, height, arr, players):
    #grab all the relevant globals
    global Red_Scores, Red_Team_Names, Red_Score_Labels, Red_Name_Labels, Red_High, Red_Total, Red_Team_Label, frame
    count=0 #weird loop condition so need a counter for label arrays
    #calculate label height based on font size and buffer space
    label_hight= Font(font=("Helvetica",font_size)).metrics("linespace")+font_buff
    #loop through arr get red team names, append relevant arrays, create/place labels
    if len(Red_Team_Names) == 0:
        frame = Frame(master=window, width=width, height=height, bg="black")
        for i in range(len(arr)):
            if arr[i][0] != "None":
                #append names and scores to relevant arrays
                Red_Team_Names.append(arr[i][0])
                Red_Scores.append(0)
                #create/place labels
                Red_Name_Labels.append(Label(frame, text=chr(8227)+arr[i][0],bg="black",fg="red", font=("Helvetica",font_size)))
                Red_Name_Labels[count].place(y=20+(count*label_hight),anchor='w')
                Red_Score_Labels.append(Label(frame, text=str(Red_Scores[count]), bg="black", fg="red", font=("Helvetica",font_size)))
                Red_Score_Labels[count].place(y=20+(count*label_hight), x=width, anchor='e')
                count+=1
        #after loop create/place red team score label
        Red_Team_Label=Label(frame, text=str(Red_Total), bg="black", fg="red", font=("Helvetica",font_size*2))
        Red_Team_Label.place(y=(count*label_hight)+30, x = width, anchor = 'e')

    #loop through players and add new score
    for i in range(len(players)):
        for j in range(len(Red_Team_Names)):
            #if player on red team scored a hit increment their score by 10
            #also increment red team total score by 10
            if players[i] == Red_Team_Names[j]:
                Red_Scores[j]+=10
                Red_Total+=10
                #update labels
                Red_Team_Label.config(text=str(Red_Total))
                Red_Score_Labels[j].config(text=Red_Scores[j])
                #check to see if red teams high score changed
                if Red_Scores[Red_High] < Red_Scores[j]:
                    #in testing depending on when the score changed the player who fell out of the
                    #lead's score would be stuck on black
                    Red_Score_Labels[Red_High].config(fg="red")
                    #reassign the high score
                    Red_High=j

    #can use these here but as it stands now they have to be called from
    #only one of the color_score functions. when they are called in both it breaks. 
    #I think it has to do with them being called.
    #during testing I called them from my test main function and they work well.
    #so closely after one another.
    if len(Green_Score_Labels) != 0:
        window.after(100, Score_flasher)
        window.after(100, Team_flasher)      
    return frame  


def green_score(window, width, height, arr, players):
    #grab all the relevant globals
    global Green_Scores, Green_Team_Names, Green_Score_Labels, Green_Name_Labels, Green_High, Green_Total, Green_Team_Names_Label, frame
    count=0 #weird loop condition so need a counter for label arrays
    #calculate label height based on font size and buffer space
    label_hight= Font(font=("Helvetica",font_size)).metrics("linespace")+font_buff
    #loop through arr and grab green team names, append relevant arrays, create/place labels
    if len(Green_Team_Names) == 0:
        frame = Frame(master=window, width=width, height=height, bg="black")
        for i in range(len(arr)):
            if arr[i][1] != "None":
                #append names and scores to relevant arrays
                Green_Team_Names.append(arr[i][1])
                Green_Scores.append(0)
                #create/place labels
                Green_Name_Labels.append(Label(frame, text=chr(8227)+arr[i][1],bg="black",fg="green", font=("Helvetica",font_size)))
                Green_Name_Labels[count].place(y=20+(count*label_hight),anchor='w')
                Green_Score_Labels.append(Label(frame, text=str(Green_Scores[count]), bg="black", fg="green", font=("Helvetica",font_size)))
                Green_Score_Labels[count].place(y=20+(count*label_hight), x=width, anchor='e')
                count+=1 
        #after loop create/place green team score label
        Green_Team_Names_Label= Label(frame, text= str(Green_Total), bg="black", fg="green", font=("Helvetica",font_size*2))
        Green_Team_Names_Label.place(y=(count*label_hight+30), x = width, anchor = 'e')

    #loop through players and add new score
    for i in range(len(players)):
        for j in range(len(Green_Team_Names)):
            #if player on green team scored a hit increment their score by 10
            #also increment green team total score by 10
            if players[i] == Green_Team_Names[j]:
                Green_Scores[j]+=10
                Green_Total+=10
                #update labels
                Green_Team_Names_Label.config(text=str(Green_Total))
                Green_Score_Labels[j].config(text=Green_Scores[j])
                #check to see if green teams high score  changed
                if Green_Scores[Green_High] < Green_Scores[j]:
                    #in testing depending on when the score changed the player who fell out of the
                    #lead's score would be stuck on black
                    Green_Score_Labels[Green_High].config(fg="green")
                    #reassign the high score
                    Green_High=j


    return frame  


def Score_flasher():
    #grab all the relevant globals
    global Red_Scores, Red_Score_Labels, Red_High, Green_Scores, Green_Score_Labels, Green_High, flash_scores
    
    #check to see which teams high score is higher
    if Red_Scores[Red_High] > Green_Scores[Green_High]:
        Red_Score_Labels[Red_High].config(fg=flash_red[flash_scores])        #change the red high score back and forth so it will flash 
        
    elif Green_Scores[Green_High] > Red_Scores[Red_High]:
        Green_Score_Labels[Green_High].config(fg=flash_green[flash_scores])  #changes the green high score back and forth so it will flash
    
    #increment the score flasher index so it changes color next call
    flash_scores = 1-flash_scores

    
def Team_flasher():
    #grab all the relevant globals
    global Red_Total, Red_Team_Label, Green_Total, Green_Team_Names_Label, flash_team
    
    #check to see which teams total score is higher
    if Red_Total > Green_Total:
        Red_Team_Label.config(fg=flash_red[flash_team])                     #change red team score label so it will flash
        Green_Team_Names_Label.config(fg="green")                           #set green team label back to green just in case
        
    elif Green_Total > Red_Total:
        Green_Team_Names_Label.config(fg=flash_green[flash_team])           #change green team score label so it will flash
        Red_Team_Label.config(fg="red")                                     #set red team label back to red just in case 
    
    #increment the team score flasher so it changes color next call   
    flash_team = 1-flash_team