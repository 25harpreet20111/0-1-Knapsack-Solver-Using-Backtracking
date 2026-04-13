import tkinter as tk
from tkinter import messagebox

class KnapsackBacktrackingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("0/1 Knapsack - Backtracking")
        self.root.geometry("600x650")
        self.root.config(bg="#e87414")

        self.best_profit = 0
        self.best_set = []

        self.create_widgets()
        self.create_footer()   # ✅ Footer added

    def create_widgets(self):

        title = tk.Label(self.root,
                         text="🎒 0/1 Knapsack (Backtracking)", 
                         font=("Times New Roman", 20, "bold"),
                         bg="#101039",
                         fg="white")
        title.pack(pady=16)

        frame = tk.Frame(self.root, bg="#101039")
        frame.pack(pady=16)

        tk.Label(frame, text="Weights:",
                 bg="#101039",
                 font=("Times New Roman", 14, "bold"),
                 fg="white").grid(row=0, column=0)

        self.weight_entry = tk.Entry(frame, width=60)
        self.weight_entry.grid(row=0, column=1)

        tk.Label(frame, text="Values:",
                 bg="#101039",
                 font=("Times New Roman", 14, "bold"),
                 fg="white").grid(row=1, column=0)

        self.value_entry = tk.Entry(frame, width=60)
        self.value_entry.grid(row=1, column=1)

        tk.Label(frame, text="Capacity:",
                 bg="#101039",
                 font=("Times New Roman", 14, "bold"),
                 fg="white").grid(row=2, column=0)

        self.capacity_entry = tk.Entry(frame)
        self.capacity_entry.grid(row=2, column=1)

        tk.Button(self.root,
                  text="Solve (Backtracking)",
                  command=self.solve,
                  bg="#4CAF50",
                  fg="white",
                  font=("Times New Roman", 14, "bold"),
                  width=30).pack(pady=14)

        self.result_label = tk.Label(self.root,
                                     text="Result will appear here",
                                     bg="#101039",
                                     fg="yellow",
                                     font=("Times New Roman", 18, "bold"))
        self.result_label.pack(pady=14)

        self.canvas = tk.Canvas(self.root,
                                width=500,
                                height=250,
                                bg="white")
        self.canvas.pack(pady=16)

    def create_footer(self):
        footer = tk.Label(
            self.root,
            text="© 2026 Knapsack Backtracking Visualizer | Developed by Harpreet Sandhu",
            bg="#101039",
            fg="white",
            font=("Times New Roman", 10, "bold"),
            pady=6
        )
        footer.pack(side=tk.BOTTOM, fill=tk.X)

    def knapsack_bt(self, i, current_weight,
                    current_profit, taken):

        if current_weight > self.capacity:
            return

        if current_profit > self.best_profit:
            self.best_profit = current_profit
            self.best_set = taken[:]

        if i == self.n:
            return

        taken[i] = 1
        self.knapsack_bt(
            i + 1,
            current_weight + self.weights[i],
            current_profit + self.values[i],
            taken
        )

        taken[i] = 0
        self.knapsack_bt(
            i + 1,
            current_weight,
            current_profit,
            taken
        )

    def draw_items(self):

        self.canvas.delete("all")
        x = 20
        for i in range(self.n):

            color = "green" if self.best_set[i] == 1 else "gray"

            self.canvas.create_rectangle(
                x, 80, x+60, 140,
                fill=color
            )

            self.canvas.create_text(
                x+30, 110,
                text=f"W:{self.weights[i]}\nV:{self.values[i]}",
                fill="white"
            )
            x += 70

    def solve(self):
        try:
            self.weights = list(map(int,
                               self.weight_entry.get().split(",")))
            self.values = list(map(int,
                               self.value_entry.get().split(",")))
            self.capacity = int(self.capacity_entry.get())

            if len(self.weights) != len(self.values):
                raise ValueError

            self.n = len(self.weights)
            self.best_profit = 0
            self.best_set = [0]*self.n

            taken = [0]*self.n

            self.knapsack_bt(0, 0, 0, taken)

            self.result_label.config(
                text=f"Maximum Profit = {self.best_profit}\n"
                     f"Selected Set = {self.best_set}"
            )
            self.draw_items()
        except:
            messagebox.showerror("Error", "Enter valid input!")
if __name__ == "__main__":
    root = tk.Tk()
    app = KnapsackBacktrackingGUI(root)
    root.mainloop()