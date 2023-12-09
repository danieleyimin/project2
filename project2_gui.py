import tkinter as tk
from tkinter import messagebox
from project2_logic import VoteLogic

class VoteGUI:
    def __init__(self, root, vote_logic):
        self.root = root
        self.vote_logic = vote_logic

        self.vote_frame = tk.Frame(self.root)
        self.candidate_frame = tk.Frame(self.root)

        self.vote_menu()

    def hide_menu(self, menu_frame):
        menu_frame.pack_forget()

    def show_menu(self, menu_frame):
        menu_frame.pack()

    def vote_menu(self):
        self.root.title("VOTE MENU")

        # Hide candidate frame
        self.hide_menu(self.candidate_frame)

        # Show vote frame
        self.show_menu(self.vote_frame)

        tk.Label(self.vote_frame, text="=" * 54).pack()
        tk.Label(self.vote_frame, text="VOTE MENU").pack()
        tk.Label(self.vote_frame, text="=" * 54).pack()

        tk.Button(self.vote_frame, text="Vote", command=self.show_candidate_menu).pack()
        tk.Button(self.vote_frame, text="Exit", command=self.show_results_and_exit).pack()
        
    def show_candidate_menu(self):
        self.hide_menu(self.vote_frame)  # Hide vote frame
        if not hasattr(self, 'candidate_menu_created'):
            self.candidate_menu()  # Create and show candidate menu
            self.candidate_menu_created = True  # Set the flag to indicate that the candidate menu has been created
        else:
            self.show_menu(self.candidate_frame)  # Show existing candidate menu


    def candidate_menu(self):
        self.root.title("CANDIDATE MENU")
        
        # Show candidate frame
        self.show_menu(self.candidate_frame)
        
        tk.Label(self.candidate_frame, text="*" * 54).pack()
        tk.Label(self.candidate_frame, text="CANDIDATE MENU").pack()
        tk.Label(self.candidate_frame, text="*" * 54).pack()
        
        for candidate_id, candidate_name in self.vote_logic.candidates.items():
            tk.Button(self.candidate_frame, text=f"{candidate_id}: {candidate_name}", command=lambda c=candidate_id: self.cast_vote(c)).pack()

    def cast_vote(self, candidate_id):
        self.vote_logic.cast_vote(candidate_id)
        messagebox.showinfo("Vote Cast", f"Voted for {self.vote_logic.candidates[candidate_id]}")

        # Hide candidate frame
        self.hide_menu(self.candidate_frame)

        # Show vote frame
        self.show_menu(self.vote_frame)

    def show_results_and_exit(self):
        self.hide_menu(self.vote_frame)  # Hide vote frame
        self.show_results()

    def show_results(self):
        tk.Label(self.root, text="^" * 54).pack()
        for candidate, count in self.vote_logic.vote_count.items():
            tk.Label(self.root, text=f"{candidate} - {count}").pack()
        tk.Label(self.root, text=f"Total – {sum(self.vote_logic.vote_count.values())}").pack()
        tk.Label(self.root, text="^" * 54).pack()
        self.root.quit()
