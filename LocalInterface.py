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
                              command=self.quitBtn_clicked)
        self.quitBtn.pack(pady=5, ipadx=8, ipady=3)

    def submitBtn_clicked(self):
        problems = str(self.textField.get("1.0", END))
        problems = problems.replace(" ", "").replace("z=", "")
        problems = [x for x in problems.split("\n") if x != ""]

        x = pulp.LpVariable("x", lowBound=0)
        y = pulp.LpVariable("y", lowBound=0)
        problem = pulp.LpProblem("Un_semplice_problema_di_max", pulp.LpMaximize)

        constraints = []  # Initialize constraints list

        try:
            for i in range(len(problems)):
                if i == 0:
                    problem += eval(problems[i]), "The_objective_function"
                else:
                    constraint = problems[i].replace("x", f"{x}").replace("y", f"{y}")
                    problem += eval(constraint), f"{i}_constraint"
                    # Extract coefficients and constant from the constraint and add to the constraints list
                    coef_x, coef_y, constant = map(float, re.findall(r'[-+]?\d*\.\d+|\d+', constraint))
                    constraints.append((coef_x, coef_y, constant))

            solver = pulp.PULP_CBC_CMD()
            problem.solve(solver)

            s = ""
            for variable in problem.variables():
                s += f"{variable.name} = {variable.varValue}\n"

            self.res['text'] = f"{s}\nMassimale: {pulp.value(problem.objective)}"

            # Extract optimal solution
            optimal_x = pulp.value(x)
            optimal_y = pulp.value(y)

            # Plot the feasible region
            x_values = np.linspace(0, 100, 100)
            y_values = [(j[2] - j[0] * x_values) / j[1] for j in constraints]

            for j in range(1, len(problems)):
                plt.plot(x_values, y_values[j-1], label=f"{problems[j]}")

            # Highlight the feasible region
            plt.fill_between(x_values, np.minimum.reduce([x for x in y_values]),
                             color='gray', alpha=0.5, label='Feasible_Region')

            # Highlight the optimal solution
            plt.scatter([optimal_x], [optimal_y], color='red',
                        label=f'Massimale: {pulp.value(problem.objective)}')

            plt.xlabel("x")
            plt.ylabel("y")
            plt.title("Feasible_Region_and_Optimal_Solution")
            plt.legend()
            plt.grid(True)

            plt.xlim(0, 100)
            plt.ylim(0, 100)

            self.submitBtn.config(state=DISABLED)
            plt.connect('close_event', lambda event, btn=self.submitBtn: self.activate_submit_button(event, btn))
            plt.show()


        except Exception as e:
            messagebox.showerror("Errore", e)

        # messagebox.showinfo("Risultato", f"{s}\n{pulp.value(problem.objective)}")

        # print(self.textField.get("1.0", END))
        # print(int(self.textField.index('end-1c').split('.')[0]))

    def activate_submit_button(self, event, btn):
        # Activate submit button when the Matplotlib window is closed
        btn['state'] = NORMAL

    def quitBtn_clicked(self):
        plt.close() # Close the Matplotlib window
        self.destroy() # Close the tkinter application


if __name__ == "__main__":
    App().mainloop()
