#!/usr/bin/env python3
"""Generate figures for Chapter 16: The Distribution of Time."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch
import numpy as np


def time_ball_mechanism():
    """Diagram showing the time ball mechanism.

    Shows the ball, mast, electromagnetic release, and signal path.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 6))

    # Observatory dome (simplified arc)
    dome_theta = np.linspace(0, np.pi, 50)
    dome_x = 2 * np.cos(dome_theta)
    dome_y = 1 * np.sin(dome_theta)
    ax.plot(dome_x, dome_y, 'k-', linewidth=2)
    ax.fill_between(dome_x, 0, dome_y, color='#d4c4a8', alpha=0.5)

    # Mast
    ax.plot([0, 0], [0.5, 4], 'k-', linewidth=4)
    ax.text(0.2, 2, 'Mast', fontsize=8, ha='left')

    # Time ball (raised position)
    ball_raised = Circle((0, 3.8), 0.4, facecolor='red', edgecolor='black',
                          linewidth=2, alpha=0.5)
    ax.add_patch(ball_raised)
    ax.text(0.6, 3.8, 'Ball (raised)', fontsize=8, ha='left', alpha=0.7)

    # Time ball (dropped position)
    ball_dropped = Circle((0, 1.5), 0.4, facecolor='red', edgecolor='black',
                           linewidth=2)
    ax.add_patch(ball_dropped)
    ax.text(0.6, 1.5, 'Ball (dropped)', fontsize=8, ha='left')

    # Arrow showing drop
    ax.annotate('', xy=(0, 2), xytext=(0, 3.3),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax.text(-0.3, 2.7, 'Drop', fontsize=8, ha='right', color='blue')

    # Electromagnetic release
    release = Rectangle((-0.3, 3.9), 0.6, 0.3, facecolor='#888888',
                        edgecolor='black', linewidth=1)
    ax.add_patch(release)
    ax.text(0.5, 4.05, 'Electromagnet\nrelease', fontsize=7, ha='left')

    # Wire to master clock
    ax.plot([0.3, 2, 2], [4.05, 4.05, -0.5], 'g-', linewidth=1.5)
    ax.text(2.2, 1.5, 'Wire to\nmaster clock', fontsize=7, ha='left', color='green')

    # Observer with telescope
    obs_x, obs_y = -3, -1
    ax.plot(obs_x, obs_y, 'ko', markersize=10)
    ax.plot([obs_x, obs_x + 1], [obs_y, obs_y + 0.3], 'k-', linewidth=3)  # telescope
    ax.text(obs_x, obs_y - 0.4, 'Observer', fontsize=8, ha='center')

    # Line of sight
    ax.plot([obs_x + 0.5, 0], [obs_y + 0.15, 1.5], 'r--', linewidth=1, alpha=0.5)

    # Ship on Thames
    ship_x = 3
    ax.plot([ship_x - 0.5, ship_x + 0.5], [-1.5, -1.5], 'k-', linewidth=2)
    ax.plot([ship_x, ship_x], [-1.5, -1], 'k-', linewidth=2)  # mast
    ax.text(ship_x, -2, 'Ship on\nThames', fontsize=7, ha='center')

    # Ground/water
    ax.axhline(-1.5, color='#4169E1', linewidth=1, alpha=0.5)
    ax.fill_between([-4, 4], [-2.5, -2.5], [-1.5, -1.5], color='#4169E1', alpha=0.2)

    # Timing info
    ax.text(0, -2.3, '1:00 PM daily\nVisible to ~3 km', fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-2.8, 5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'time-ball-mechanism', chapter=16)


def time_distribution_hierarchy():
    """Diagram showing the hierarchy of time distribution.

    From atomic clocks to end users.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 6))

    levels = [
        ('Atomic Time Standards\n(Cesium/H-maser clocks)', 0, 5, '#1f77b4'),
        ('National Metrology\nInstitutes (NIST, PTB)', 0, 4, '#ff7f0e'),
        ('Satellite Systems\n(GPS, Galileo, GLONASS)', -1.5, 3, '#2ca02c'),
        ('Terrestrial Networks\n(Radio, Internet NTP)', 1.5, 3, '#d62728'),
        ('Local Receivers\n(Clocks, computers)', 0, 2, '#9467bd'),
        ('End Users', 0, 1, '#8c564b'),
    ]

    box_width = 2.5
    box_height = 0.6

    for label, x, y, color in levels:
        box = FancyBboxPatch((x - box_width/2, y - box_height/2),
                             box_width, box_height,
                             boxstyle="round,pad=0.05,rounding_size=0.1",
                             facecolor=color, edgecolor='black', linewidth=1,
                             alpha=0.7)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=8,
                color='white', fontweight='bold')

    # Arrows connecting levels
    connections = [
        ((0, 4.7), (0, 4.3)),        # Atomic to National
        ((0, 3.7), (-1.5, 3.3)),     # National to Satellite
        ((0, 3.7), (1.5, 3.3)),      # National to Terrestrial
        ((-1.5, 2.7), (0, 2.3)),     # Satellite to Local
        ((1.5, 2.7), (0, 2.3)),      # Terrestrial to Local
        ((0, 1.7), (0, 1.3)),        # Local to End Users
    ]

    for (x1, y1), (x2, y2) in connections:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

    # Accuracy labels
    accuracies = [
        (2.5, 5, '~10 ns'),
        (2.5, 4, '~100 ns'),
        (-3.5, 3, '~100 ns'),
        (3.5, 3, '~1 ms'),
        (2.5, 2, '~10 ms'),
    ]

    for x, y, acc in accuracies:
        ax.text(x, y, acc, fontsize=7, ha='center', va='center',
                style='italic', color='gray')

    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 6)
    ax.axis('off')

    save_figure(fig, 'time-distribution-hierarchy', chapter=16)


def error_budget_timeball():
    """Visualization of error sources in time ball observation."""
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    sources = [
        ('Observer reaction', 0.10),
        ('Ball fall timing', 0.02),
        ('EM release', 0.01),
        ('Atmospheric refraction', 0.01),
        ('Light travel', 0.005),
    ]

    labels = [s[0] for s in sources]
    values = [s[1] for s in sources]
    colors = ['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4', '#9467bd']

    # Horizontal bar chart
    y_pos = np.arange(len(labels))
    bars = ax.barh(y_pos, values, color=colors, edgecolor='black', linewidth=0.5)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel('Error magnitude (seconds)', fontsize=10)
    ax.set_xlim(0, 0.12)

    # Value labels
    for bar, val in zip(bars, values):
        width = bar.get_width()
        ax.text(width + 0.003, bar.get_y() + bar.get_height()/2,
                f'{val*1000:.0f} ms', va='center', fontsize=8)

    # Total error annotation
    total_rss = np.sqrt(sum(v**2 for v in values))
    ax.axvline(total_rss, color='red', linestyle='--', linewidth=2)
    ax.text(total_rss + 0.005, len(labels) - 0.5,
            f'Total (RSS)\n{total_rss*1000:.0f} ms',
            fontsize=8, color='red')

    ax.grid(True, axis='x', alpha=0.3)
    plt.tight_layout()

    save_figure(fig, 'error-budget-timeball', chapter=16)


def telegraph_vs_radio():
    """Comparison diagram of telegraph and radio time distribution."""
    setup_style()
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))

    # Telegraph (left)
    ax = axes[0]
    ax.set_title('Telegraph Distribution', fontsize=10, fontweight='bold')

    # Greenwich
    gw = Circle((0, 3), 0.3, facecolor='#1f77b4', edgecolor='black')
    ax.add_patch(gw)
    ax.text(0, 3, 'GW', fontsize=8, ha='center', va='center', color='white')

    # Telegraph poles and wires
    stations = [(-1.5, 1), (0, 1), (1.5, 1)]
    for x, y in stations:
        ax.plot([x, x], [y, y + 0.5], 'k-', linewidth=2)  # pole
        station = Rectangle((x - 0.3, y - 0.3), 0.6, 0.3,
                            facecolor='#ff7f0e', edgecolor='black')
        ax.add_patch(station)

    # Wires from Greenwich
    for x, y in stations:
        ax.plot([0, x], [2.7, y + 0.5], 'k-', linewidth=1)

    ax.text(0, 0.3, 'Wired connection\nrequired', fontsize=8, ha='center')
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(0, 4)
    ax.axis('off')

    # Radio (right)
    ax = axes[1]
    ax.set_title('Radio Distribution', fontsize=10, fontweight='bold')

    # Transmitter
    tx = Circle((0, 3), 0.3, facecolor='#1f77b4', edgecolor='black')
    ax.add_patch(tx)
    ax.text(0, 3, 'TX', fontsize=8, ha='center', va='center', color='white')

    # Antenna
    ax.plot([0, 0], [3.3, 3.8], 'k-', linewidth=2)
    ax.plot([-0.3, 0.3], [3.8, 3.8], 'k-', linewidth=2)

    # Radio waves (concentric arcs)
    for r in [0.8, 1.3, 1.8]:
        theta = np.linspace(-np.pi/3, -2*np.pi/3, 30)
        x = r * np.cos(theta)
        y = 3 + r * np.sin(theta)
        ax.plot(x, y, 'r-', linewidth=1, alpha=0.5)

    # Receivers
    receivers = [(-1.5, 1), (0, 0.8), (1.5, 1.2)]
    for x, y in receivers:
        rx = Rectangle((x - 0.2, y - 0.15), 0.4, 0.3,
                       facecolor='#2ca02c', edgecolor='black')
        ax.add_patch(rx)
        ax.plot([x, x], [y + 0.15, y + 0.4], 'k-', linewidth=1)  # antenna

    ax.text(0, 0.2, 'No wires needed\nBroadcast to all', fontsize=8, ha='center')
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(0, 4)
    ax.axis('off')

    plt.tight_layout()
    save_figure(fig, 'telegraph-vs-radio', chapter=16)


def galvanic_network():
    """Diagram of the Observatory's galvanic time distribution network."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    # Master clock (center)
    clock = FancyBboxPatch((-0.5, 2), 1, 1.5,
                            boxstyle="round,pad=0.05",
                            facecolor='#1f77b4', edgecolor='black', linewidth=2)
    ax.add_patch(clock)
    ax.text(0, 2.75, 'Master\nClock', fontsize=9, ha='center', va='center',
            color='white', fontweight='bold')

    # Clock pendulum
    ax.plot([0, 0], [2, 1.7], 'k-', linewidth=2)
    ax.plot(0, 1.6, 'o', color='gold', markersize=8, markeredgecolor='black')

    # Connected instruments
    instruments = [
        ('Transit\nCircle', -2.5, 3),
        ('Time Ball', 0, 4.5),
        ('Post\nOffice', 2.5, 3),
        ('Mural\nCircle', -2.5, 1),
        ('Telegraph\nStation', 2.5, 1),
    ]

    box_size = 0.8
    for name, x, y in instruments:
        box = FancyBboxPatch((x - box_size/2, y - box_size/2),
                             box_size, box_size,
                             boxstyle="round,pad=0.05",
                             facecolor='#ff7f0e', edgecolor='black', linewidth=1)
        ax.add_patch(box)
        ax.text(x, y, name, fontsize=7, ha='center', va='center',
                color='white', fontweight='bold')

        # Wire from master clock
        ax.plot([0, x], [2.75, y], 'g-', linewidth=1.5)

    # Electrical pulse annotation
    ax.annotate('', xy=(-1.2, 2.2), xytext=(-0.5, 2.5),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(-1.5, 2.5, 'Electrical\npulse', fontsize=7, ha='right', color='green')

    # Title
    ax.text(0, 0.3, 'Galvanic Network: simultaneous time signals\nto all connected instruments',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'galvanic-network', chapter=16)


if __name__ == "__main__":
    time_ball_mechanism()
    time_distribution_hierarchy()
    error_budget_timeball()
    telegraph_vs_radio()
    galvanic_network()
