#!/usr/bin/env python3
"""Generate figures for Chapter 7: The Longitude Act and Its Incentives."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np


def prize_thresholds():
    """Visualize the relationship between accuracy requirements and prize amounts.
    """
    setup_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 4))

    # Left: Bar chart of prize amounts
    accuracies = [60, 40, 30]  # nautical miles
    prizes = [10000, 15000, 20000]  # pounds
    colors = ['#ff7f0e', '#2ca02c', '#1f77b4']

    bars = ax1.bar(range(3), prizes, color=colors, edgecolor='black', linewidth=0.5)

    ax1.set_xticks(range(3))
    ax1.set_xticklabels([f'{a} nm' for a in accuracies])
    ax1.set_xlabel('Accuracy requirement (nautical miles)')
    ax1.set_ylabel('Prize amount (pounds)')
    ax1.set_title('Longitude Act Prizes', fontsize=10)
    ax1.set_ylim(0, 25000)
    ax1.grid(True, axis='y', alpha=0.3)

    # Add value labels
    for bar, prize in zip(bars, prizes):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, height + 500,
                 f'{prize:,}', ha='center', fontsize=9, fontweight='bold')

    # Right: Convert to time/angular equivalents
    # At equator: 60 nm = 1 degree = 4 minutes of time
    time_errors = [4, 2.67, 2]  # minutes of time (at equator)
    angular_errors = [1, 0.67, 0.5]  # degrees

    x = np.arange(3)
    width = 0.35

    bars1 = ax2.bar(x - width/2, time_errors, width, label='Time error (min)',
                    color='#1f77b4', edgecolor='black', linewidth=0.5)
    bars2 = ax2.bar(x + width/2, angular_errors, width, label='Angular error (deg)',
                    color='#ff7f0e', edgecolor='black', linewidth=0.5)

    ax2.set_xticks(x)
    ax2.set_xticklabels([f'{a} nm' for a in accuracies])
    ax2.set_xlabel('Accuracy requirement')
    ax2.set_ylabel('Equivalent error')
    ax2.set_title('Physical Meaning', fontsize=10)
    ax2.legend(loc='upper right', fontsize=8)
    ax2.grid(True, axis='y', alpha=0.3)

    # Add annotation
    fig.text(0.5, 0.02, '30 nm accuracy requires clock error < 0.5 seconds/day over 6 weeks',
             ha='center', fontsize=8, style='italic')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15)

    save_figure(fig, 'prize-thresholds', chapter=7)


def board_timeline():
    """Timeline of key Board of Longitude decisions.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 5))

    # Key events
    events = [
        (1714, 'Longitude Act\npasses', 'policy'),
        (1730, 'H1 completed', 'harrison'),
        (1736, 'H1 sea trial', 'harrison'),
        (1761, 'H4 Jamaica trial\n(5.1s error)', 'harrison'),
        (1765, 'Maskelyne becomes\nAstronomer Royal', 'lunar'),
        (1767, 'Nautical Almanac\nfirst published', 'lunar'),
        (1772, 'H5 tested before\nKing George III', 'harrison'),
        (1773, 'Harrison awarded\nfinal payment', 'policy'),
        (1828, 'Board dissolved', 'policy'),
    ]

    # Color by category
    colors = {'policy': '#2ca02c', 'harrison': '#1f77b4', 'lunar': '#ff7f0e'}

    # Draw timeline
    years = [e[0] for e in events]
    ax.plot([min(years)-5, max(years)+5], [0, 0], 'k-', linewidth=2)

    # Alternate above/below for readability
    for i, (year, label, category) in enumerate(events):
        y_offset = 0.5 if i % 2 == 0 else -0.5
        color = colors[category]

        # Vertical line to event
        ax.plot([year, year], [0, y_offset * 0.8], color=color, linewidth=1.5)

        # Event marker
        ax.plot(year, 0, 'o', color=color, markersize=8)

        # Text label
        va = 'bottom' if y_offset > 0 else 'top'
        ax.text(year, y_offset, label, fontsize=8, ha='center', va=va,
                color=color, fontweight='bold')

    # Add year markers on timeline
    for year in range(1720, 1830, 20):
        ax.text(year, -0.12, str(year), fontsize=8, ha='center', va='top', color='gray')

    # Legend
    legend_elements = [
        mpatches.Patch(color='#2ca02c', label='Policy/Board'),
        mpatches.Patch(color='#1f77b4', label='Harrison chronometers'),
        mpatches.Patch(color='#ff7f0e', label='Lunar distance method'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=8)

    ax.set_xlim(1705, 1835)
    ax.set_ylim(-1, 1)
    ax.axis('off')

    save_figure(fig, 'board-timeline', chapter=7)


def competing_methods():
    """Comparison of the four proposed longitude methods.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    methods = ['Lunar Distance', 'Jupiter Moons', 'Magnetic\nVariation', 'Chronometer']

    # Ratings (1-5 scale) for different criteria
    # Categories: Theoretical soundness, Practicality at sea, Equipment cost, Skill required
    criteria = ['Theory', 'Practicality', 'Cost', 'Skill\nrequired']

    # Data: higher is better for all except skill required (inverted)
    data = {
        'Lunar Distance': [5, 3, 5, 2],  # Solid theory, moderate practicality, cheap, high skill
        'Jupiter Moons': [5, 1, 3, 3],   # Solid theory, poor at sea, telescope cost, moderate skill
        'Magnetic\nVariation': [2, 4, 5, 4],  # Poor theory (changing), practical, cheap, easy
        'Chronometer': [4, 5, 1, 5],     # Good theory, very practical, expensive, easy to use
    }

    x = np.arange(len(criteria))
    width = 0.2
    multiplier = 0

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

    for i, (method, values) in enumerate(data.items()):
        offset = width * multiplier
        bars = ax.bar(x + offset, values, width, label=method, color=colors[i],
                      edgecolor='black', linewidth=0.5)
        multiplier += 1

    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels(criteria)
    ax.set_ylabel('Rating (higher = better)')
    ax.set_ylim(0, 6)
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, axis='y', alpha=0.3)

    # Annotation
    ax.text(0.5, -0.12, 'Each method had distinct trade-offs; none was obviously superior',
            ha='center', fontsize=8, style='italic', transform=ax.transAxes)

    plt.tight_layout()

    save_figure(fig, 'competing-methods', chapter=7)


if __name__ == "__main__":
    prize_thresholds()
    board_timeline()
    competing_methods()
