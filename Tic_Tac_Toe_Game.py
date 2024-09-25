from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        
        self.current_player = 'X'
        self.moves_count = 0
        self.buttons = [ttk.Button(master, text=' ', command=lambda i=i: self.button_click(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3, sticky='snew', ipadx=40, ipady=40)

        self.player_turn_label = ttk.Label(master, text="   Player 1 turn!   ")
        self.player_turn_label.grid(row=3, column=0, columnspan=3, sticky='snew', ipadx=40, ipady=40)

        self.restart_button = ttk.Button(master, text='Restart', command=self.restart_game)
        self.restart_button.grid(row=4, column=0, columnspan=3, sticky='snew', ipadx=40, ipady=40)

    def button_click(self, index):
        if self.buttons[index]['text'] == ' ':
            self.buttons[index]['text'] = self.current_player
            self.moves_count += 1
            if self.check_winner():
                tkinter.messagebox.showinfo("Tic Tac Toe", f"Winner is player {1 if self.current_player == 'X' else 2}")
                self.disable_buttons()
            elif self.moves_count == 9:
                tkinter.messagebox.showinfo("Tic Tac Toe", "Match is Draw.")
                self.disable_buttons()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.player_turn_label['text'] = f"   Player {1 if self.current_player == 'X' else 2} turn!   "

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)               # Diagonal
        ]
        return any(all(self.buttons[i]['text'] == self.current_player for i in combo) for combo in winning_combinations)

    def disable_buttons(self):
        for button in self.buttons:
            button.state(['disabled'])

    def restart_game(self):
        self.current_player = 'X'
        self.moves_count = 0
        self.player_turn_label['text'] = "   Player 1 turn!   "
        for button in self.buttons:
            button['text'] = ' '
            button.state(['!disabled'])

if __name__ == "__main__":
    root = Tk()
    app = TicTacToe(root)
    root.mainloop()
