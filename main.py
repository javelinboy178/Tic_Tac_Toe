import tkinter as tk
from tkinter import ttk
from tkinter import *


class TicTacToe(tk.Tk):
    #root holder for the whole game

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.players = {"player 1": StringVar(),
                        "player 2": StringVar()}
        self.frames = {}
        #populate frames with all intended frames for game
        #Downside is all frames when started go though def __init__()
        for F in (StartPage, NamePage, Game, Player1Wins, Player2Wins):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    #page change function used many times throughtout game
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    #Start Page just includes quit and start game buttons
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is Tic-Tac-Toe")
        label.pack()

        button1 = ttk.Button(self, text="Start Game", command=lambda: controller.show_frame(NamePage))
        button1.pack()

        button2 = ttk.Button(self, text="Quit Game", command=quit)
        button2.pack()


class NamePage(tk.Frame):
    #Page to input player 1 and 2 names sends those names to root for later use
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter your names")
        label.pack()

        self.controller = controller

        player1 = ttk.Entry(self, textvariable=self.controller.players["player 1"])
        player1.pack()

        player2 = tk.Entry(self, textvariable=self.controller.players["player 2"])
        player2.pack()

        button1 = ttk.Button(self, text="Enter the Game", command=lambda: controller.show_frame(Game))
        button1.pack()


class Game(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #Title
        label = tk.Label(self, text="Tic-Tac-Toe")
        label.grid(row=0, column=3)

        #Sets the names as labels and places them on the frame for later changing
        self.controller = controller
        self.player1_text = self.controller.players["player 1"].get()
        self.player2_text = self.controller.players["player 2"].get()
        self.player1_label = tk.Label(self)
        self.player2_label = tk.Label(self)
        self.player1_label.grid(row=1, column=3)
        self.player2_label.grid(row=5, column=3)
        self.counter = 0
        self.update_label()
        #Starting player is always player_1
        self.player_1 = True
        self.player_2 = False
        #def lists used in creating game board
        self.frames_list = []
        self.btn_list = []

        self.create_frames_and_buttons()

    #used to update names
    def update_label(self):
         if self.counter < 100:
            self.player1_label.configure(text="player 1: " + self.controller.players["player 1"].get())
            self.player2_label.configure(text="player 2: " + self.controller.players["player 2"].get())
            self.player1_label.after(1000, self.update_label)
            self.player2_label.after(1000, self.update_label)
            self.counter += 1

    #populates game board
    def create_frames_and_buttons(self):
        ndex = 0
        i = 0
        x = 0
        for i in range(3):
            for x in range(3):
                self.frames_list.append(Frame(self, width=100, height=100))
                self.frames_list[ndex].propagate(False)
                self.frames_list[ndex].grid(row=i, column=x, sticky="nsew", padx=2, pady=2)
                self.btn_list.append(Button(self.frames_list[ndex], text="", font="Helvetica 16 bold",
                                            command=lambda ndex=ndex: self.process_turn(ndex)))
                self.btn_list[ndex].pack(expand=True, fill=BOTH)
                x += 1
                ndex += 1
    #checks for win conditions
    def check_win(self):
        if self.btn_list[0]["text"] == self.btn_list[1]["text"] == self.btn_list[2]["text"] == "X":
                self.controller.show_frame(Player1Wins)
        elif self.btn_list[0]["text"] == self.btn_list[1]["text"] == self.btn_list[2]["text"] == "O":
                self.controller.show_frame(Player2Wins)
        elif self.btn_list[3]["text"] == self.btn_list[4]["text"] == self.btn_list[5]["text"] == "X":
                self.controller.show_frame(Player1Wins)
        elif self.btn_list[3]["text"] == self.btn_list[4]["text"] == self.btn_list[5]["text"] == "O":
                self.controller.show_frame(Player2Wins)
        elif self.btn_list[6]["text"] == self.btn_list[7]["text"] == self.btn_list[8]["text"] == "X":
                self.controller.show_frame(Player1Wins)
        elif self.btn_list[6]["text"] == self.btn_list[7]["text"] == self.btn_list[8]["text"] == "O":
                self.controller.show_frame(Player2Wins)
        elif self.btn_list[0]["text"] == self.btn_list[3]["text"] == self.btn_list[6]["text"] == "X":
                self.controller.show_frame(Player1Wins)
        elif self.btn_list[0]["text"] == self.btn_list[3]["text"] == self.btn_list[6]["text"] == "O":
                self.controller.show_frame(Player2Wins)
        elif self.btn_list[1]["text"] == self.btn_list[4]["text"] == self.btn_list[7]["text"] == "X":
                self.controller.show_frame(Player1Wins)
        elif self.btn_list[1]["text"] == self.btn_list[4]["text"] == self.btn_list[7]["text"] == "O":
                self.controller.show_frame(Player2Wins)
        elif self.btn_list[2]["text"] == self.btn_list[5]["text"] == self.btn_list[8]["text"] == "X":
                self.controller.show_frame(Player1Wins)
        elif self.btn_list[2]["text"] == self.btn_list[5]["text"] == self.btn_list[8]["text"] == "O":
                self.controller.show_frame(Player2Wins)
        elif self.btn_list[0]["text"] == self.btn_list[4]["text"] == self.btn_list[8]["text"] == "X":
                self.controller.show_frame(Player1Wins)
        elif self.btn_list[0]["text"] == self.btn_list[4]["text"] == self.btn_list[8]["text"] == "O":
                self.controller.show_frame(Player2Wins)
        elif self.btn_list[2]["text"] == self.btn_list[4]["text"] == self.btn_list[6]["text"] == "X":
                self.controller.show_frame(Player1Wins)
        elif self.btn_list[2]["text"] == self.btn_list[4]["text"] == self.btn_list[6]["text"] == "O":
                self.controller.show_frame(Player2Wins)
        else:
            pass
    #changes button text to player, disables button, changes player turn
    def process_turn(self, ndex):
        if self.player_1:
            self.btn_list[ndex].config(text="X", state="disabled")
            self.player_2 = True
            self.player_1 = False
        else:
            self.btn_list[ndex].config(text="O", state="disabled")
            self.player_2 = False
            self.player_1 = True
        self.check_win()

#Win page for Player 1
class Player1Wins(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.winner_title = self.controller.players["player 1"].get()

        self.big_label = ttk.Label(self, text=self.winner_title, font="Helvetica 20 bold")
        self.big_label.pack()
        self.counter = 0
        self.update_label()

    def update_label(self):
        if self.counter < 100:
            self.big_label.configure(text=self.controller.players["player 1"].get() + " WINS!!!")
            self.big_label.after(1000, self.update_label)
            self.counter += 1

#Win Page for player 2
class Player2Wins(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.winner_title = self.controller.players["player 2"].get()

        self.big_label = ttk.Label(self, text=self.winner_title, font="Helvetica 20 bold")
        self.big_label.pack()

        self.counter = 0
        self.update_label()

    def update_label(self):
        if self.counter < 100:
            self.big_label.configure(text=self.controller.players["player 2"].get() + " WINS!!!")
            self.big_label.after(1000, self.update_label)
            self.counter += 1


app = TicTacToe()
app.mainloop()
