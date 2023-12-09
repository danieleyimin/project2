import tkinter as tk
from project2_gui import VoteGUI
from project2_logic import VoteLogic

if __name__ == "__main__":
    root = tk.Tk()
    vote_logic = VoteLogic()
    vote_gui = VoteGUI(root, vote_logic)
    root.mainloop()
