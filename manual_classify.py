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
window.title("LINEAR CLASSIFICATION // AI TRAINING LAB")
window.geometry("1200x800")
window.configure(bg="#10131a")


# ============================================================
# COLOURS
# ============================================================

BACKGROUND = "#10131a"
PANEL = "#181d27"
PANEL2 = "#202632"
TEXT = "#f2f5f7"
MUTED = "#8d98a8"

RED = "#ff4d6d"
BLUE = "#4da6ff"
GREEN = "#35e39a"
YELLOW = "#ffd166"
PURPLE = "#a970ff"


# ============================================================
# TITLE
# ============================================================

title = tk.Label(
    window,
    text="LINEAR CLASSIFICATION",
    font=("Arial", 26, "bold"),
    fg=TEXT,
    bg=BACKGROUND
)

title.pack(pady=(20, 0))

subtitle = tk.Label(
    window,
    text="MANUAL CLASSIFICATION // FIND THE BEST SEPARATING LINE",
    font=("Arial", 10, "bold"),
    fg=MUTED,
    bg=BACKGROUND
)

subtitle.pack(pady=(2, 15))


# ============================================================
# MAIN AREA
# ============================================================

main = tk.Frame(window, bg=BACKGROUND)
main.pack(fill="both", expand=True, padx=20, pady=5)


# ============================================================
# GRAPH PANEL
# ============================================================

graph_panel = tk.Frame(
    main,
    bg=PANEL,
    highlightbackground="#303846",
    highlightthickness=1
)

graph_panel.pack(side="left", fill="both", expand=True, padx=(0, 10))


# Create graph
fig, ax = plt.subplots(figsize=(7, 6))

fig.patch.set_facecolor(PANEL)
ax.set_facecolor("#11151d")

ax.scatter(
    x_values,
    y_values,
    c=colours,
    s=60,
    edgecolors="white",
    linewidths=0.5
)

ax.set_title(
    "DATASET",
    color=TEXT,
    fontsize=14,
    fontweight="bold"
)

ax.set_xlabel("X VALUE", color=MUTED)
ax.set_ylabel("Y VALUE", color=MUTED)

ax.tick_params(colors=MUTED)

for spine in ax.spines.values():
    spine.set_color("#303846")

ax.grid(
    True,
    color="#303846",
    alpha=0.4
)

canvas = FigureCanvasTkAgg(fig, master=graph_panel)
canvas.draw()
canvas.get_tk_widget().pack(
    fill="both",
    expand=True,
    padx=15,
    pady=15
)


# ============================================================
# CONTROL PANEL
# ============================================================

control_panel = tk.Frame(
    main,
    bg=PANEL,
    width=320,
    highlightbackground="#303846",
    highlightthickness=1
)

control_panel.pack(side="right", fill="y")
control_panel.pack_propagate(False)


# ============================================================
# DATASET CARD
# ============================================================

dataset_title = tk.Label(
    control_panel,
    text="DATASET",
    font=("Arial", 10, "bold"),
    fg=MUTED,
    bg=PANEL
)

dataset_title.pack(anchor="w", padx=20, pady=(20, 3))


dataset_label = tk.Label(
    control_panel,
    text=f"{len(x_values)} DATA POINTS",
    font=("Arial", 22, "bold"),
    fg=TEXT,
    bg=PANEL
)

dataset_label.pack(anchor="w", padx=20)


# ============================================================
# SCORE
# ============================================================

score_title = tk.Label(
    control_panel,
    text="CLASSIFICATION SCORE",
    font=("Arial", 10, "bold"),
    fg=MUTED,
    bg=PANEL
)

score_title.pack(anchor="w", padx=20, pady=(25, 3))


score_label = tk.Label(
    control_panel,
    text="-- %",
    font=("Arial", 42, "bold"),
    fg=GREEN,
    bg=PANEL
)

score_label.pack(anchor="w", padx=20)


status_label = tk.Label(
    control_panel,
    text="ENTER A LINE TO BEGIN",
    font=("Arial", 9, "bold"),
    fg=MUTED,
    bg=PANEL
)

status_label.pack(anchor="w", padx=20, pady=(0, 20))


# ============================================================
# INPUT AREA
# ============================================================

line_title = tk.Label(
    control_panel,
    text="YOUR LINE",
    font=("Arial", 10, "bold"),
    fg=MUTED,
    bg=PANEL
)

line_title.pack(anchor="w", padx=20, pady=(5, 10))


# Gradient
m_frame = tk.Frame(control_panel, bg=PANEL)
m_frame.pack(fill="x", padx=20)

