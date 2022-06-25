from six.moves import tkinter as tk
class UI(tk.Frame):
    def __init__(self,parent = None):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Un titulo ")


if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("800x800")
    APP = UI(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()
