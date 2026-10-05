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

window.title("LINEAR CLASSIFICATION — RANDOM SEARCH")
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


# Title

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
    text="AUTOMATED RANDOM SEARCH LAB",
    font=("Arial", 9, "bold"),
    fg=GREY,
    bg=BG
).pack(
    anchor="w"
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


# ---- Number of trials ----

make_label(
    control_bar,
    "NUMBER OF TRIALS",
    9,
    GREY,
    "bold"
).pack(
    side="left",
    padx=(25, 8)
)


trials_entry = tk.Entry(
    control_bar,
    font=("Arial", 18, "bold"),
    fg="#111111",
    bg="#f4f6fa",
    insertbackground="#111111",
    width=9,
    justify="center",
    relief="flat",
    bd=0
)

trials_entry.pack(
    side="left",
    ipady=9
)

trials_entry.insert(0, "1000")


# ---- Search range ----

range_box = tk.Frame(
    control_bar,
    bg="#0d131d",
    highlightbackground="#303b4d",
    highlightthickness=1
)

range_box.pack(
    side="left",
    padx=25,
    pady=18
)


tk.Label(
    range_box,
    text="RANDOM RANGE",
    font=("Arial", 7, "bold"),
    fg=GREY,
    bg="#0d131d"
).pack(
    side="left",
    padx=(12, 5)
)

tk.Label(
    range_box,
    text="m: −5 → 5     c: −100 → 100",
    font=("Arial", 11, "bold"),
    fg=CYAN,
    bg="#0d131d"
).pack(
    side="left",
    padx=(0, 12),
    pady=9
)


# ---- Search button ----

def button_hover(event):

    search_button.config(
        bg="#887cff"
    )


def button_leave(event):

    search_button.config(
        bg=PURPLE
    )


search_button = tk.Button(
    control_bar,
    text="RUN RANDOM SEARCH  →",
    command=run_search if "run_search" in globals() else None,
    font=("Arial", 11, "bold"),
    fg=WHITE,
    bg=PURPLE,
    activebackground="#887cff",
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    padx=25,
    pady=12,
    bd=0
)

search_button.pack(
    side="right",
    padx=22
)

search_button.bind(
    "<Enter>",
    button_hover
)

search_button.bind(
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


live_label = tk.Label(
    graph_header,
    text="● READY",
    font=("Arial", 8, "bold"),
    fg=GREEN,
    bg=PANEL
)

live_label.pack(
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
    "DATASET — READY FOR SEARCH",
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
# BEST SCORE CARD
# ============================================================

score_panel = rounded_frame(
    dashboard,
    bg=PANEL,
    height=190
)

score_panel.pack(
    fill="x",
    pady=(0, 12)
)

score_panel.pack_propagate(False)


make_label(
    score_panel,
    "BEST CLASSIFICATION SCORE",
    9,
    GREY,
    "bold"
).pack(
    pady=(18, 2)
)


score_label = tk.Label(
    score_panel,
    text="--%",
    font=("Arial", 42, "bold"),
    fg=GREEN,
    bg=PANEL
)

score_label.pack()


status_label = tk.Label(
    score_panel,
    text="WAITING FOR SEARCH",
    font=("Arial", 9, "bold"),
    fg=GREY,
    bg=PANEL
)

status_label.pack(
    pady=(0, 10)
)


# ============================================================
# BEST LINE
# ============================================================

line_panel = rounded_frame(
    dashboard,
    bg=PANEL,
    height=150
)

line_panel.pack(
    fill="x",
    pady=(0, 12)
)

line_panel.pack_propagate(False)


make_label(
    line_panel,
    "BEST LINE FOUND",
    9,
    GREY,
    "bold"
).pack(
    pady=(15, 5)
)


equation = tk.Label(
    line_panel,
    text="y = ?",
    font=("Arial", 18, "bold"),
    fg=YELLOW,
    bg=PANEL
)

equation.pack(
    pady=3
)


m_result = tk.Label(
    line_panel,
    text="m = --",
    font=("Arial", 9, "bold"),
    fg=LIGHT_GREY,
    bg=PANEL
)

m_result.pack(
    pady=(5, 0)
)


c_result = tk.Label(
    line_panel,
    text="c = --",
    font=("Arial", 9, "bold"),
    fg=LIGHT_GREY,
    bg=PANEL
)

c_result.pack()


# ============================================================
# SEARCH STATISTICS
# ============================================================

stats_panel = rounded_frame(
    dashboard,
    bg=PANEL,
    height=175
)

stats_panel.pack(
    fill="x",
    pady=(0, 12)
)

stats_panel.pack_propagate(False)


make_label(
    stats_panel,
    "SEARCH STATISTICS",
    9,
    GREY,
    "bold"
).pack(
    anchor="w",
    padx=18,
    pady=(15, 8)
)


# Trials

trials_row = tk.Frame(
    stats_panel,
    bg=PANEL
)

trials_row.pack(
    fill="x",
    padx=18,
    pady=3
)


tk.Label(
    trials_row,
    text="TRIALS TESTED",
    font=("Arial", 9, "bold"),
    fg=GREY,
    bg=PANEL
).pack(
    side="left"
)


trials_result = tk.Label(
    trials_row,
    text="--",
    font=("Arial", 10, "bold"),
    fg=WHITE,
    bg=PANEL
)

trials_result.pack(
    side="right"
)


# Correct

correct_row = tk.Frame(
    stats_panel,
    bg=PANEL
)

correct_row.pack(
    fill="x",
    padx=18,
    pady=3
)


tk.Label(
    correct_row,
    text="CORRECT POINTS",
    font=("Arial", 9, "bold"),
    fg=GREEN,
    bg=PANEL
).pack(
    side="left"
)


correct_label = tk.Label(
    correct_row,
    text="--",
    font=("Arial", 10, "bold"),
    fg=WHITE,
    bg=PANEL
)

correct_label.pack(
    side="right"
)


# Incorrect

incorrect_row = tk.Frame(
    stats_panel,
    bg=PANEL
)

incorrect_row.pack(
    fill="x",
    padx=18,
    pady=3
)


tk.Label(
    incorrect_row,
    text="INCORRECT POINTS",
    font=("Arial", 9, "bold"),
    fg=RED,
    bg=PANEL
).pack(
    side="left"
)


incorrect_label = tk.Label(
    incorrect_row,
    text="--",
    font=("Arial", 10, "bold"),
    fg=WHITE,
    bg=PANEL
)

incorrect_label.pack(
    side="right"
)


# ============================================================
# SEARCH PROGRESS
# ============================================================

progress_panel = rounded_frame(
    dashboard,
    bg=PANEL,
    height=100
)

progress_panel.pack(
    fill="x",
    pady=(0, 12)
)

progress_panel.pack_propagate(False)


make_label(
    progress_panel,
    "SEARCH PROGRESS",
    9,
    GREY,
    "bold"
).pack(
    anchor="w",
    padx=18,
    pady=(13, 6)
)


progress_bar = tk.Frame(
    progress_panel,
    bg="#202936",
    height=8
)

progress_bar.pack(
    fill="x",
    padx=18
)

progress_bar.pack_propagate(False)


progress_fill = tk.Frame(
    progress_bar,
    bg=PURPLE,
    height=8,
    width=0
)

progress_fill.place(
    x=0,
    y=0,
    relheight=1
)


progress_text = tk.Label(
    progress_panel,
    text="0%",
    font=("Arial", 8, "bold"),
    fg=LIGHT_GREY,
    bg=PANEL
)

progress_text.pack(
    pady=(6, 0)
)


# ============================================================
# INSTRUCTIONS
# ============================================================

info_panel = rounded_frame(
    dashboard,
    bg=PANEL,
    height=200
)

info_panel.pack(
    fill="both",
    expand=True
)


make_label(
    info_panel,
    "HOW RANDOM SEARCH WORKS",
    9,
    GREY,
    "bold"
).pack(
    anchor="w",
    padx=18,
    pady=(17, 8)
)


instructions = (
    "1. Choose the number of trials\n\n"
    "2. Python randomly selects m and c\n\n"
    "3. The line is scored against the data\n\n"
    "4. The best result is saved\n\n"
    "5. Repeat until all trials are complete\n\n"
    "The final line is the best one found."
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
# RANDOM SEARCH FUNCTION
# ============================================================

def run_search():

    try:

        trials = int(trials_entry.get())

        if trials <= 0:
            raise ValueError

    except ValueError:

        messagebox.showerror(
            "Invalid Number",
            "Please enter a positive whole number of trials."
        )

        return


    # Disable button while searching

    search_button.config(
        state="disabled",
        text="SEARCHING..."
    )

    live_label.config(
        text="● SEARCHING",
        fg=YELLOW
    )

    window.update()


    # ========================================================
    # BEST RESULT VARIABLES
    # ========================================================

    best_score = -1
    best_m = 0
    best_c = 0


    # ========================================================
    # RANDOM SEARCH
    # ========================================================

    for trial in range(trials):

        # Randomly generate m and c

        m = random.uniform(-5, 5)

        c = random.uniform(-100, 100)


        # Calculate both possible classifications

        score_1_correct = 0
        score_2_correct = 0


        for i in range(len(x_values)):

            line_y = m * x_values[i] + c


            # Point is above the line

            if y_values[i] >= line_y:

                # Score 1: red above, blue below

                if colours[i] == "red":
                    score_1_correct += 1

                # Score 2: blue above, red below

                if colours[i] == "blue":
                    score_2_correct += 1


            # Point is below the line

            else:

                # Score 1: blue below

                if colours[i] == "blue":
                    score_1_correct += 1

                # Score 2: red below

                if colours[i] == "red":
                    score_2_correct += 1


        # Convert to percentages

        score_1 = (
            score_1_correct /
            len(x_values)
            * 100
        )

        score_2 = (
            score_2_correct /
            len(x_values)
            * 100
        )


        trial_score = max(
            score_1,
            score_2
        )


        # ====================================================
        # KEEP ONLY THE BEST RESULT
        # ====================================================

        if trial_score > best_score:

            best_score = trial_score
            best_m = m
            best_c = c


        # ====================================================
        # UPDATE PROGRESS
        # ====================================================

        if trial % max(1, trials // 100) == 0:

            percentage = (
                trial /
                trials
                * 100
            )

            progress_text.config(
                text=f"{percentage:.0f}%"
            )

            progress_fill.place(
                relwidth=percentage / 100
            )

            window.update()


    # ========================================================
    # FINAL PROGRESS
    # ========================================================

    progress_fill.place(
        relwidth=1
    )

    progress_text.config(
        text="100%"
    )


    # ========================================================
    # FINAL RESULTS
    # ========================================================

    correct_points = round(
        best_score /
        100 *
        len(x_values)
    )

    incorrect_points = (
        len(x_values) -
        correct_points
    )


    # ========================================================
    # EQUATION
    # ========================================================

    if best_c >= 0:

        equation_text = (
            f"y = {best_m:.3f}x + {best_c:.3f}"
        )

    else:

        equation_text = (
            f"y = {best_m:.3f}x − {abs(best_c):.3f}"
        )


    equation.config(
        text=equation_text
    )

    m_result.config(
        text=f"m = {best_m:.6f}"
    )

    c_result.config(
        text=f"c = {best_c:.6f}"
    )


    # ========================================================
    # SCORE
    # ========================================================

    if best_score >= 95:

        score_colour = GREEN
        status = "EXCELLENT CLASSIFICATION"

    elif best_score >= 85:

        score_colour = YELLOW
        status = "STRONG CLASSIFICATION"

    elif best_score >= 70:

        score_colour = YELLOW
        status = "KEEP SEARCHING"

    else:

        score_colour = RED
        status = "LOW CLASSIFICATION"


    score_label.config(
        text=f"{best_score:.1f}%",
        fg=score_colour
    )

    status_label.config(
        text=status,
        fg=score_colour
    )


    # ========================================================
    # STATISTICS
    # ========================================================

    trials_result.config(
        text=f"{trials:,}"
    )

    correct_label.config(
        text=str(correct_points)
    )

    incorrect_label.config(
        text=str(incorrect_points)
    )


    # ========================================================
    # DRAW FINAL GRAPH
    # ========================================================

    ax.clear()

    ax.set_facecolor(GRAPH_BG)


    # Graph range

    x_min = min(x_values) - 5
    x_max = max(x_values) + 5

    y_min = min(y_values) - 15
    y_max = max(y_values) + 15


    x_line = np.linspace(
        x_min,
        x_max,
        300
    )

    y_line = (
        best_m *
        x_line +
        best_c
    )


    # Classification areas

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


    # Data points

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


    # Glow

    ax.plot(
        x_line,
        y_line,
        color=YELLOW,
        linewidth=10,
        alpha=0.08,
        zorder=9
    )


    # Best line

    ax.plot(
        x_line,
        y_line,
        color=YELLOW,
        linewidth=3.5,
        zorder=10
    )


    # Styling

    ax.set_xlim(
        x_min,
        x_max
    )

    ax.set_ylim(
        y_min,
        y_max
    )

    ax.set_title(
        f"BEST RANDOM CLASSIFIER   {best_score:.1f}%",
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

        spine.set_color(
            BORDER
        )


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


    # ========================================================
    # FINISHED
    # ========================================================

    live_label.config(
        text="● COMPLETE",
        fg=GREEN
    )

    search_button.config(
        state="normal",
        text="RUN RANDOM SEARCH  →"
    )


# ============================================================
# CONNECT BUTTON TO FUNCTION
# ============================================================

search_button.config(
    command=run_search
)


# ============================================================
# KEYBOARD SHORTCUT
# ============================================================

window.bind(
    "<Return>",
    lambda event: run_search()
)


# ============================================================
# STARTUP
# ============================================================

trials_entry.focus()

window.mainloop()