m_label = tk.Label(
    m_frame,
    text="GRADIENT (m)",
    font=("Arial", 10, "bold"),
    fg=TEXT,
    bg=PANEL
)

m_label.pack(side="left")


m_entry = tk.Entry(
    m_frame,
    font=("Arial", 14, "bold"),
    bg=PANEL2,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat"
)

m_entry.pack(side="right", ipadx=8, ipady=6)


# Y intercept
c_frame = tk.Frame(control_panel, bg=PANEL)
c_frame.pack(fill="x", padx=20, pady=12)

c_label = tk.Label(
    c_frame,
    text="Y-INTERCEPT (c)",
    font=("Arial", 10, "bold"),
    fg=TEXT,
    bg=PANEL
)

c_label.pack(side="left")


c_entry = tk.Entry(
    c_frame,
    font=("Arial", 14, "bold"),
    bg=PANEL2,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat"
)

c_entry.pack(side="right", ipadx=8, ipady=6)


# ============================================================
# EQUATION DISPLAY
# ============================================================

equation_label = tk.Label(
    control_panel,
    text="y = mx + c",
    font=("Arial", 16, "bold"),
    fg=YELLOW,
    bg=PANEL
)

equation_label.pack(pady=15)


# ============================================================
# CLASSIFY FUNCTION
# ============================================================

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


    # --------------------------------------------------------
    # Calculate scores
    # --------------------------------------------------------

    score_1_correct = 0
    score_2_correct = 0

    for i in range(len(x_values)):

        line_y = m * x_values[i] + c

        if y_values[i] >= line_y:

            # Red above
            if colours[i] == "red":
                score_1_correct += 1

            # Blue above
            if colours[i] == "blue":
                score_2_correct += 1

        else:

            # Blue below
            if colours[i] == "blue":
                score_1_correct += 1

            # Red below
            if colours[i] == "red":
                score_2_correct += 1


    score_1 = score_1_correct / len(x_values) * 100
    score_2 = score_2_correct / len(x_values) * 100

    best_score = max(score_1, score_2)


    # --------------------------------------------------------
    # Update interface
    # --------------------------------------------------------

    score_label.config(
        text=f"{best_score:.1f}%"
    )

    equation_label.config(
        text=f"y = {m:g}x + {c:g}"
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
            text="DECENT — KEEP OPTIMISING",
            fg=YELLOW
        )

    else:

        score_label.config(fg=RED)

        status_label.config(
            text="POOR SEPARATION — TRY AGAIN",
            fg=RED
        )


    # --------------------------------------------------------
    # Redraw graph
    # --------------------------------------------------------

    ax.clear()

    ax.set_facecolor("#11151d")

    ax.scatter(
        x_values,
        y_values,
        c=colours,
        s=65,
        edgecolors="white",
        linewidths=0.6
    )


    # Line
    x_line = [
        min(x_values),
        max(x_values)
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


    # Fill the two sides
    ax.fill_between(
        x_line,
        y_line,
        max(y_values) + 20,
        color=RED,
        alpha=0.04
    )

    ax.fill_between(
        x_line,
        y_line,
        min(y_values) - 20,
        color=BLUE,
        alpha=0.04
    )


    ax.set_title(
        f"CLASSIFICATION // {best_score:.1f}%",
        color=TEXT,
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel("X VALUE", color=MUTED)
    ax.set_ylabel("Y VALUE", color=MUTED)

    ax.tick_params(colors=MUTED)

    for spine in ax.spines.values():
        spine.set_color("#303846")

    ax.grid(
        True,
        color="#303846",
        alpha=0.4
    )

    canvas.draw()


# ============================================================
# BUTTON
# ============================================================

classify_button = tk.Button(
    control_panel,
    text="CLASSIFY LINE",
    command=classify,
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#635bff",
    activebackground="#7b75ff",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

classify_button.pack(
    fill="x",
    padx=20,
    pady=20,
    ipady=12
)


# ============================================================
# INSTRUCTIONS
# ============================================================

instructions = tk.Label(
    control_panel,
    text=(
        "HOW IT WORKS\n\n"
        "1. Look at the red and blue points.\n"
        "2. Choose a gradient and intercept.\n"
        "3. Draw your separating line.\n"
        "4. The program checks every point.\n"
        "5. The higher score becomes your result."
    ),
    font=("Arial", 9),
    justify="left",
    fg=MUTED,
    bg=PANEL
)

instructions.pack(
    anchor="w",
    padx=20,
    pady=10
)


# ============================================================
# KEYBOARD SHORTCUT
# ============================================================

window.bind(
    "<Return>",
    lambda event: classify()
)


# ============================================================
# START
# ============================================================

window.mainloop()