import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import random


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
# COLOURS
# ============================================================

BG = "#080b12"
PANEL = "#111722"
PANEL_2 = "#151c29"
GRAPH_BG = "#090e16"

WHITE = "#f5f7fb"
GREY = "#7f8a9d"
LIGHT_GREY = "#b7c0cf"

PURPLE = "#7567ff"
PURPLE_DARK = "#4d43bd"

CYAN = "#48d9ff"
GREEN = "#38e59b"
YELLOW = "#ffd166"
RED = "#ff4f70"
BLUE = "#4da6ff"

BORDER = "#252e3d"
GRID = "#202936"


# ============================================================
# WINDOW
# ============================================================

window = tk.Tk()

window.title("LINEAR CLASSIFICATION LAB")
window.geometry("1400x900")
window.minsize(1150, 750)
window.configure(bg=BG)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def rounded_frame(parent, bg=PANEL, width=None, height=None):
    frame = tk.Frame(
        parent,
        bg=bg,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    if width:
        frame.config(width=width)

    if height:
        frame.config(height=height)

    return frame


def make_label(parent, text, size=10, color=WHITE,
               weight="normal", bg=PANEL):

    return tk.Label(
        parent,
        text=text,
        font=("Arial", size, weight),
        fg=color,
        bg=bg
    )


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    window,
    bg=BG,
    height=95
)

header.pack(
    fill="x",
    padx=28,
    pady=(20, 5)
)

header.pack_propagate(False)


# Left side title

title_container = tk.Frame(
    header,
    bg=BG
)

title_container.pack(
    side="left",
    fill="y"
)


tk.Label(
    title_container,
    text="LINEAR",
    font=("Arial", 30, "bold"),
    fg=WHITE,
    bg=BG
).pack(
    side="left"
)

tk.Label(
    title_container,
    text=" CLASSIFICATION",
    font=("Arial", 30, "bold"),
    fg=PURPLE,
    bg=BG
).pack(
    side="left"
)


tk.Label(
    title_container,
    text="MANUAL DATA SEPARATION LAB",
    font=("Arial", 9, "bold"),
    fg=GREY,
    bg=BG
).pack(
    anchor="w",
    pady=(0, 0)
)


# Dataset badge

dataset_badge = tk.Frame(
    header,
    bg=PANEL,
    highlightbackground=BORDER,
    highlightthickness=1
)

dataset_badge.pack(
    side="right",
    pady=12
)

tk.Label(
    dataset_badge,
    text="●",
    font=("Arial", 12),
    fg=GREEN,
    bg=PANEL
).pack(
    side="left",
    padx=(12, 5)
)

tk.Label(
    dataset_badge,
    text=f"DATASET  •  {len(x_values)} POINTS",
    font=("Arial", 9, "bold"),
    fg=LIGHT_GREY,
    bg=PANEL
).pack(
    side="left",
    padx=(0, 12),
    pady=10
)


# ============================================================
# CONTROL BAR
# ============================================================

control_bar = rounded_frame(
    window,
    bg=PANEL,
    height=100
)

control_bar.pack(
    fill="x",
    padx=28,
    pady=(5, 15)
)

control_bar.pack_propagate(False)


# ---- Gradient ----

make_label(
    control_bar,
    "GRADIENT  m",
    9,
    GREY,
    "bold"
).pack(
    side="left",
    padx=(25, 8)
)


m_entry = tk.Entry(
    control_bar,
    font=("Arial", 18, "bold"),
    fg="#111111",
    bg="#f4f6fa",
    insertbackground="#111111",
    width=8,
    justify="center",
    relief="flat",
    bd=0
)

m_entry.pack(
    side="left",
    ipady=9
)

m_entry.insert(0, "1")


# ---- Plus sign ----

tk.Label(
    control_bar,
    text="+",
    font=("Arial", 20, "bold"),
    fg=GREY,
    bg=PANEL
).pack(
    side="left",
    padx=12
)


# ---- Intercept ----

make_label(
    control_bar,
    "Y-INTERCEPT  c",
    9,
    GREY,
    "bold"
).pack(
    side="left",
    padx=(0, 8)
)


c_entry = tk.Entry(
    control_bar,
    font=("Arial", 18, "bold"),
    fg="#111111",
    bg="#f4f6fa",
    insertbackground="#111111",
    width=8,
    justify="center",
    relief="flat",
    bd=0
)

c_entry.pack(
    side="left",
    ipady=9
)

c_entry.insert(0, "0")


# ---- Equation preview ----

equation_box = tk.Frame(
    control_bar,
    bg="#0d131d",
    highlightbackground="#303b4d",
    highlightthickness=1
)

