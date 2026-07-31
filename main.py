import tkinter as tk
from sympy import *
x=symbols('x')
import matplotlib.pyplot as plt
import numpy as np
from sympy import lambdify

window = tk.Tk()
window.title(" Math Problem Solver ")
window.geometry("500x400")
window.configure(bg="#F8F5F2")

# Title
title = tk.Label(window, text=" Math Problem Solver ", font=("Segoe UI", 22, "bold"),
bg="#F8F5F2", fg="#1A1717")
title.pack(pady=20)

# Expression label
label = tk.Label(window, text="Enter Expression:", font=("Segoe UI", 12, "bold"),
bg="#C3C4C7")
label.pack(pady=10)

# Input box
entry = tk.Entry(window, width=40, font=("Segoe UI", 14))
entry.pack(pady=10)

main_frame = tk.Frame(window, bg="#E8F0FE")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)
left_frame = tk.LabelFrame(main_frame, text="", bd=2, relief="solid", bg="#E8F0FE")
left_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)
right_frame = tk.LabelFrame(main_frame, text="", bd=2, relief="solid", bg="#E8F0FE")
right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

current_answer = None

def differentiate():
    global current_answer
    try:
        expression = sympify(entry.get())
        if order_entry.get() == "":
            order = 1
        else:
            order = int(order_entry.get())
        result = diff(expression, x, order)
        current_answer = result
        result_label.config(text=str(result))

        explanation = "Differentiation\n\n"
        if order == 1:
            explanation += "• First order differentiation performed.\n"
        elif order == 2:
            explanation += "• Second order differentiation performed.\n"
        elif order == 3:
            explanation += "• Third order differentiation performed.\n"
        else:
            explanation += f"• {order} order differentiation performed.\n"
        if expression.is_polynomial():
            explanation += "Power Rule\n"
            explanation += "Formula: d(x^n)/dx = n*x^(n-1)\n\n"
        elif expression.is_Mul:
           explanation += "Product Rule (UV Rule)\n"
           explanation += "Formula:\n"
           explanation += "d(uv)/dx = u'v + uv'\n\n"
        elif expression.is_Pow and expression.base.func != Symbol:
            explanation += "Chain Rule\n"
            explanation += "Formula:\n"
            explanation += "d(f(g(x)))/dx = f'(g(x))*g'(x)\n\n"
        elif expression.is_rational_function():
            explanation += "Quotient Rule\n"
            explanation += "Formula:\n"
            explanation += "d(u/v)/dx = (u'v-uv')/v^2\n\n"
        if expression.has(sin):
            explanation += "• d/dx(sin(x)) = cos(x)\n"   
        if expression.has(cos):
            explanation += "• d/dx(cos(x)) = -sin(x)\n"  
        if expression.has(tan):
            explanation += "• d/dx(tan(x)) = sec²(x)\n" 
        if expression.has(sec):
            explanation += "• d/dx(sec(x)) = sec(x)tan(x)\n"
        if expression.has(csc):
            explanation += "• d/dx(csc(x)) = -csc(x)cot(x)\n"
        if expression.has(cot):
            explanation += "• d/dx(cot(x)) = -csc²(x)\n"  
        if expression.has(sqrt):
            explanation += "• d/dx(√x) = 1/(2√x)\n"
        if expression.has(asin):
            explanation += "• d/dx(sin⁻¹x) = 1/√(1-x²)\n"
        if expression.has(acos):
            explanation += "• d/dx(cos⁻¹x) = -1/√(1-x²)\n"
        if expression.has(atan):
            explanation += "• d/dx(tan⁻¹x) = 1/(1+x²)\n"
        if expression.has(log):
            explanation += "• d/dx(log(x)) = 1/x\n" 
        if expression.has(exp):
            explanation += "• d/dx(eˣ) = eˣ\n"
        explanation_label.config(text=explanation)
    except:
        result_label.config(text= "Invalid Expression")

