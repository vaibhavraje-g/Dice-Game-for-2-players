# -*- coding: utf-8 -*-
"""
@author: Gaikwad
"""
from tkinter import *
import random


root = Tk()               #creating instace of class TK , creating base.
root.title("Dice Rolling Game")
root.geometry("720x480")  # size width x height
root.minsize(360,240)     #minimum size while resizing 
root.maxsize(1080,520)    #max size while resizing 


label = Label(root,font=('helvatica',80,'bold'),text = '')
label2 = Label(root,font=('helvatica',15,'bold'),text = '')
label3 = Label(root,font=('comicsansms',15,'bold'),text = '')
label4 = Label(root,font=('comicsansms',10,'bold'),text = '')

sum_dice = 0
sum_dice2 = 0
running_game = TRUE
count = 0 

def roll_dice():
  
    
    global sum_dice
    global running_game
    global count  
    global sum_dice2
    
    
    # this if decides to run game if maximun score is achived then it stops the rolling dice and only exit from game can be done
    if running_game:
        
        
        #dict with key as unicode for special symbols for dice and with respective in val
        dice_int_dict = {'\u2680':1,'\u2681':2,'\u2683':4,'\u2685':6,'\u2682':3,'\u2684':5}
        
        #genrating  list of keys from dict and picking random key  
        op_var = random.choice(list(dice_int_dict.keys()))
        
        #this elif decides where to add score player1(even) or player2(odd)
        if count % 2 == 0:
            
            sum_dice += dice_int_dict[op_var]
            
        else:
            
            sum_dice2 += dice_int_dict[op_var]
        
        
        #display dice using special unicode 
        label.configure(text = op_var)
        label.pack()
        
        #display scores of both players
        label2.configure(text = "SCORE \n \n player1:"+str(sum_dice)+"\t\t\t\t\tplayer2:"+str(sum_dice2))
        label2.pack()
        
        
        #if dice  displays six for any player then another bonus chance to roll dice is given to resp player
        #here count is decremented bcoz after bonus roll score should add to same player if not dec... then it goes to sum of nect player
        
        if dice_int_dict[op_var] == 6 and count % 2 == 0:
            label3.configure(text = " WOW...! \nPLAYER1 YOU GOT SIX \n BONUS ROLL..! \tROLL DICE AGAIN...!")
            label3.pack()
            count -= 1
            
        elif dice_int_dict[op_var] == 6 and count % 2 != 0:
            label3.configure(text = " WOW...! \nPLAYER2 YOU GOT SIX \n BONUS ROLL..! \t ROLL DICE AGAIN...!")
            label3.pack()
            count -= 1
            
        else:
            label3.configure(text = '')
            label3.pack()
            
            
        count += 1
        
        # this elif is to decide the name of winner and exit the game  
        if sum_dice >= 100 or sum_dice2 >= 100:
            
            if sum_dice >= 100:
                player = "PLAYER1"
                
            elif sum_dice2 >= 100: 
                player = "PLAYER2"
                
            #label to dsiplay winner 
            label3.configure(text = " CONGRATULATIONS.....! \n"+player+" IS WINNER \n\n GAME  OVER..! \t\tPRESS EXIT...!")
            label3.pack()
            
            #button to exit game
            button2 = Button(root,font = ('helvatica',20,'bold'),text = 'EXIT',foreground = 'grey',background = 'white', command = root.destroy) 
            button2.pack()
            running_game = FALSE
            
 #this button rolls dice           
button1 = Button(root,font = ('comicsansms',20,'bold'),text = 'Roll Dice',fg = 'green',bg = 'yellow', command = roll_dice)
button1.place(x=30,y=200) 
button1.pack()


root.mainloop()