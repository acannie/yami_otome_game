import tkinter as tk

class Main(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        master.geometry("300x300")
        master.title("雛形")


def main():
    win = tk.Tk()
    app = Main(master=win)
    app.mainloop()


if __name__ == "__main__":
    main()
