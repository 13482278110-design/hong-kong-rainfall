# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

import csv
import os
import math
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Ellipse
from matplotlib.transforms import Affine2D

DATA_FILE = "data/daily_HKO_RF_2026.csv"
MONTH = 2

days = []
rainfall = []


# --------------------------------------------------
# 1. Read the original HKO rainfall data
# --------------------------------------------------

with open(DATA_FILE, encoding="utf-8-sig") as file:
    reader = csv.reader(file)

    next(reader)
    next(reader)
    next(reader)  # header

    for row in reader:
        if len(row) < 4:
            continue

        month = int(row[1])

        if month == MONTH:
            days.append(int(row[2]))

            value = 0.0 if row[3] == "Trace" else float(row[3])
            rainfall.append(value)


# --------------------------------------------------
# 2. Raindrop shape
# --------------------------------------------------
# Shorter tip + fuller lower body

vertices = [
    (0.00, 1.00),       # tip

    (-0.08, 0.82),
    (-0.24, 0.60),
    (-0.42, 0.34),

    (-0.62, 0.04),
    (-0.76, -0.28),
    (-0.72, -0.52),

    (-0.66, -0.82),
    (-0.38, -1.00),
    (0.00, -1.02),

    (0.38, -1.00),
    (0.66, -0.82),
    (0.72, -0.52),

    (0.76, -0.28),
    (0.62, 0.04),
    (0.42, 0.34),

    (0.24, 0.60),
    (0.08, 0.82),
    (0.00, 1.00),

    (0.00, 1.00),
]

codes = [
    Path.MOVETO,

    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE4,

    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE4,

    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE4,

    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE4,

    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE4,

    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE4,

    Path.CLOSEPOLY,
]

drop_path = Path(vertices, codes)


# --------------------------------------------------
# 3. Draw one raindrop
# --------------------------------------------------

def draw_drop(ax, x, rainfall_value):

    # Square-root scale keeps small rainfall visible
    # while preserving the exceptional 39 mm day.
    scale = math.sqrt(rainfall_value)

    # Width grows a little faster than before,
    # so the drops look rounder rather than needle-like.
    height = 0.32 + scale * 0.43
    width = 0.16 + scale * 0.11

    # Put the rounded bottom close to the baseline.
    center_y = height * 1.02

    transform = (
        Affine2D()
        .scale(width, height)
        .translate(x, center_y)
        + ax.transData
    )

    # Main drop
    outer_drop = PathPatch(
        drop_path,
        transform=transform,
        facecolor="#68B4DF",
        edgecolor="#287EAE",
        linewidth=1.0,
        alpha=0.82,
        zorder=4,
    )

    ax.add_patch(outer_drop)

    # Soft inner layer
    inner_transform = (
        Affine2D()
        .scale(width * 0.73, height * 0.73)
        .translate(x, center_y - height * 0.10)
        + ax.transData
    )

    inner_drop = PathPatch(
        drop_path,
        transform=inner_transform,
        facecolor="#B9E1F5",
        edgecolor="none",
        alpha=0.34,
        zorder=5,
    )

    ax.add_patch(inner_drop)

    # Small white highlight
    highlight = Ellipse(
        (
            x - width * 0.25,
            center_y + height * 0.05
        ),
        width=max(width * 0.16, 0.025),
        height=max(height * 0.25, 0.055),
        angle=-12,
        facecolor="white",
        edgecolor="none",
        alpha=0.58,
        zorder=6,
    )

    ax.add_patch(highlight)

    return height, center_y


# --------------------------------------------------
# 4. Canvas
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(16, 9))

fig.subplots_adjust(
    left=0.07,
    right=0.95,
    top=0.72,
    bottom=0.22
)

dark_blue = "#284D66"
light_blue = "#BCD4E1"
grey = "#7D858A"


# --------------------------------------------------
# 5. Draw all 28 days
# --------------------------------------------------

for day, value in zip(days, rainfall):

    if value == 0:

        # Dry day
        ax.scatter(
            day,
            0.10,
            s=13,
            color=light_blue,
            alpha=0.50,
            edgecolors="none",
            zorder=3,
        )

    else:

        height, center_y = draw_drop(
            ax,
            day,
            value
        )

        top = center_y + height

        # Real rainfall value
        ax.text(
            day,
            top + 0.25,
            f"{value:g}",
            ha="center",
            va="bottom",
            fontsize=10,
            color=dark_blue,
        )


# --------------------------------------------------
# 6. Axis
# --------------------------------------------------

ax.set_xlim(0.4, 28.8)
ax.set_ylim(-0.45, 7.2)

ax.set_xticks(days)
ax.set_yticks([])

ax.set_xlabel(
    "DAY OF FEBRUARY",
    fontsize=10,
    color=dark_blue,
    labelpad=22,
)

ax.tick_params(
    axis="x",
    length=0,
    pad=10,
    labelsize=9,
    colors=dark_blue,
)

# Quiet baseline
ax.axhline(
    0,
    color=light_blue,
    linewidth=0.9,
    alpha=0.75,
    zorder=1,
)

for spine in ax.spines.values():
    spine.set_visible(False)


# --------------------------------------------------
# 7. Title
# --------------------------------------------------

fig.text(
    0.07,
    0.91,
    "FEBRUARY IN RAIN",
    fontsize=31,
    color=dark_blue,
    ha="left",
)

fig.text(
    0.07,
    0.855,
    "HONG KONG  ·  2026",
    fontsize=12,
    color=dark_blue,
    ha="left",
)

fig.text(
    0.07,
    0.81,
    "28 days of rainfall, translated into 28 marks.",
    fontsize=9,
    color=grey,
    ha="left",
)


# --------------------------------------------------
# 8. Supporting text
# --------------------------------------------------

fig.text(
    0.93,
    0.91,
    "SAME CITY\nDIFFERENT DAYS\nDIFFERENT SKIES",
    fontsize=9,
    color=dark_blue,
    ha="right",
    va="top",
    linespacing=1.7,
)

fig.text(
    0.07,
    0.085,
    "A QUIETER MONTH,\nUNTIL THE LAST DAY.",
    fontsize=10,
    color=dark_blue,
    ha="left",
    linespacing=1.6,
)

fig.text(
    0.93,
    0.085,
    "SOURCE: HONG KONG OBSERVATORY\nDAILY TOTAL RAINFALL",
    fontsize=8,
    color=grey,
    ha="right",
    linespacing=1.6,
)


# --------------------------------------------------
# 9. Save
# --------------------------------------------------

os.makedirs("out", exist_ok=True)

plt.savefig(
    "out/rainfall.png",
    dpi=200,
    bbox_inches="tight"
)

plt.show()