from tkinter import *
from tkinter import ttk, messagebox
import pulp
import numpy as np
import matplotlib.pyplot as plt
import re

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Massimizzazione costi")
        # self.geometry("500x500")
        self.resizable(0, 0)

        self.titleLabel = Label(self,
                                text="Massimizzazione GEP",
                                font=('sans serif', 18))
        self.titleLabel.pack()

        self.textField = Text(self, width=50, height=25, font=('sans serif', 12))
        self.textField.pack(pady=5)

        self.res = Label(self, font=('sans serif', 12))
        self.res.pack(pady=10)

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
        problems = str(self.textField.get("1.0", END))
        problems = problems.replace(" ", "").replace("z=", "")
        problems = [x for x in problems.split("\n") if x != ""]

        x = pulp.LpVariable("x", lowBound=0)
        y = pulp.LpVariable("y", lowBound=0)
        problem = pulp.LpProblem("Un semplice problema di max", pulp.LpMaximize)

        constraints = []  # Initialize constraints list

        try:
            for i in range(len(problems)):
                if i == 0:
                    problem += eval(problems[i]), "The objective function"
                else:
                    constraint = problems[i].replace("x", f"{x}").replace("y", f"{y}")
                    problem += eval(constraint), f"{i} constraint"
                    # Extract coefficients and constant from the constraint and add to the constraints list
                    coef_x, coef_y, constant = map(float, re.findall(r'[-+]?\d*\.\d+|\d+', constraint))
                    constraints.append((coef_x, coef_y, constant))

            problem.solve()

            s = ""
            for variable in problem.variables():
                s += f"{variable.name} = {variable.varValue}\n"

            self.res['text'] = f"{s}\n{pulp.value(problem.objective)}"

            # Extract optimal solution
            optimal_x = pulp.value(x)
            optimal_y = pulp.value(y)

            # Plot the feasible region
            x_values = np.linspace(0, 100, 100)
            y_values = [(j[2] - j[0] * x_values) / j[1] for j in constraints]

            for j in y_values:
                plt.plot(x_values, j, label=f"n")

            # Highlight the feasible region
            plt.fill_between(x_values, np.minimum.reduce([x for x in y_values]),
                             color='gray', alpha=0.5, label='Feasible Region')

            # Highlight the optimal solution
            plt.scatter([optimal_x], [optimal_y], color='red',
                        label='Optimal Solution')

            plt.xlabel("x")
            plt.ylabel("y")
            plt.title("Feasible Region and Optimal Solution")
            plt.legend()
            plt.grid(True)
            plt.xlim(0, 100)
            plt.ylim(0, 100)
            plt.show()
        except Exception as e:
            messagebox.showerror("Errore", e)

        # messagebox.showinfo("Risultato", f"{s}\n{pulp.value(problem.objective)}")

        # print(self.textField.get("1.0", END))
        # print(int(self.textField.index('end-1c').split('.')[0]))


if __name__ == "__main__":
    App().mainloop()
