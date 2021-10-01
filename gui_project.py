from tkinter import *
import tkinter.messagebox as tkmb
import random


ITEM_PRICES = {
    'Big Mac' : 5.69,
    'Quarter Pounder BLT' : 6.09,
    'McChicken' : 5.39,
    'Nuggets (10PC)' : 6.99,
    'Junior Chicken' : 1.99,
    'Filet-O-Fish' : 5.19,
    'Egg McMuffin' : 4.19,
    'Egg BLT Bagel' : 4.69,
    'Small Fries' : 1.69
}


class McDonaldsTill:
    def __init__(self):
        user_order = []
        total_items = 0
        order_total = 0.0
        self.mainWin = Tk()
        self.mainWin.title('Reggie\'s Project')
        self.mainWin.geometry('1200x720')

        self.item = StringVar()

        self.big_mac_button = Button(self.mainWin, text = 'Big Mac', height = 5, width = 10)
        self.big_mac_button.pack()

        self.big_mac_button.configure(command = lambda: self.add_item_to_order(self.big_mac_button))

        mainloop()

    def add_item_to_order(self, button):
        item_text = button.cget('text')
        user_order[total_items] = item_text
        total_items += 1
        order_total += ITEM_PRICES[item_text]

gui = McDonaldsTill()
