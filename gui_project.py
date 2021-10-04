from tkinter import *
import tkinter.messagebox as tkmb
import random



class McDonaldsTill:

    ITEM_PRICES = {
        'Big Mac' : 5.69,
        'Quarter Pounder BLT' : 6.09,
        'McChicken' : 5.39,
        'Nuggets (10PC)' : 6.99,
        'Junior Chicken' : 1.99,
        'Filet-O-Fish' : 5.19,
        'Egg McMuffin' : 4.19,
        'Egg BLT Bagel' : 4.69,
        'Fries' : 1.69
    }
    user_order = list()
    order_total = 0.0

    def __init__(self):
        self.mainWin = Tk()
        self.mainWin.title('Reggie\'s Project')
        self.mainWin.geometry('1600x900')

        self.button_food_frame = Frame(self.mainWin, width = 960, height = 900)
        self.button_food_frame.place(x = 0, y = 120)

        self.big_mac_button = Button(self.button_food_frame, text = 'Big Mac', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Big Mac'))
        self.big_mac_button.place(x = 0, y = 0)

        self.quarter_pounder_button = Button(self.button_food_frame, text = 'Quarter Pounder BLT', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Quarter Pounder BLT'))
        self.quarter_pounder_button.place(x = 0, y = 150)

        self.mc_chicken_button = Button(self.button_food_frame, text = ' McChicken', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('McChicken'))
        self.mc_chicken_button.place(x = 0, y = 300)

        self.nuggets_ten_button = Button(self.button_food_frame, text = 'Chicken Nuggets', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Nuggets (10PC)'))
        self.nuggets_ten_button.place(x = 0, y = 450)

        self.filet_o_fish_button = Button(self.button_food_frame, text = 'Filet-O-Fish', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Filet-O-Fish'))
        self.filet_o_fish_button.place(x = 180, y = 0)

        self.egg_mc_muffin_button = Button(self.button_food_frame, text = 'Egg McMuffin', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Egg McMuffin'))
        self.egg_mc_muffin_button.place(x = 180, y = 150)

        self.egg_blt_bagel_button = Button(self.button_food_frame, text = 'Egg BLT Bagel', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Egg BLT Bagel'))
        self.egg_blt_bagel_button.place(x = 180, y = 300)

        self.fries_button = Button(self.button_food_frame, text = 'Fries', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Fries'))
        self.fries_button.place(x = 180, y = 450)

        self.junior_chkn_button = Button(self.button_food_frame, text = 'Junior Chicken', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Junior Chicken'))
        self.junior_chkn_button.place(x = 368, y = 0)
        
        mainloop()

    def add_item_to_order(self, item_name):
        self.user_order.append(item_name)
        self.order_total += self.ITEM_PRICES[item_name]


gui = McDonaldsTill()
