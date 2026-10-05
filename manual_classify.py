import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ============================================================
# LOAD DATA
# ============================================================

file = open("linear_1 .csv", "r")

x_values = []
y_values = []
colours = []

for line in file:
    data = line.strip().split(",")

    x_values.append(float(data[0]))
    y_values.append(float(data[1]))
    colours.append(data[2].strip())

file.close()


# ============================================================
# WINDOW
# ============================================================

window = tk.Tk()

window.title("LINEAR CLASSIFICATION LAB")
window.geometry("1250x850")
window.configure(bg="#0b0f17")


# ============================================================
# COLOURS
# ============================================================

BG = "#0b0f17"
PANEL = "#171d29"
INPUT = "#ffffff"

WHITE = "#ffffff"
GREY = "#8f9aaa"

YELLOW = "#ffd166"
GREEN = "#35e39a"
PURPLE = "#7067ff"


# ============================================================
# TITLE
# ============================================================

title = tk.Label(
    window,
    text="LINEAR CLASSIFICATION LAB",
    font=("Arial", 28, "bold"),
    fg=WHITE,
    bg=BG
)

title.pack(pady=(15, 0))


subtitle = tk.Label(
    window,
    text="FIND THE BEST LINE TO SEPARATE THE DATA",
    font=("Arial", 10, "bold"),
    fg=GREY,
    bg=BG
)

subtitle.pack(pady=(2, 10))


# ============================================================
# INPUT BAR
# ============================================================

input_bar = tk.Frame(
    window,
    bg=PANEL,
    height=95
)

input_bar.pack(
    fill="x",
    padx=20,
    pady=(0, 15)
)

input_bar.pack_propagate(False)


# -------------------------
# m
# -------------------------

tk.Label(
    input_bar,
    text="GRADIENT",
    font=("Arial", 9, "bold"),
    fg=GREY,
    bg=PANEL
).pack(
    side="left",
    padx=(25, 5)
)


m_entry = tk.Entry(
    input_bar,
    font=("Arial", 20, "bold"),
    fg="#111111",
    bg=INPUT,
    insertbackground="#111111",
    width=8,
    justify="center",
    relief="solid",
    bd=2
)

m_entry.pack(
    side="left",
    padx=5,
    ipady=8
)

m_entry.insert(0, "1")


# -------------------------
# c
# -------------------------

tk.Label(
    input_bar,
    text="Y-INTERCEPT",
    font=("Arial", 9, "bold"),
    fg=GREY,
    bg=PANEL
).pack(
    side="left",
    padx=(25, 5)
)


c_entry = tk.Entry(
    input_bar,
    font=("Arial", 20, "bold"),
    fg="#111111",
    bg=INPUT,
    insertbackground="#111111",
    width=8,
    justify="center",
    relief="solid",
    bd=2
)

c_entry.pack(
    side="left",
    padx=5,
    ipady=8
)

c_entry.insert(0, "0")


# -------------------------
# Equation
# -------------------------

equation = tk.Label(
    input_bar,
    text="y = 1x + 0",
    font=("Arial", 17, "bold"),
    fg=YELLOW,
    bg=PANEL
)

equation.pack(
    side="left",
    padx=30
)


# -------------------------
# CLASSIFY BUTTON
# -------------------------

def classify():

    try:
        m = float(m_entry.get())
        c = float(c_entry.get())

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter numbers for m and c."
        )

        return


    # ========================================================
    # CALCULATE SCORES
    # ========================================================

    score_1_correct = 0
    score_2_correct = 0

    for i in range(len(x_values)):

        line_y = m * x_values[i] + c

        if y_values[i] >= line_y:

            if colours[i] == "red":
                score_1_correct += 1

            if colours[i] == "blue":
                score_2_correct += 1

        else:

            if colours[i] == "blue":
                score_1_correct += 1

            if colours[i] == "red":
                score_2_correct += 1


    score_1 = score_1_correct / len(x_values) * 100
    score_2 = score_2_correct / len(x_values) * 100

    best_score = max(score_1, score_2)


    # ========================================================
    # UPDATE TEXT
    # ========================================================

    equation.config(
        text=f"y = {m:g}x + {c:g}"
    )

    score_label.config(
        text=f"{best_score:.1f}%"
    )


    if best_score >= 95:
        score_label.config(fg=GREEN)
        status_label.config(
            text="EXCELLENT CLASSIFICATION",
            fg=GREEN
        )

    elif best_score >= 85:
        score_label.config(fg=YELLOW)
        status_label.config(
            text="STRONG CLASSIFICATION",
            fg=YELLOW
        )

    elif best_score >= 70:
        score_label.config(fg=YELLOW)
        status_label.config(
            text="KEEP IMPROVING",
            fg=YELLOW
        )

    else:
        score_label.config(fg="#ff4d6d")
        status_label.config(
            text="TRY A DIFFERENT LINE",
            fg="#ff4d6d"
        )


    # ========================================================
    # REDRAW GRAPH
    # ========================================================

    ax.clear()

    ax.set_facecolor("#0d121b")

    ax.scatter(
        x_values,
        y_values,
        c=colours,
        s=65,
        edgecolors="white",
        linewidths=0.5
    )


    # Classification line

    x_line = [
        min(x_values) - 5,
        max(x_values) + 5
    ]

    y_line = [
        m * x_line[0] + c,
        m * x_line[1] + c
    ]

    ax.plot(
        x_line,
        y_line,
        color=YELLOW,
        linewidth=3
    )


    # Light classification regions

    ax.fill_between(
        x_line,
        y_line,
        max(y_values) + 30,
        color="#ff4d6d",
        alpha=0.05
    )

    ax.fill_between(
        x_line,
        y_line,
        min(y_values) - 30,
        color="#4da6ff",
        alpha=0.05
    )


    ax.set_title(
        f"CLASSIFICATION SCORE: {best_score:.1f}%",
        color=WHITE,
        fontsize=15,
        fontweight="bold"
    )

    ax.set_xlabel(
        "X VALUE",
        color=GREY
    )

    ax.set_ylabel(
        "Y VALUE",
        color=GREY
    )

    ax.tick_params(
        colors=GREY
    )

    for spine in ax.spines.values():
        spine.set_color("#303846")

    ax.grid(
        True,
        color="#303846",
        alpha=0.4
    )

    canvas.draw()


