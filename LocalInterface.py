from tkinter import *
from tkinter import ttk, messagebox

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Massimizzazione costi")
        #self.geometry("500x500")
        self.resizable(0,0)

        self.titleLabel = Label(self,
                                text="Massimizzazione GEP",
                                font=('sans serif', 18))
        self.titleLabel.pack()

        self.textField = Text(self, width=50, height=25, font=('sans serif', 12))
        self.textField.pack(pady=5)

        self.submitBtn = Button(self,
                                text="Calcola",
                                font=('sans serif', 12),
                                bg='red',
                                fg='white',
                                command=self.submitBtn_clicked)
        self.submitBtn.pack(pady=10, ipadx=10, ipady=5)

        self.quitBtn = Button(self,
                              text='Quit',
                              font=('sans serif', 12),
                              bg='green',
                              fg='white',
                              command=self.destroy)
        self.quitBtn.pack(pady=5, ipadx=8, ipady=3)

    def submitBtn_clicked(self):
        print(self.textField.get("1.0", END))
        print(int(self.textField.index('end-1c').split('.')[0]))

if __name__ == "__main__":
    App().mainloop()