equation_box.pack(
    side="left",
    padx=25,
    pady=18
)


tk.Label(
    equation_box,
    text="EQUATION",
    font=("Arial", 7, "bold"),
    fg=GREY,
    bg="#0d131d"
).pack(
    side="left",
    padx=(12, 5)
)


equation = tk.Label(
    equation_box,
    text="y = 1x + 0",
    font=("Arial", 15, "bold"),
    fg=YELLOW,
    bg="#0d131d"
)

equation.pack(
    side="left",
    padx=(0, 12),
    pady=9
)


# ============================================================
# CLASSIFICATION FUNCTION
# ============================================================

def classify():

    try:
        m = float(m_entry.get())
        c = float(c_entry.get())

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers for m and c."
        )

        return


    # ========================================================
    # CALCULATE CLASSIFICATION
    # ========================================================

    score_1_correct = 0
    score_2_correct = 0

    red_correct = 0
    blue_correct = 0

    red_total = colours.count("red")
    blue_total = colours.count("blue")

    for i in range(len(x_values)):

        line_y = m * x_values[i] + c

        if y_values[i] >= line_y:

            if colours[i] == "red":
                score_1_correct += 1
                red_correct += 1

            if colours[i] == "blue":
                score_2_correct += 1

        else:

            if colours[i] == "blue":
                score_1_correct += 1
                blue_correct += 1

            if colours[i] == "red":
                score_2_correct += 1


    score_1 = score_1_correct / len(x_values) * 100
    score_2 = score_2_correct / len(x_values) * 100

    best_score = max(score_1, score_2)

    correct_points = round(
        best_score / 100 * len(x_values)
    )

    incorrect_points = len(x_values) - correct_points


    # ========================================================
    # UPDATE EQUATION
    # ========================================================

    if c >= 0:
        equation_text = f"y = {m:g}x + {c:g}"
    else:
        equation_text = f"y = {m:g}x − {abs(c):g}"

    equation.config(
        text=equation_text
    )


    # ========================================================
    # SCORE COLOUR + STATUS
    # ========================================================

    if best_score >= 95:

        score_colour = GREEN
        status = "EXCELLENT CLASSIFICATION"

    elif best_score >= 85:

        score_colour = YELLOW
        status = "STRONG CLASSIFICATION"

    elif best_score >= 70:

        score_colour = YELLOW
        status = "KEEP IMPROVING"

    else:

        score_colour = RED
        status = "TRY A DIFFERENT LINE"


    score_label.config(
        text=f"{best_score:.1f}%",
        fg=score_colour
    )

    status_label.config(
        text=status,
        fg=score_colour
    )


    # ========================================================
    # UPDATE STATS
    # ========================================================

    correct_label.config(
        text=str(correct_points)
    )

    incorrect_label.config(
        text=str(incorrect_points)
    )

    red_label.config(
        text=f"{score_1:.1f}%"
    )

    blue_label.config(
        text=f"{score_2:.1f}%"
    )


    # ========================================================
    # REDRAW GRAPH
    # ========================================================

    ax.clear()

    ax.set_facecolor(GRAPH_BG)

    # --------------------------------------------------------
    # GRAPH RANGE
    # --------------------------------------------------------

    x_min = min(x_values) - 5
    x_max = max(x_values) + 5

    y_min = min(y_values) - 15
    y_max = max(y_values) + 15

    x_line = np.linspace(
        x_min,
        x_max,
        300
    )

    y_line = m * x_line + c


    # --------------------------------------------------------
    # CLASSIFICATION AREAS
    # --------------------------------------------------------

    ax.fill_between(
        x_line,
        y_line,
        y_max,
        color=RED,
        alpha=0.055
    )

    ax.fill_between(
        x_line,
        y_min,
        y_line,
        color=BLUE,
        alpha=0.055
    )


    # --------------------------------------------------------
    # DATA POINTS
    # --------------------------------------------------------

    ax.scatter(
        x_values,
        y_values,
        c=colours,
        s=80,
        edgecolors="#ffffff",
        linewidths=0.7,
        alpha=0.95,
        zorder=5
    )


    # --------------------------------------------------------
    # CLASSIFICATION LINE
    # --------------------------------------------------------

    ax.plot(
        x_line,
        y_line,
        color=YELLOW,
        linewidth=3.5,
        zorder=10
    )


    # Glow effect

    ax.plot(
        x_line,
        y_line,
        color=YELLOW,
        linewidth=9,
        alpha=0.08,
        zorder=9
    )


    # --------------------------------------------------------
    # GRAPH STYLING
    # --------------------------------------------------------

    ax.set_xlim(
        x_min,
        x_max
    )

    ax.set_ylim(
        y_min,
        y_max
    )

    ax.set_title(
        f"CLASSIFICATION SCORE   {best_score:.1f}%",
        color=WHITE,
        fontsize=15,
        fontweight="bold",
        pad=15
    )

    ax.set_xlabel(
        "X VALUE",
        color=GREY,
        fontsize=9,
        fontweight="bold"
    )

    ax.set_ylabel(
        "Y VALUE",
        color=GREY,
        fontsize=9,
        fontweight="bold"
    )

    ax.tick_params(
        colors=GREY,
        labelsize=8
    )

    for spine in ax.spines.values():
        spine.set_color(BORDER)

    ax.grid(
        True,
        color=GRID,
        linewidth=0.7,
        alpha=0.7
    )

    fig.tight_layout(
        pad=2
    )

    canvas.draw_idle()


