from tkinter import *
import tkinter.messagebox as tkmb
import random



class McDonaldsTill:

    FOOD_PRICES = {
        'Big Mac' : 5.69,
        'Hamburger' : 1.69,
        'Cheeseburger' : 1.89,
        'Quarter Pounder BLT' : 6.09,
        'Quarter Pounder Cheese' : 5.69,
        'McChicken' : 5.39,
        'Nuggets (10PC)' : 6.99,
        'Junior Chicken' : 1.99,
        'Filet-O-Fish' : 5.19,
        'Egg McMuffin' : 4.19,
        'Egg BLT Bagel' : 4.69,
        'Fries' : 1.69
    }

    DRINK_PRICES = {
        'Coffee' : 1.79,
        'Tea' : 1.79,
        'Coffee Carafe' : 15.99,
        'Latte' : 2.99,
        'Cappuccino' : 2.99,
        'Americano' : 2.19,
        'Mocha' : 2.99,
        'Espresso' : 1.39,
        'Hot Chocolate' : 2.99,
        'Soda' : 2.24,
        'Ice Coffee' : 2.39,
        'Fruit Smoothie' : 3.34,
        'Iced Frappe' : 3.34,
        'Orange Juice' : 1.99,
        'Apple Juice' : 1.99,
        'Milk Bottle' : 1.69,
        'Water Bottle' : 2.19,
        
    }
    
    user_order = list()
    order_total = 0.0

    def __init__(self):
        self.mainWin = Tk()
        self.mainWin.title('Reggie\'s Project')
        self.mainWin.geometry('1440x900')

        self.button_food_frame = Frame(self.mainWin, width = 960, height = 900)
        self.button_food_frame.place(x = 0, y = 120)

        self.button_drink_frame = Frame(self.mainWin, width = 280, height = 900)
        self.button_drink_frame.place(x = 960,y = 120)

        self.big_mac_button = Button(self.button_food_frame, text = 'Big Mac', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Big Mac'))
        self.big_mac_button.place(x = 0, y = 0)

        self.quarter_pounder_blt_button = Button(self.button_food_frame, text = 'Quarter Pounder BLT', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Quarter Pounder BLT'))
        self.quarter_pounder_blt_button.place(x = 0, y = 160)

        self.mc_chicken_button = Button(self.button_food_frame, text = ' McChicken', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('McChicken'))
        self.mc_chicken_button.place(x = 0, y = 320)

        self.nuggets_ten_button = Button(self.button_food_frame, text = 'Chicken Nuggets', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Nuggets (10PC)'))
        self.nuggets_ten_button.place(x = 0, y = 480)

        self.filet_o_fish_button = Button(self.button_food_frame, text = 'Filet-O-Fish', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Filet-O-Fish'))
        self.filet_o_fish_button.place(x = 180, y = 0)

        self.egg_mc_muffin_button = Button(self.button_food_frame, text = 'Egg McMuffin', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Egg McMuffin'))
        self.egg_mc_muffin_button.place(x = 180, y = 160)

        self.egg_blt_bagel_button = Button(self.button_food_frame, text = 'Egg BLT Bagel', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Egg BLT Bagel'))
        self.egg_blt_bagel_button.place(x = 180, y = 320)

        self.fries_button = Button(self.button_food_frame, text = 'Fries', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Fries'))
        self.fries_button.place(x = 180, y = 480)

        self.junior_chkn_button = Button(self.button_food_frame, text = 'Junior Chicken', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Junior Chicken'))
        self.junior_chkn_button.place(x = 360, y = 0)

        self.hamburger_button = Button(self.button_food_frame, text = 'Cheese Burger', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Hamburger'))
        self.hamburger_button.place(x = 360, y = 160)

        self.cheeseburger_button = Button(self.button_food_frame, text = 'Cheeseburger', height = 10, width = 20, font = 'bold', command = lambda: self.add_item_to_order('Cheeseburger'))
        self.cheeseburger_button.place(x = 360, y = 320)

        self.quarter_pounder_cheese_button = Button(self.button_food_frame, text = 'Quarter Pounder Cheese', height = 10, width = 20, command = lambda: self.add_item_to_order('Quarter Pounder Cheese'))
        self.quarter_pounder_cheese_button.place(x = 360, y = 480)

        self.coffee_button = Button(self.button_drink_frame, text = 'Coffee', height = 10, width = 20, command = lambda: self.add_item_to_order('Coffee'))
        self.coffee_button.place(x = 0, y = 0)

        
        mainloop()

    def add_item_to_order(self, item_name):
        self.user_order.append(item_name)
        if item_name in FOOD_PRICES.keys():
            self.order_total += self.FOOD_PRICES[item_name]
        elif item_name in DRINK_PRICES.keys():
            self.order_total += self.DRINK_PRICES[item_name]

gui = McDonaldsTill()
