from tkinter import *

class Screen_PrepareToBattle (Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
        '''
        This method creates all of the widgets the prepare to battle page.
        '''

        Label(self,text = "You", font = "Comic 12 bold", fg = "blue").grid(column = 0, row = 0)
        Label(self, text = "Computer", font = "Comic 12 bold", fg = "red").grid(column = 1, row = 0)

        big_player_img = PhotoImage(file="images/" + self.player1.large_image)
        player_img = Label(self,image = big_player_img)
        player_img.photo = big_player_img
        player_img.grid(row = 1, column = 0)

        big_comp_img = PhotoImage(file="images/" + self.player2.large_image)
        comp_img = Label(self,image = big_comp_img)
        comp_img.photo = big_comp_img
        comp_img.grid(row = 1, column = 1)

        Label(self, text = f"{self.player1.hit_points} HP", font = "Calibri 15").grid()
        Label(self, text = f"{self.player1.dexterity} Dexterity", font = "Calibri 15").grid(column = 0)
        Label(self, text =f"{self.player1.strength} Strength", font = "Calibri 15").grid(column = 0)

        Label(self, text = f"{self.player2.hit_points} HP", font = "Calibri 15").grid(column = 1, row = 2)
        Label(self, text = f"{self.player2.dexterity} Dexterity", font = "Calibri 15").grid(column = 1, row = 3)
        Label(self, text =f"{self.player2.strength} Strength", font = "Calibri 15").grid(column = 1, row = 4)


        Button(self, text = "Commence Battle", font = "Times 14 bold", fg = "aqua", bg = "purple", command = self.commence_battle_clicked).grid(column = 1, sticky = E)
 
    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
        