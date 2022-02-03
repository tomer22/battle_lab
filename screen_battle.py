from tkinter import *

class Screen_Battle (Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        self.button = Button(self, text = "Attack", font = "Times 14 bold", fg = "red", bg = "black", command = self.attack_clicked)
        self.button.grid(column = 0, row = 0, sticky = N)

        self.label1 = Label(self, font = "Helvetica 12 bold")
        self.label1.grid(column = 1, row = 0)
        self.label2 = Label(self, font = "Helvetica 12 bold")
        self.label2.grid(column = 1)
        self.label3 = Label(self, font = "Helvetica 12 bold")
        self.label3.grid(column = 1)
        self.label4 = Label(self, font = "Helvetica 12 bold", fg = "orange")
        self.label4.grid(column = 1)

        Label(self,text = "You", font = "Comic 12 bold", fg = "blue").grid(column = 0, row = 4)
        Label(self, text = "Computer", font = "Comic 12 bold", fg = "red").grid(column = 1, row = 4)

        big_player_img = PhotoImage(file="images/" + self.player1.large_image)
        player_img = Label(self,image = big_player_img)
        player_img.photo = big_player_img
        player_img.grid(row = 5, column = 0)

        big_comp_img = PhotoImage(file="images/" + self.player2.large_image)
        comp_img = Label(self,image = big_comp_img)
        comp_img.photo = big_comp_img
        comp_img.grid(row = 5, column = 1)

        self.hitpoints_label1 = Label(self, text=f"{self.player1.hit_points}/{self.player1_max_hp}", font = "12")
        self.hitpoints_label1.grid()
        self.hitpoints_label2 = Label(self, text=f"{self.player2.hit_points}/{self.player2_max_hp}", font = "12")
        self.hitpoints_label2.grid(column=1, row=6)
        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and (if still alive) the computer.
            2) Updates the labels on the top right with the results of the attacks.
            3) Determines if there was a victor, and if so display that info 
            4) If there is a victor, remove the Attack button.  Create an Exit button to replace it.  

            To remove a widget, use the destroy() method. For example:
    
                self.button.destroy()   
        '''        
        
        self.label1["text"] = self.player1.attack(self.player2)

        if self.player2.hit_points > 0:
            self.label2["text"] = self.player2.attack(self.player1)
        else:
            self.label2["text"] = ""
        self.hitpoints_label1["text"] = f"{self.player1.hit_points}/{self.player1_max_hp}"
        self.hitpoints_label2["text"] = f"{self.player2.hit_points}/{self.player2_max_hp}"

        if self.player1.hit_points <= 0 or self.player2.hit_points <= 0:
            self.button.destroy()
            if self.player1.hit_points <= 0:
                self.label3["text"] = self.player1.get_death_message()
                self.label4["text"] = self.player2.name
            else:
                self.label3["text"] = self.player2.get_death_message()
                self.label4["text"] = f"{self.player1.name} is victorious!"
            
            Button(self, text = "Exit", font = "Times 15 bold", fg = "brown", bg = "yellow", command = self.exit_clicked).grid(column = 1, row = 7, sticky = E)
                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()
  
            
            
            
             