# ============================================================
# CLASSIFY BUTTON
# ============================================================

def button_hover(event):
    classify_button.config(
        bg="#887cff"
    )


def button_leave(event):
    classify_button.config(
        bg=PURPLE
    )


classify_button = tk.Button(
    control_bar,
    text="CLASSIFY  →",
    command=classify,
    font=("Arial", 11, "bold"),
    fg=WHITE,
    bg=PURPLE,
    activebackground="#887cff",
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    padx=28,
    pady=12,
    bd=0
)

classify_button.pack(
    side="right",
    padx=22
)

classify_button.bind(
    "<Enter>",
    button_hover
)

classify_button.bind(
    "<Leave>",
    button_leave
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
    padx=28,
    pady=(0, 20)
)


# ============================================================
# GRAPH PANEL
# ============================================================

graph_panel = rounded_frame(
    content,
    bg=PANEL
)

graph_panel.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 15)
)


# Graph header

graph_header = tk.Frame(
    graph_panel,
    bg=PANEL,
    height=50
)

graph_header.pack(
    fill="x"
)

graph_header.pack_propagate(False)


tk.Label(
    graph_header,
    text="DATA VISUALISATION",
    font=("Arial", 10, "bold"),
    fg=WHITE,
    bg=PANEL
).pack(
    side="left",
    padx=18
)


tk.Label(
    graph_header,
    text="● LIVE",
    font=("Arial", 8, "bold"),
    fg=GREEN,
    bg=PANEL
).pack(
    side="right",
    padx=18
)


# ============================================================
# MATPLOTLIB
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 6)
)

fig.patch.set_facecolor(PANEL)

ax.set_facecolor(GRAPH_BG)


ax.scatter(
    x_values,
    y_values,
    c=colours,
    s=80,
    edgecolors="white",
    linewidths=0.7
)