def integrate_exp():
    global current_answer
    try:
        expression =sympify(entry.get())
        if lower_entry.get() == "" or upper_entry.get() == "":
            result = integrate(expression, x)
        else:
            lower = sympify(lower_entry.get())
            upper = sympify(upper_entry.get())
            result = integrate(expression, (x, lower,upper)) 
        result_label.config(text=str(result))
        current_answer = result

        explanation = "Integration\n\n"
        if explanation == "Integration\n\n":
            explanation += "• General integration performed.\n"
        if expression.is_polynomial():
            explanation += "• Power Rule for Integration.\n"
        if expression.has(sin):
            explanation += "• ∫sin(x) dx = -cos(x)\n" 
        if expression.has(cos):
            explanation += "• ∫cos(x) dx = sin(x)\n"
        if expression.has(tan):
            explanation += "• ∫tan(x) dx = -log(cos(x))\n"
        if expression.has(sec):
            explanation += "• ∫sec²(x) dx = tan(x)\n"
        if expression.has(csc):
            explanation += "• ∫csc²(x) dx = -cot(x)\n"
        if expression.has(cot):
            explanation += "• ∫cot(x) dx = log(sin(x))\n"
        if expression.has(sqrt):
            explanation += "• ∫√x dx = (2/3)x^(3/2)\n"
        if expression.has(exp):
            explanation += "• ∫eˣ dx = eˣ\n"
        if expression.has(log):
            explanation += "• Logarithmic function detected.\n"
        if expression.is_Mul:
            explanation += "• Integration by Parts applied.\n"
        if expression.is_rational_function():
            explanation += "• Logarithmic Integration Rule applied.\n"
        if expression.has(sin, cos, exp, log):
            explanation += "• Substitution Method applied.\n"
        if expression.has(asin):
            explanation += "• Inverse Sine Function detected.\n"
        if expression.has(acos):
            explanation += "• Inverse Cosine Function detected.\n"
        if expression.has(atan):
            explanation += "• Inverse Tangent Function detected.\n"    
        if lower_entry.get() != "" and upper_entry.get() != "":
            explanation += "• Definite integration performed using the given limits."
        explanation_label.config(text=explanation)
    except:
        result_label.config(text="Invalid Expression")

def show_graph():
    try:
        expression= sympify(entry.get())
        if current_answer is None:
            result_label.config(text="Calculate first")
            return
        
        f1 = lambdify(x, expression, "numpy")
        f2 = lambdify(x, current_answer, "numpy")
        x_values = np.linspace(-10, 10, 400)
        plt.figure(figsize=(6,4))
        plt.plot(x_values, f1(x_values), label=str(expression))
        plt.plot(x_values, f2(x_values), label=str(current_answer))
        plt.title("Graph")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()

    except:
        result_label.config(text="Invalid Expression")

def clear():
    global current_answer
    current_answer = None
    entry.delete(0,tk.END)
    order_entry.delete(0, tk.END)
    lower_entry.delete(0, tk.END) 
    upper_entry.delete(0, tk.END)
    result_label.config(text="Answer")
    explanation_label.config(text="")
    plt.close('all')

diff_frame = tk.Frame(left_frame)
diff_frame.pack(pady=5)
order_label = tk.Label(diff_frame,text = "Order")
order_label.pack()
order_entry = tk.Entry(diff_frame, width = 5)
order_entry.pack()

diff_button = tk.Button(diff_frame, text=" Differentiate", font=("Arial", 12, "bold"),
bg="#AC845B", width=20, command=differentiate)
diff_button.pack(pady=10)


limit_frame = tk.Frame(left_frame)
limit_frame.pack(pady=5)
lower_label = tk.Label(limit_frame,text = "Lower")
lower_label.pack(side = "left")
lower_entry = tk.Entry(limit_frame, width=5)
lower_entry.pack(side = "left", padx=10)
upper_label = tk.Label(limit_frame,text = "Upper")
upper_label.pack(side = "left")
upper_entry = tk.Entry(limit_frame, width=5)
upper_entry.pack(side = "left", padx=10)

int_button = tk.Button(left_frame, text=" Integrate", font=("Arial", 12, "bold"),
bg="#AC845B", width=20, command=integrate_exp)
int_button.pack(pady=10)

graph_button = tk.Button(left_frame, text= "Show Graph", font= ("Arial", 12, "bold"),
                         bg = "#AC845B", width=20, command = show_graph)
graph_button.pack(pady=10)

clear_button = tk.Button(left_frame,text="Clear",font=("Arial", 12, "bold"),command=clear)
clear_button.pack(pady=10)

# Result
result_label = tk.Label(right_frame, text="Answer:", font=("Arial", 14, "bold"),
bg="#A85454",fg= "black", width=40, height=2)
result_label.pack(pady=20)

explanation_title = tk.Label(right_frame, text="Explanation:", font=("Arial", 12, "bold"), bg="#C3C4C7")
explanation_title.pack(pady=(10,0))

explanation_label = tk.Label(right_frame, text="", font=("Arial", 11), justify="left", wraplength=450, anchor="w")
explanation_label.pack()

window.mainloop()