classify_button = tk.Button(
    input_bar,
    text="CLASSIFY",
    command=classify,
    font=("Arial", 13, "bold"),
    fg=WHITE,
    bg=PURPLE,
    activebackground="#918aff",
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    padx=25,
    pady=10
)

classify_button.pack(
    side="right",
    padx=25
)


# ============================================================
# MAIN CONTENT
# ============================================================

content = tk.Frame(
    window,
    bg=BG
)

content.pack(
    fill="both",
    expand=True,
    padx=20
)


# ============================================================
# GRAPH PANEL
# ============================================================

graph_panel = tk.Frame(
    content,
    bg=PANEL
)

graph_panel.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 15)
)


fig, ax = plt.subplots(
    figsize=(8, 6)
)

fig.patch.set_facecolor(PANEL)

ax.set_facecolor("#0d121b")

ax.scatter(
    x_values,
    y_values,
    c=colours,
    s=65,
    edgecolors="white",
    linewidths=0.5
)

ax.set_title(
    "DATASET",
    color=WHITE,
    fontsize=15,
    fontweight="bold"
)

ax.set_xlabel(
    "X VALUE",
    color=GREY
)

ax.set_ylabel(
    "Y VALUE",
    color=GREY
)

ax.tick_params(
    colors=GREY
)

for spine in ax.spines.values():
    spine.set_color("#303846")

ax.grid(
    True,
    color="#303846",
    alpha=0.4
)


canvas = FigureCanvasTkAgg(
    fig,
    master=graph_panel
)

canvas.draw()

canvas.get_tk_widget().pack(
    fill="both",
    expand=True,
    padx=15,
    pady=15
)


# ============================================================
# SCORE PANEL
# ============================================================

score_panel = tk.Frame(
    content,
    bg=PANEL,
    width=260
)

score_panel.pack(
    side="right",
    fill="y"
)

score_panel.pack_propagate(False)


tk.Label(
    score_panel,
    text="CLASSIFICATION",
    font=("Arial", 10, "bold"),
    fg=GREY,
    bg=PANEL
).pack(
    pady=(35, 5)
)


score_label = tk.Label(
    score_panel,
    text="--%",
    font=("Arial", 45, "bold"),
    fg=GREEN,
    bg=PANEL
)

score_label.pack()


status_label = tk.Label(
    score_panel,
    text="READY",
    font=("Arial", 10, "bold"),
    fg=GREY,
    bg=PANEL
)

status_label.pack(
    pady=5
)


tk.Label(
    score_panel,
    text=f"{len(x_values)} DATA POINTS",
    font=("Arial", 16, "bold"),
    fg=WHITE,
    bg=PANEL
).pack(
    pady=(35, 5)
)


tk.Label(
    score_panel,
    text=(
        "Enter your line above.\n\n"
        "m = gradient\n"
        "c = y-intercept\n\n"
        "The program checks every\n"
        "point and calculates the\n"
        "best possible classification\n"
        "score for your line."
    ),
    font=("Arial", 10),
    justify="center",
    fg=GREY,
    bg=PANEL
).pack(
    pady=20,
    padx=20
)


# ============================================================
# ENTER KEY
# ============================================================

window.bind(
    "<Return>",
    lambda event: classify()
)


# ============================================================
# AUTOMATICALLY SELECT m
# ============================================================

m_entry.focus()


# ============================================================
# START
# ============================================================

window.mainloop()