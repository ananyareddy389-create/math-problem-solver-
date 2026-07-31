# Math Problem Solver

## Overview

Math Problem Solver is a desktop application developed using Python that performs symbolic calculus operations through a graphical user interface (GUI). The application enables users to differentiate and integrate mathematical expressions, visualize graphs, and understand the mathematical rules applied during computation.

The project combines symbolic mathematics with an interactive interface, making calculus operations simple and easy to understand.

---

## Features

### Differentiation
- Performs first-order and higher-order differentiation.
- Supports polynomial, trigonometric, logarithmic, exponential, square root, and inverse trigonometric functions.
- Identifies and explains differentiation rules, including:
  - Power Rule
  - Product Rule
  - Quotient Rule
  - Chain Rule

### Integration
- Performs indefinite integration.
- Performs definite integration using user-defined lower and upper limits.
- Supports polynomial, trigonometric, logarithmic, exponential, square root, and inverse trigonometric functions.
- Displays the integration method or rule used whenever applicable.

### Graph Visualization
- Plots the original mathematical expression.
- Plots the differentiated or integrated result on the same graph.
- Displays graph title, axis labels, legend, and grid for better visualization.

### User Interface
- Clean and interactive GUI built using Tkinter.
- Simple input fields and operation buttons.
- Separate sections for results and explanations.
- Clear button to reset all inputs and outputs.

---

## Libraries Used

- **Tkinter** – Used to create the graphical user interface (GUI).
- **SymPy** – Used for symbolic mathematical operations such as differentiation and integration.
- **NumPy** – Used to generate numerical values for graph plotting.
- **Matplotlib** – Used to visualize mathematical functions using graphs.

---

## Project Structure

```text
Math-Problem-Solver/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## How to Use

1. Enter a mathematical expression.
2. Click **Differentiate** or **Integrate**.
3. For differentiation, optionally enter the order of differentiation.
4. For definite integration, enter the lower and upper limits.
5. View the calculated result, explanation of the mathematical rule used, and the graph comparing the original function with the computed result.

---

## Example

**Input**

```text
sin(x)
```

**Differentiation Result**

```text
cos(x)
```

**Integration Result**

```text
-cos(x)
```

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Python programming
- GUI development using Tkinter
- Symbolic mathematics using SymPy
- Graph plotting using Matplotlib
- Numerical computation using NumPy
- Event-driven programming
- Exception handling
- Integrating multiple Python libraries into a single application

---

## Future Improvements

- Support shorthand mathematical expressions such as `sinx` and `cosx`.
- Add limit calculations.
- Display detailed step-by-step symbolic solutions.
- Save calculation history.
- Export results to a file.
- Improve the user interface with additional customization options.

---

## Author

**Ananya Reddy**

B.Tech – Information Technology