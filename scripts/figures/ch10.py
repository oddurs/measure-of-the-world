#!/usr/bin/env python3
"""Generate figures for Chapter 10: Maskelyne's Nautical Almanac."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
import numpy as np


def navigator_procedure():
    """Flowchart of the 6-step lunar distance procedure.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6.4, 5.5))

    # Steps
    steps = [
        ('1. Observe\nMoon-Star Distance', 0, 5, '#e6f3ff'),
        ('2. Note\nChronometer Time', 0, 4, '#fff2e6'),
        ('3. Clear Distance\n(Parallax, Refraction)', 0, 3, '#ffe6e6'),
        ('4. Compare with\nNautical Almanac', 0, 2, '#e6ffe6'),
        ('5. Convert to\nLongitude', 0, 1, '#f0e6ff'),
        ('6. Determine\nPosition', 0, 0, '#ffffcc'),
    ]

    box_width = 2.2
    box_height = 0.6

    # Draw boxes
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

    # Time annotations
    times = ['2-3 min', '1 min', '30-60 min', '5 min', '5 min', '-']
    for i, (step, time) in enumerate(zip(steps, times)):
        if time != '-':
            ax.text(1.4, step[2], time, fontsize=7, ha='left', va='center',
                    color='#666666', style='italic')

    ax.text(1.4, 5.5, 'Typical time', fontsize=8, ha='left', va='center',
            color='#666666', fontweight='bold')

    # Total time box
    ax.text(0, -0.8, 'Total: 1-2 hours of calculation\n(vs. minutes with chronometer)',
            fontsize=9, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-2, 2.5)
    ax.set_ylim(-1.2, 5.8)
    ax.axis('off')

    save_figure(fig, 'navigator-procedure', chapter=10)


def almanac_structure():
    """Diagram showing the structure of the Nautical Almanac tables.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    # Table categories
    tables = [
        ('Lunar\nPositions', 0, 4, '#1f77b4', 'Every 12 hours'),
        ('Solar\nPositions', 1.5, 4, '#ff7f0e', 'Every 12 hours'),
        ('Lunar-Star\nDistances', 0, 3, '#2ca02c', 'Every 3 hours'),
        ('Lunar-Sun\nDistances', 1.5, 3, '#d62728', 'Every 3 hours'),
        ('Star\nPositions', 0, 2, '#9467bd', 'Reference stars'),
        ("Jupiter's\nMoons", 1.5, 2, '#8c564b', 'Eclipse times'),
        ('Auxiliary\nTables', 0.75, 1, '#7f7f7f', 'Interpolation, refraction'),
    ]

    box_width = 1.3
    box_height = 0.7

    for label, x, y, color, note in tables:
        box = FancyBboxPatch((x - box_width/2, y - box_height/2),
                             box_width, box_height,
                             boxstyle="round,pad=0.05,rounding_size=0.1",
                             facecolor=color, edgecolor='black', linewidth=1,
                             alpha=0.7)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=8,
                fontweight='bold', color='white')
        ax.text(x, y - box_height/2 - 0.15, note, ha='center', va='top',
                fontsize=7, color='#555555')

    # Header
    ax.text(0.75, 4.8, 'Nautical Almanac Contents', fontsize=11,
            ha='center', fontweight='bold')

    # Volume note
    ax.text(0.75, 0.14, 'Thousands of lines per year, all computed by hand',
            fontsize=8, ha='center', va='top', style='italic', color='#666666')

    ax.set_xlim(-1, 2.5)
    ax.set_ylim(-0.35, 5.2)
    ax.axis('off')

    save_figure(fig, 'almanac-structure', chapter=10)


def chronometer_vs_almanac():
    """Comparison of chronometer vs lunar distance methods.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(5.4, 3.6))

    categories = ['Cost', 'Calculation\nTime', 'Accuracy', 'Reliability']

    # Scores (1-5 scale, higher is better)
    chronometer = [1, 5, 5, 3]  # Expensive, fast, accurate, can fail
    almanac = [5, 1, 3, 5]      # Cheap, slow, moderate accuracy, always works

    x = np.arange(len(categories))
    width = 0.35

    bars1 = ax.bar(x - width/2, chronometer, width, label='Chronometer',
                   color='#1f77b4', edgecolor='black', linewidth=0.5)
    bars2 = ax.bar(x + width/2, almanac, width, label='Nautical Almanac',
                   color='#ff7f0e', edgecolor='black', linewidth=0.5)

    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylabel('Rating (5 = better)')
    ax.set_ylim(0, 6)
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, axis='y', alpha=0.3)

    # Annotations
    ax.text(-0.35, 1.3, '100-200', fontsize=7, ha='center', color='white', fontweight='bold')
    ax.text(0.35, 5.3, 'shillings', fontsize=7, ha='center', color='white', fontweight='bold')

    # Title
    ax.set_title('Method Comparison', fontsize=10)

    # Note
    ax.text(0.5, -0.32, 'Each method had advantages; ships often carried both',
            fontsize=8, style='italic', ha='center', transform=ax.transAxes)

    plt.tight_layout()
    save_figure(fig, 'chronometer-vs-almanac', chapter=10)


