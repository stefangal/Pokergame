import sys, os
import tkinter as tk
from tkinter import messagebox
from Pokergame.Cards import *


class Application(tk.Frame):
    def __init__(self, master, cash):
        tk.Frame.__init__(self, master)
        self.master.title('Pokergame by Stefan G.')
        self.icon = tk.PhotoImage(file='Icon.png')
        self.master.call('wm', 'iconphoto', self.master._w, self.icon)
        self.logo = tk.PhotoImage(file='logo.png').subsample(4, 4)
        self.cash =cash
        self.master.resizable(0, 0)
        self.master.geometry('845x600')
        self.master.configure(background='black')
        self.my_bet = 0
        self.bet_in = 0
        self.img0 = tk.PhotoImage(file='PNG/gray_back.png').subsample(5, 5)
        self.c1 = False
        self.c2 = False
        self.visual()


    def visual(self):
        self.bet_entry = tk.Entry(self.master, font=('Arial', 10, 'bold'), width=5, state='readonly')

        self.entry_label = tk.Label(self.master, text='Your bet:', font=('Arial', 10), bg='black', fg='white')
        self.bet_button = tk.Button(self.master, text='BET', font=('Arial', 7), width=5, command=self.bet, state='disabled')
        self.bet_label = tk.Label(self.master, text="", fg='grey', font=('Arial', 12), justify='right', bg='black')
        self.com_label = tk.Label(self.master, bd=5, bg='darkgrey', fg='red', width=60, height=3 )
        self.com_label_hands = tk.Label(self.master, bd=10, bg='black', fg='yellow', width=60, height=3)
        self.top_text = tk.Label(self.master, text='POKER GAME', bg='black', fg='red', font=('Arial black', 36))
        self.logoL = tk.Label(self.master, image=self.logo)
        self.money = tk.Label(self.master, text='Your money: ' + str(self.cash), bg='black', fg='red', font=('Arial', 12, 'bold'))
        self.bet_on_table_label = tk.Label(self.master, text='BET: ', bg='black', fg='red', font=('Arial', 12, 'bold'))
        self.bet_on_table = tk.Label(self.master, text=self.bet_in, bg='black', fg='red', font=('Arial', 12, 'bold'))

        self.card1 = tk.Button(self.master, image=self.img0, background='black', padx=1, pady=10, command=self.turn_card1)
        self.card2 = tk.Button(self.master, image=self.img0, background='black', padx=1, pady=10, command=self.turn_card2)
        self.card3 = tk.Button(self.master, image=self.img0, background='black', justify='center', padx=10, pady=10)
        self.card4 = tk.Button(self.master, image=self.img0, background='black', justify='center', padx=10, pady=10)
        self.card5 = tk.Button(self.master, image=self.img0, background='black', justify='center', padx=10, pady=10)
        self.card6 = tk.Button(self.master, image=self.img0, background='black', justify='center', padx=10, pady=10)
        self.card7 = tk.Button(self.master, image=self.img0, background='black', justify='center', padx=10, pady=10)
        self.check_button1 = tk.Button(self.master, text='CHECK 1', state='disabled', font=('Arial', 7, 'bold'), width=10, height=3, command=self.check1)
        self.check_button2 = tk.Button(self.master, text='CHECK 2', state='disabled', font=('Arial', 7, 'bold'), width=10, height=3, command=self.check2)
        self.restart_button = tk.Button(self.master, text='RESTART', font=('Arial', 7, 'bold'), width=10, height=3, command=self.restart)
        self.raising_button = tk.Button(self.master, text='RAISE', state='disabled', font=('Arial', 7, 'bold'), width=10, height=3, command=self.raising)
        self.fold_button = tk.Button(self.master, text='FOLD', state='disabled', font=('Arial', 7, 'bold'), width=10, height=3, command=self.fold)

        self.bet_entry.place(x=420, y=100)

        self.money.place(x=550, y=97)
        self.bet_on_table_label.place(x=700, y=97)
        self.bet_on_table.place(x=750, y=97)
        self.top_text.place(x=250, y=15)
        self.logoL.place(x=700, y=15)
        self.com_label_hands.place(x=350, y=200)
        self.com_label.place(x=350, y=130)
        self.entry_label.place(x=350, y=100)
        self.bet_entry.focus_set() # by starting cursor focuses here
        self.bet_button.place(x=470, y=100)
        self.restart_button.place(x=50, y=40)
        self.bet_label.place(x=450, y=10)

        self.card1.place(x=10, y=100)
        self.card2.place(x=180, y=100)
        self.card3.place(x=10, y=350)
        self.card4.place(x=180, y=350)
        self.card5.place(x=350, y=350)
        self.card6.place(x=520, y=350)
        self.card7.place(x=690, y=350)
        self.check_button1.place(x=560, y=280)
        self.check_button2.place(x=730, y=280)
        self.raising_button.place(x=390, y=230)
        self.fold_button.place(x=390, y=280)


    def bet(self):
        if self.bet_entry['state'] != 'readonly' and int(self.bet_entry.get()) <= int(self.cash):
            self.my_bet = self.bet_entry.get()
            self.bet_in += int(self.my_bet)
            self.bet_on_table['text'] = self.bet_in
            self.com_label.configure(text=f'Your bet is now {self.my_bet}. Good luck!', width=60, height=3)
            self.bet_label.configure(fg='yellow', bg='black')
            self.bet_entry.configure(state='readonly', fg='grey')
            self.cash = int(self.cash) - int(self.my_bet)
            self.adjust_my_money()
            self.table_3()
        else:
            self.com_label.configure(text=f'Your monay is not enough !!!', width=60, height=3)

    def turn_card1(self):
        self.card1.configure(image=self.img1)
        self.c1 = True
        if self.c2 == True:
            self.com_label.configure(text='BET NOW')
            self.my_cards_turned()

    def turn_card2(self):
        self.card2.configure(image=self.img2)
        self.c2 = True
        if self.c1 == True:
            self.com_label.configure(text='BET NOW')
            self.my_cards_turned()

    def my_cards_turned(self):
        if self.c1 == True and self.c2 == True:
            self.bet_entry['state'] = 'normal'
            self.bet_button['state'] = 'normal'
            self.raising_button['state'] = 'normal'
            self.fold_button['state'] = 'normal'

    def adjust_my_money(self):
        self.money['text'] = 'Your money: '+ str(self.cash)

    def table_3(self):
        for card in table.on_table:
            if card not in player1.on_hand:
                player1.on_hand.append(card)
        if int(self.my_bet) > 0:
            self.card3['image'] = self.img3
            self.card4['image'] = self.img4
            self.card5['image'] = self.img5
        app.com_label_hands['text'] = my_status(player1)
        app.raising_button['state'] = 'normal'
        app.check_button1['state'] = 'normal'
        return True

    def restart(self):
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def check1(self):
        table.deal_on_table(1)

        for card in table.on_table:
            if card not in player1.on_hand:
                player1.on_hand.append(card)

        self.img6 = tk.PhotoImage(file='PNG/' + str(table.on_table[3]) + '.png').subsample(5, 5)
        self.card6['image'] = self.img6
        self.check_button1['state'] = 'disabled'
        self.check_button2['state'] = 'normal'
        app.com_label_hands['text'] = my_status(player1)

    def check2(self):
        table.deal_on_table(1)

        for card in table.on_table:
            if card not in player1.on_hand:
                player1.on_hand.append(card)

        self.img7 = tk.PhotoImage(file='PNG/' + str(table.on_table[4]) + '.png').subsample(5, 5)
        self.card7['image'] = self.img7
        self.check_button2['state'] = 'disabled'
        app.com_label_hands['text'] = my_status(player1)

    def fold(self):
        messagebox.showinfo("FOLD PRESSED", "Game OVER. Good bye !!!")
        tk._exit()

    def raising(self):
        self.bet_entry['state'] = 'normal'
        self.bet_entry['fg'] = 'black'
        self.bet_entry['text'] = " "
        self.bet_entry.focus_set()


