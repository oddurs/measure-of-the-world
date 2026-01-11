#!/usr/bin/env python3
"""Generate figures for Chapter 13: The Airy Transit Circle."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch, Arc
import numpy as np


def transit_circle_schematic():
    """Schematic diagram of the Airy transit circle.

    Shows the key components: telescope, pivot axis, graduated circle,
    and reticule.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 6))

    # Pivot axis (horizontal, east-west)
    axis_y = 2.5
    ax.plot([-3, 3], [axis_y, axis_y], 'k-', linewidth=8)
    ax.text(3.2, axis_y, 'Pivot axis\n(E-W)', fontsize=8, ha='left', va='center')

    # V-bearings
    for x in [-2.5, 2.5]:
        # V-shape bearing
        ax.plot([x-0.2, x, x+0.2], [axis_y-0.3, axis_y-0.1, axis_y-0.3],
                'k-', linewidth=2)
        ax.fill([x-0.2, x, x+0.2, x+0.2, x-0.2],
                [axis_y-0.3, axis_y-0.1, axis_y-0.3, axis_y-0.5, axis_y-0.5],
                color='gray', alpha=0.5)

    # Telescope tube (angled for visibility)
    telescope_angle = 30  # degrees from vertical
    tube_length = 3
    tube_end_x = tube_length * np.sin(np.radians(telescope_angle))
    tube_end_y = axis_y - tube_length * np.cos(np.radians(telescope_angle))

    # Tube body
    ax.plot([0, tube_end_x], [axis_y, tube_end_y],
            color='#8B4513', linewidth=15, solid_capstyle='round')

    # Objective lens (at bottom)
    ax.plot([tube_end_x - 0.3, tube_end_x + 0.3],
            [tube_end_y - 0.1, tube_end_y + 0.1], 'b-', linewidth=4)
    ax.text(tube_end_x + 0.5, tube_end_y, 'Objective\nlens', fontsize=7, ha='left')

    # Eyepiece (at top)
    eye_x = -0.3 * np.sin(np.radians(telescope_angle))
    eye_y = axis_y + 0.3 * np.cos(np.radians(telescope_angle))
    ax.plot([eye_x - 0.2, eye_x + 0.2], [eye_y, eye_y], 'k-', linewidth=4)
    ax.text(eye_x - 0.5, eye_y + 0.2, 'Eyepiece', fontsize=7, ha='right')

    # Graduated circle (on one side)
    circle_x = 2
    circle = Circle((circle_x, axis_y), 1.2, fill=False, edgecolor='#1f77b4',
                    linewidth=2)
    ax.add_patch(circle)

    # Tick marks on circle
    for angle in range(0, 360, 15):
        rad = np.radians(angle)
        x1 = circle_x + 1.1 * np.cos(rad)
        y1 = axis_y + 1.1 * np.sin(rad)
        x2 = circle_x + 1.3 * np.cos(rad)
        y2 = axis_y + 1.3 * np.sin(rad)
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=0.5)

    ax.text(circle_x, axis_y + 1.7, 'Graduated\ncircle', fontsize=8,
            ha='center', color='#1f77b4')

    # Reading microscope
    ax.plot([circle_x + 0.8, circle_x + 1.5], [axis_y + 0.8, axis_y + 1.3],
            'k-', linewidth=2)
    ax.plot(circle_x + 1.5, axis_y + 1.3, 'ko', markersize=6)
    ax.text(circle_x + 1.7, axis_y + 1.3, 'Reading\nmicroscope', fontsize=7, ha='left')

    # Star ray
    star_dist = 2.5
    star_x = tube_end_x + star_dist * np.sin(np.radians(telescope_angle))
    star_y = tube_end_y - star_dist * np.cos(np.radians(telescope_angle))
    ax.annotate('', xy=(tube_end_x + 0.2, tube_end_y - 0.2),
                xytext=(star_x, star_y),
                arrowprops=dict(arrowstyle='->', color='gold', lw=2))
    ax.plot(star_x, star_y, '*', color='gold', markersize=15,
            markeredgecolor='black', markeredgewidth=0.5)
    ax.text(star_x + 0.3, star_y, 'Starlight', fontsize=8, color='#B8860B')

    # Meridian plane indicator
    ax.plot([0, 0], [-1, 5], 'g--', linewidth=1, alpha=0.5)
    ax.text(0.1, 4.5, 'Meridian\nplane', fontsize=8, color='green', ha='left')

    # Level (striding level on axis)
    level_x = 0
    level = Rectangle((level_x - 0.8, axis_y + 0.1), 1.6, 0.3,
                       facecolor='#87CEEB', edgecolor='black', linewidth=1)
    ax.add_patch(level)
    ax.plot(level_x, axis_y + 0.25, 'o', color='white', markersize=4)  # bubble
    ax.text(level_x, axis_y + 0.6, 'Level', fontsize=7, ha='center')

    # Reticule inset
    inset_ax = fig.add_axes([0.08, 0.12, 0.22, 0.22])
    inset_ax.set_xlim(-1, 1)
    inset_ax.set_ylim(-1, 1)

    # Five vertical wires
    for x in [-0.6, -0.3, 0, 0.3, 0.6]:
        inset_ax.axvline(x, color='black', linewidth=0.5)

    # One horizontal wire
    inset_ax.axhline(0, color='black', linewidth=0.5)

    # Star crossing
    inset_ax.plot(0.1, 0.1, '*', color='gold', markersize=8)

    inset_ax.set_aspect('equal')
    inset_ax.set_title('Reticule', fontsize=8)
    inset_ax.axis('off')

    ax.set_xlim(-4, 5)
    ax.set_ylim(-2, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'transit-circle-schematic', chapter=13)