ax.set_title(
    "DATASET",
    color=WHITE,
    fontsize=15,
    fontweight="bold",
    pad=15
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
    spine.set_color(BORDER)

ax.grid(
    True,
    color=GRID,
    alpha=0.7
)


canvas = FigureCanvasTkAgg(
    fig,
    master=graph_panel
)

canvas.draw()

canvas.get_tk_widget().pack(
    fill="both",
    expand=True,
    padx=12,
    pady=(0, 12)
)


# ============================================================
# RIGHT DASHBOARD
# ============================================================

dashboard = tk.Frame(
    content,
    bg=BG,
    width=300
)

dashboard.pack(
    side="right",
    fill="y"
)

dashboard.pack_propagate(False)


# ============================================================
# SCORE CARD
# ============================================================

score_panel = rounded_frame(
    dashboard,
    bg=PANEL,
    height=205
)

score_panel.pack(
    fill="x",
    pady=(0, 12)
)

score_panel.pack_propagate(False)


make_label(
    score_panel,
    "CLASSIFICATION SCORE",
    9,
    GREY,
    "bold"
).pack(
    pady=(20, 2)
)


score_label = tk.Label(
    score_panel,
    text="--%",
    font=("Arial", 43, "bold"),
    fg=GREEN,
    bg=PANEL
)

score_label.pack()


status_label = tk.Label(
    score_panel,
    text="READY",
    font=("Arial", 9, "bold"),
    fg=GREY,
    bg=PANEL
)

status_label.pack(
    pady=(0, 12)
)


# ============================================================
# POINT STATISTICS
# ============================================================

stats_panel = rounded_frame(
    dashboard,
    bg=PANEL,
    height=155
)

stats_panel.pack(
    fill="x",
    pady=(0, 12)
)

stats_panel.pack_propagate(False)


make_label(
    stats_panel,
    "POINT ANALYSIS",
    9,
    GREY,
    "bold"
).pack(
    anchor="w",
    padx=18,
    pady=(15, 8)
)


stats_row = tk.Frame(
    stats_panel,
    bg=PANEL
)

stats_row.pack(
    fill="x",
    padx=12
)


# Correct

correct_box = tk.Frame(
    stats_row,
    bg="#0d1916"
)

correct_box.pack(
    side="left",
    fill="both",
    expand=True,
    padx=4
)

tk.Label(
    correct_box,
    text="CORRECT",
    font=("Arial", 8, "bold"),
    fg=GREEN,
    bg="#0d1916"
).pack(
    pady=(10, 2)
)

correct_label = tk.Label(
    correct_box,
    text="--",
    font=("Arial", 20, "bold"),
    fg=WHITE,
    bg="#0d1916"
)

correct_label.pack(
    pady=(0, 8)
)


# Incorrect

incorrect_box = tk.Frame(
    stats_row,
    bg="#1b1116"
)

incorrect_box.pack(
    side="left",
    fill="both",
    expand=True,
    padx=4
)

tk.Label(
    incorrect_box,
    text="INCORRECT",
    font=("Arial", 8, "bold"),
    fg=RED,
    bg="#1b1116"
).pack(
    pady=(10, 2)
)

incorrect_label = tk.Label(
    incorrect_box,
    text="--",
    font=("Arial", 20, "bold"),
    fg=WHITE,
    bg="#1b1116"
)

incorrect_label.pack(
    pady=(0, 8)
)


# ============================================================
# CLASS BALANCE
# ============================================================

balance_panel = rounded_frame(
    dashboard,
    bg=PANEL,
    height=145
)

balance_panel.pack(
    fill="x",
    pady=(0, 12)
)

balance_panel.pack_propagate(False)


make_label(
    balance_panel,
    "CLASS PERFORMANCE",
    9,
    GREY,
    "bold"
).pack(
    anchor="w",
    padx=18,
    pady=(15, 7)
)


red_row = tk.Frame(
    balance_panel,
    bg=PANEL
)

red_row.pack(
    fill="x",
    padx=18
)


tk.Label(
    red_row,
    text="RED",
    font=("Arial", 9, "bold"),
    fg=RED,
    bg=PANEL
).pack(
    side="left"
)


red_label = tk.Label(
    red_row,
    text="--%",
    font=("Arial", 9, "bold"),
    fg=WHITE,
    bg=PANEL
)

red_label.pack(
    side="right"
)


blue_row = tk.Frame(
    balance_panel,
    bg=PANEL
)

blue_row.pack(
    fill="x",
    padx=18,
    pady=(7, 0)
)


tk.Label(
    blue_row,
    text="BLUE",
    font=("Arial", 9, "bold"),
    fg=BLUE,
    bg=PANEL
).pack(
    side="left"
)


blue_label = tk.Label(
    blue_row,
    text="--%",
    font=("Arial", 9, "bold"),
    fg=WHITE,
    bg=PANEL
)

blue_label.pack(
    side="right"
)


# ============================================================
# INSTRUCTIONS
# ============================================================

info_panel = rounded_frame(
    dashboard,
    bg=PANEL,
    height=220
)

info_panel.pack(
    fill="both",
    expand=True
)

make_label(
    info_panel,
    "HOW TO PLAY",
    9,
    GREY,
    "bold"
).pack(
    anchor="w",
    padx=18,
    pady=(18, 8)
)


instructions = (
    "1. Choose a gradient (m)\n\n"
    "2. Choose a y-intercept (c)\n\n"
    "3. Your line becomes  y = mx + c\n\n"
    "4. Click CLASSIFY\n\n"
    "5. Try to maximise your score\n\n"
    "TIP\n"
    "A perfect classifier scores 100%."
)


tk.Label(
    info_panel,
    text=instructions,
    font=("Arial", 9),
    justify="left",
    anchor="nw",
    fg=LIGHT_GREY,
    bg=PANEL
).pack(
    fill="both",
    expand=True,
    padx=18,
    pady=(0, 15)
)


# ============================================================
# KEYBOARD SHORTCUT
# ============================================================

window.bind(
    "<Return>",
    lambda event: classify()
)


# ============================================================
# LIVE EQUATION PREVIEW
# ============================================================

def update_equation(event=None):

    try:

        m = float(m_entry.get())
        c = float(c_entry.get())

        if c >= 0:
            text = f"y = {m:g}x + {c:g}"
        else:
            text = f"y = {m:g}x − {abs(c):g}"

        equation.config(
            text=text
        )

    except:

        equation.config(
            text="y = ?"
        )


m_entry.bind(
    "<KeyRelease>",
    update_equation
)

c_entry.bind(
    "<KeyRelease>",
    update_equation
)


# ============================================================
# STARTUP
# ============================================================

m_entry.focus()

window.mainloop()