winner = Winner()
table = Table()
deck = Deck()

player1 = Player('Stefan')

deck.create_deck() # create deck of cards and return the self.deck_cards as list
deck.shuffle_deck() # shuffling the self.deck_cards

def my_status(player):
    if winner.five_of_kind(player):
        winner.five_of_kind(player)
        return ('Five of kind')
    elif winner.straight_flush(player):
        winner.straight_flush(player)
        return ('Straight flush')
    elif winner.four_of_kind(player):
        winner.four_of_kind(player)
        return ('Four of kind')
    elif winner.fullhouse(player):
        winner.fullhouse(player)
        return ('Fullhouse')
    elif winner.flush(player):
        winner.flush(player)
        return ('Flush')
    elif winner.straight(player):
        winner.straight(player)
        return ('Straight')
    elif winner.three_of_kind(player):
        winner.three_of_kind(player)
        return ('3 of kind')
    elif winner.two_pair(player):
        winner.two_pair(player)
        return ('2 pairs')
    elif winner.one_pair(player):
        winner.one_pair(player)
        return ('1 pair')
    elif winner.high_card(player):
        winner.high_card(player)
        return ('High card')
    else:
        return ''

root = tk.Tk()
app = Application(root, cash=1500)

app.com_label.configure(text="Cards are SHUFFLED & DEAL is done. Turn your cards!")

player1.get_card(2)
table.deal_on_table(3)

app.img1 = tk.PhotoImage(file='PNG/'+str(player1.on_hand[0])+'.png').subsample(5, 5)
app.img2 = tk.PhotoImage(file='PNG/'+str(player1.on_hand[1])+'.png').subsample(5, 5)
app.img3 = tk.PhotoImage(file='PNG/' + str(table.on_table[0]) + '.png').subsample(5, 5)
app.img4 = tk.PhotoImage(file='PNG/' + str(table.on_table[1]) + '.png').subsample(5, 5)
app.img5 = tk.PhotoImage(file='PNG/' + str(table.on_table[2]) + '.png').subsample(5, 5)

app.mainloop()