def _radial_ha(cos_a: float) -> str:
    """Horizontal alignment for a label placed radially outward."""
    if cos_a > 0.3:
        return 'left'
    if cos_a < -0.3:
        return 'right'
    return 'center'


def _radial_va(sin_a: float) -> str:
    """Vertical alignment for a label placed radially outward."""
    if sin_a > 0.3:
        return 'bottom'
    if sin_a < -0.3:
        return 'top'
    return 'center'


def computer_network():
    """Diagram showing the distributed computer network.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 5))

    # Central hub (Maskelyne at Greenwich)
    hub = Circle((0, 0), 0.42, facecolor='#1f77b4', edgecolor='black', linewidth=2)
    ax.add_patch(hub)
    ax.text(0, -0.58, 'Maskelyne\nGreenwich', ha='center', va='top',
            fontsize=8, fontweight='bold', zorder=5,
            bbox=dict(boxstyle='square,pad=0.15', facecolor='white',
                      edgecolor='none'))

    # Distributed computers, evenly spaced around the hub.  The names run to
    # thirteen characters, far wider than any node that would fit on the ring,
    # so each caption sits outside its marker and reads radially outward.
    computers = [
        ('Clergy\nYorkshire', 90),
        ('Mary Edwards\nLudlow', 150),
        ('Rupert Cotes\nBristol', 210),
        ('Other\nComputers', 270),
        ('Surveyors\nLondon', 330),
        ('Schoolmasters\nLincolnshire', 30),
    ]

    ring, node_r = 1.35, 0.17
    for name, angle in computers:
        rad = np.radians(angle)
        x, y = ring * np.cos(rad), ring * np.sin(rad)
        ax.add_patch(Circle((x, y), node_r, facecolor='#ff7f0e',
                            edgecolor='black', linewidth=1))

        # Connection line, stopping at both circles' edges
        ax.plot([0.42 * np.cos(rad), (ring - node_r) * np.cos(rad)],
                [0.42 * np.sin(rad), (ring - node_r) * np.sin(rad)],
                'k-', linewidth=0.8, alpha=0.5)

        lx, ly = (ring + node_r + 0.12) * np.cos(rad), (ring + node_r + 0.12) * np.sin(rad)
        ax.text(lx, ly, name, fontsize=7, ha=_radial_ha(np.cos(rad)),
                va=_radial_va(np.sin(rad)))

    # Arrows showing correspondence
    ax.annotate('', xy=(0.48, 0.28), xytext=(1.12, 0.65),
                arrowprops=dict(arrowstyle='<->', color='#2ca02c', lw=1.5))

    # Legend
    ax.text(0, -2.75, 'Redundant computation: same calculation\n' +
            'assigned to multiple computers independently',
            fontsize=8, ha='center', va='top', style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-3.4, 3.4)
    ax.set_ylim(-3.5, 2.4)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'computer-network', chapter=10)


if __name__ == "__main__":
    navigator_procedure()
    almanac_structure()
    chronometer_vs_almanac()
    computer_network()
