from tkinter import *
from characters import *

class Screen_CharacterSelection (Frame):
    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)
       # Save the CharacterRoster
        self.roster = roster
        # Save the method reference to which we return control after the player hits "Character Selected"
        self.callback_on_selected = callback_on_selected

        self.grid()

        self.create_widgets()

        
    def create_widgets (self):

        '''
        This method creates all of the widgets character selector page.
        The information about each character should be derived from self.roster, 
        which is a CharacterRoster loaded from battle_characters.txt. 
        The layout should NOT be hard-coded: if you re-order, alter, or remove entries 
        in battle_characters.txt, the layout should automatically reflect those changes. 
        
        ########
        
        The radio buttons on this page should all use the variable "self.character_index_index".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character_index would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character_index has been instantiated for your convenience below.
        
        ########

        Here is some sample code for including an image on a page:   (char is a Character object)
            
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image);
            w= tkinter.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.

            w.grid (ADD PARAMETERS HERE)
        '''

        self.character_index = StringVar()
        self.character_index.set(None)

        Label(self, text="Hit Points", font = "13").grid(row=1, column=3, sticky=N)
        Label(self, text="Dexterity", font = "13").grid(row=1, column=4, sticky=N)
        Label(self, text="Strength", font = "13").grid(row=1, column=5, sticky=N)

        for i in range(len(self.roster.character_list)):
            fighter = self.roster.character_list[i]

            Radiobutton(self, text=fighter.name, font=('Helvetica', 12), variable = self.character_index, value = i).grid(column=0, row=i+1)

            imageSmall = PhotoImage(file="images/" + fighter.small_image)
            fighter_img = Label(self,image = imageSmall)
            fighter_img.photo = imageSmall
            fighter_img.grid(column = 1, row = i+1)

            Label(self, text = fighter.hit_points, font = "13").grid(column = 3, row = i+1)
            Label(self, text = fighter.dexterity, font = "13").grid(column = 4, row = i+1)
            Label(self, text = fighter.strength, font = "13").grid(column = 5, row = i+1)

        Button(self, text = "Select Character!", bg = "red", fg = "black", font = "15", command = self.selected_clicked).grid(column = 4, sticky = E)
         

    def selected_clicked(self):
        ''' This method is to be called when the "Character Selected!" button is clicked. 
            Notice that it passes self.character_index back to the callback method. '''         
        self.callback_on_selected(self.character_index.get())