def personal_equation():
    """Diagram illustrating the personal equation concept.

    Shows how different observers have systematic timing biases.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 4))

    # Timeline
    ax.axhline(0.5, color='black', linewidth=2)
    ax.plot(3, 0.5, '|', color='black', markersize=20, markeredgewidth=2)
    ax.text(3, 0.2, 'True transit\ntime', fontsize=9, ha='center')

    # Observer recordings
    observers = [
        ('Airy', 2.7, 1.5, '#1f77b4', '-0.32s (early)'),
        ('Assistant', 3.4, 2.0, '#ff7f0e', '+0.18s (late)'),
        ('Mean', 3.05, 2.5, '#2ca02c', 'Corrected'),
    ]

    for name, time, y, color, label in observers:
        ax.plot(time, 0.5, 'v', color=color, markersize=12)
        ax.plot([time, time], [0.5, y], '--', color=color, linewidth=1, alpha=0.5)
        ax.text(time, y + 0.1, f'{name}\n{label}', fontsize=8, ha='center',
                color=color, fontweight='bold')

    # Arrows showing correction
    ax.annotate('', xy=(3, 1.3), xytext=(2.7, 1.3),
                arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=1.5))
    ax.annotate('', xy=(3, 1.8), xytext=(3.4, 1.8),
                arrowprops=dict(arrowstyle='->', color='#ff7f0e', lw=1.5))

    ax.text(2.85, 1.4, '+0.32s', fontsize=7, ha='center', color='#1f77b4')
    ax.text(3.2, 1.9, '-0.18s', fontsize=7, ha='center', color='#ff7f0e')

    # Scale
    ax.text(1, 0.5, 'Time', fontsize=9, ha='right', va='center')
    for t in [2, 2.5, 3, 3.5, 4]:
        ax.plot(t, 0.45, '|', color='gray', markersize=8)

    # Title annotation
    ax.text(3, -0.3, 'Personal equation: systematic observer timing bias\n' +
            'Must be measured and corrected for each observer',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(0.5, 5)
    ax.set_ylim(-0.8, 3)
    ax.axis('off')

    save_figure(fig, 'personal-equation', chapter=13)


def precision_evolution():
    """Chart showing the evolution of positional astronomy precision.

    Log-scale showing improvement from Tycho to Gaia.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 4.5))

    # Data from table in chapter
    instruments = [
        ("Tycho's quadrant", 1600, 90),
        ("Flamsteed's mural arc", 1700, 15),
        ("Bradley's zenith sector", 1750, 2.5),
        ("Airy's transit circle", 1850, 0.35),
        ("Photographic astrometry", 1900, 0.1),
        ("CCD astrometry", 2000, 0.01),
        ("Gaia satellite", 2020, 0.00001),
    ]

    years = [i[1] for i in instruments]
    errors = [i[2] for i in instruments]
    names = [i[0] for i in instruments]

    ax.semilogy(years, errors, 'b-o', linewidth=2, markersize=8)

    # Label each point
    offsets = [(10, 1.3), (10, 1.3), (10, 1.3), (10, 1.3),
               (-80, 1.3), (10, 0.7), (10, 1.3)]
    for year, error, name, (xoff, yoff) in zip(years, errors, names, offsets):
        ax.annotate(name, xy=(year, error), xytext=(year + xoff, error * yoff),
                    fontsize=7, ha='left' if xoff > 0 else 'right',
                    arrowprops=dict(arrowstyle='-', color='gray', lw=0.5) if xoff > 50 else None)

    # Highlight Airy
    airy_idx = 3
    ax.plot(years[airy_idx], errors[airy_idx], 'ro', markersize=12, zorder=5)
    ax.annotate('Airy Transit Circle', xy=(years[airy_idx], errors[airy_idx]),
                xytext=(1870, 2), fontsize=9, fontweight='bold', color='red',
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Typical Error (arcseconds)', fontsize=10)
    ax.set_xlim(1550, 2050)
    ax.set_ylim(0.000001, 200)
    ax.grid(True, alpha=0.3, which='both')

    # Reference lines
    ax.axhline(1, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.text(1560, 1.2, '1 arcsec', fontsize=7, color='gray')

    plt.tight_layout()
    save_figure(fig, 'precision-evolution', chapter=13)


def prime_meridian_offset():
    """Diagram showing the 102m offset between Airy and WGS84 meridians.

    Birds-eye view of Greenwich Observatory grounds.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 5))

    # Observatory building (simplified rectangle)
    building = Rectangle((-50, -30), 100, 60, facecolor='#d4c4a8',
                         edgecolor='black', linewidth=1.5)
    ax.add_patch(building)
    ax.text(0, 0, 'Greenwich\nObservatory', fontsize=9, ha='center', va='center')

    # Airy meridian (the brass line)
    ax.axvline(0, color='#8B4513', linewidth=4, label='Airy Meridian (1884)')
    ax.text(-5, 60, "Airy's\nTransit Circle\nMeridian", fontsize=8,
            ha='right', color='#8B4513', fontweight='bold')

    # WGS84 meridian (102m east)
    offset = 102 * 0.5  # scaled for display
    ax.axvline(offset, color='#1f77b4', linewidth=4, linestyle='--',
               label='WGS84 Meridian')
    ax.text(offset + 5, 60, 'WGS84\nMeridian\n(GPS)', fontsize=8,
            ha='left', color='#1f77b4', fontweight='bold')

    # Distance annotation
    ax.annotate('', xy=(offset, -50), xytext=(0, -50),
                arrowprops=dict(arrowstyle='<->', color='green', lw=2))
    ax.text(offset/2, -55, '102 meters', fontsize=10, ha='center',
            color='green', fontweight='bold')

    # Compass rose
    compass_x, compass_y = -70, 50
    ax.annotate('', xy=(compass_x, compass_y + 15), xytext=(compass_x, compass_y),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.text(compass_x, compass_y + 18, 'N', fontsize=9, ha='center', fontweight='bold')
    ax.annotate('', xy=(compass_x + 10, compass_y), xytext=(compass_x, compass_y),
                arrowprops=dict(arrowstyle='->', color='black', lw=1))
    ax.text(compass_x + 13, compass_y, 'E', fontsize=8, ha='left')

    # Tourists on brass line
    for y in [-20, -10, 0, 10]:
        ax.plot(0, y, 'o', color='#ff7f0e', markersize=4)

    ax.text(15, -20, 'Tourists on\nbrass line', fontsize=7,
            ha='left', color='#ff7f0e')

    ax.set_xlim(-100, 100)
    ax.set_ylim(-70, 80)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.legend(loc='lower right', fontsize=8)

    # Note
    ax.text(0, -68, 'The historic Prime Meridian and modern GPS reference differ\n' +
            'due to improved measurement of Earth\'s gravitational field',
            fontsize=8, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    save_figure(fig, 'prime-meridian-offset', chapter=13)


def error_budget():
    """Pie chart showing error sources in transit circle observations."""
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 5))

    # Error sources (typical magnitudes in arcsec, squared for variance)
    sources = [
        ('Personal equation\n(after correction)', 0.15, '#1f77b4'),
        ('Refraction\nuncertainty', 0.3, '#ff7f0e'),
        ('Graduation errors', 0.25, '#2ca02c'),
        ('Flexure', 0.15, '#d62728'),
        ('Pivot irregularity', 0.1, '#9467bd'),
        ('Thermal drift', 0.1, '#8c564b'),
        ('Atmospheric\nturbulence', 0.35, '#e377c2'),
    ]

    labels = [s[0] for s in sources]
    sizes = [s[1]**2 for s in sources]  # variances add
    colors = [s[2] for s in sources]

    wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors,
                                       autopct=lambda p: f'{np.sqrt(p/100 * sum(sizes)):.2f}"',
                                       pctdistance=0.7, labeldistance=1.15,
                                       textprops={'fontsize': 8})

    for autotext in autotexts:
        autotext.set_fontsize(7)
        autotext.set_color('white')

    ax.set_title('Error Budget (typical magnitudes in arcseconds)', fontsize=10)

    # Total error annotation
    total_var = sum(sizes)
    total_err = np.sqrt(total_var)
    ax.text(0, -1.4, f'Combined error (RSS): {total_err:.2f} arcseconds',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    save_figure(fig, 'error-budget', chapter=13)


def observation_reduction():
    """Flowchart showing the data reduction process for a transit observation."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    steps = [
        ('Raw observation:\nClock time + altitude', 0, 4, '#e6f3ff'),
        ('Personal equation\ncorrection', 0, 3, '#fff2e6'),
        ('Refraction\ncorrection', 0, 2, '#ffe6e6'),
        ('Sidereal time\nconversion', 0, 1, '#e6ffe6'),
        ('Final coordinates:\nRA and Dec', 0, 0, '#f0e6ff'),
    ]

    box_width = 2.2
    box_height = 0.6

    for label, x, y, color in steps:
        box = FancyBboxPatch((x - box_width/2, y - box_height/2),
                             box_width, box_height,
                             boxstyle="round,pad=0.05,rounding_size=0.1",
                             facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=9)

    # Arrows
    for i in range(len(steps) - 1):
        y1 = steps[i][2] - box_height/2
        y2 = steps[i+1][2] + box_height/2
        ax.annotate('', xy=(0, y2), xytext=(0, y1),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.2))

    # Side annotations
    annotations = [
        (1.5, 3, r'$t_{corr} = t_{obs} + PE$'),
        (1.5, 2, r'$h_{true} = h_{obs} - R$'),
        (1.5, 1, r'$\alpha = \alpha_0 + 1.0027 \times t$'),
    ]

    for x, y, text in annotations:
        ax.text(x, y, text, fontsize=9, ha='left', va='center',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                          edgecolor='#cccccc', alpha=0.8))

    ax.set_xlim(-2.5, 3.5)
    ax.set_ylim(-0.8, 4.8)
    ax.axis('off')

    save_figure(fig, 'observation-reduction', chapter=13)


if __name__ == "__main__":
    transit_circle_schematic()
    personal_equation()
    precision_evolution()
    prime_meridian_offset()
    error_budget()
    observation_reduction()
