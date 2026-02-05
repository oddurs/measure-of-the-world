#!/usr/bin/env python3
"""Generate figures for Chapter 18: GMT, UT, UTC, and the Modern Timekeeping Stack."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Arc, Wedge
import numpy as np


def sidereal_vs_solar():
    """Diagram comparing sidereal and solar day.

    Shows why a sidereal day is ~4 minutes shorter than a solar day.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 5))

    # Sun at center
    sun = Circle((0, 0), 0.4, facecolor='#FFD700', edgecolor='black', linewidth=1.5)
    ax.add_patch(sun)
    ax.text(0, 0, 'Sun', fontsize=8, ha='center', va='center')

    # Earth orbit (simplified as circle)
    orbit_r = 3
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(orbit_r * np.cos(theta), orbit_r * np.sin(theta), 'b--',
            linewidth=1, alpha=0.5)

    # Earth at position 1 (noon, star on meridian)
    e1_x, e1_y = 3, 0
    earth1 = Circle((e1_x, e1_y), 0.25, facecolor='#1f77b4', edgecolor='black')
    ax.add_patch(earth1)
    ax.text(e1_x, e1_y - 0.5, 'Day 1\nNoon', fontsize=7, ha='center')

    # Star direction (far away, fixed)
    ax.annotate('', xy=(5, 0), xytext=(e1_x + 0.3, e1_y),
                arrowprops=dict(arrowstyle='->', color='purple', lw=1))
    ax.text(5.3, 0, 'Distant\nStar', fontsize=7, ha='left', va='center', color='purple')

    # Earth at position 2 (one sidereal day later)
    angle = 2 * np.pi / 365.25  # ~1 degree of orbital motion per day
    e2_x = orbit_r * np.cos(-angle)
    e2_y = orbit_r * np.sin(-angle)
    earth2 = Circle((e2_x, e2_y), 0.25, facecolor='#1f77b4', edgecolor='black', alpha=0.5)
    ax.add_patch(earth2)

    # After sidereal day, star is on meridian but sun is not
    ax.annotate('', xy=(5, e2_y), xytext=(e2_x + 0.3, e2_y),
                arrowprops=dict(arrowstyle='->', color='purple', lw=1, alpha=0.5))
    ax.text(e2_x, e2_y - 0.5, 'Sidereal\nday later', fontsize=7, ha='center', alpha=0.7)

    # Arrow showing extra rotation needed for solar day
    arc = Arc((e2_x, e2_y), 0.8, 0.8, angle=0, theta1=270, theta2=270+np.degrees(angle),
              color='red', linewidth=2)
    ax.add_patch(arc)

    # Info box
    ax.text(0, -3.5, 'Sidereal day: 23h 56m 04s (star returns to meridian)\n'
            'Solar day: 24h 00m 00s (Sun returns to meridian)\n'
            'Difference: 3m 56s (extra rotation for orbital motion)',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-5, 6)
    ax.set_ylim(-4.5, 2)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'sidereal-vs-solar', chapter=18)


def ut_variants():
    """Diagram showing UT0, UT1, UT2 relationships."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    levels = [
        ('UT0', 'Raw observation\n(affected by polar motion)', 4, '#d62728'),
        ('UT1', 'Corrected for polar motion\n(standard reference)', 3, '#ff7f0e'),
        ('UT2', 'Smoothed for\nseasonal variation', 2, '#2ca02c'),
        ('TAI', 'International Atomic Time\n(uniform, no Earth rotation)', 1, '#1f77b4'),
        ('UTC', 'Atomic time + leap seconds\n(civil standard)', 0, '#9467bd'),
    ]

    box_width = 2.5
    box_height = 0.7

    for label, desc, y, color in levels:
        box = FancyBboxPatch((-box_width/2, y - box_height/2),
                             box_width, box_height,
                             boxstyle="round,pad=0.05",
                             facecolor=color, edgecolor='black', linewidth=1,
                             alpha=0.7)
        ax.add_patch(box)
        ax.text(0, y, label, fontsize=11, ha='center', va='center',
                color='white', fontweight='bold')
        ax.text(box_width/2 + 0.3, y, desc, fontsize=8, ha='left', va='center')

    # Arrows showing corrections
    for i in range(len(levels) - 1):
        ax.annotate('', xy=(0, levels[i+1][2] + box_height/2),
                    xytext=(0, levels[i][2] - box_height/2),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

    # Labels for corrections
    corrections = [
        (4.5, 'Polar motion correction'),
        (3.5, 'Seasonal smoothing'),
        (2.5, 'Different definition'),
        (1.5, 'Leap second insertion'),
    ]

    for y, label in corrections:
        ax.text(-box_width/2 - 0.2, y - 0.5, label, fontsize=7, ha='right',
                va='center', color='gray', style='italic')

    ax.set_xlim(-4, 5)
    ax.set_ylim(-0.8, 5)
    ax.axis('off')

    save_figure(fig, 'ut-variants', chapter=18)


def atomic_second():
    """Diagram of cesium atom hyperfine transition defining the SI second."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 4))

    # Energy levels
    ax.plot([0.5, 2.5], [0, 0], 'b-', linewidth=3)
    ax.plot([0.5, 2.5], [2, 2], 'b-', linewidth=3)

    ax.text(1.5, 0, 'F = 3', fontsize=10, ha='center', va='bottom')
    ax.text(1.5, 2, 'F = 4', fontsize=10, ha='center', va='bottom')
    ax.text(0.3, 1, 'Cesium-133\nhyperfine\nstates', fontsize=8, ha='right', va='center')

    # Transition arrow
    ax.annotate('', xy=(1.5, 1.8), xytext=(1.5, 0.2),
                arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax.text(2.7, 1, r'$\nu = 9,192,631,770$ Hz', fontsize=10, color='red',
            ha='left', va='center')

    # Microwave photon
    wave_x = np.linspace(3.5, 5, 50)
    wave_y = 1 + 0.15 * np.sin(20 * (wave_x - 3.5))
    ax.plot(wave_x, wave_y, 'r-', linewidth=1.5)
    ax.text(4.25, 0.5, 'Microwave\nradiation', fontsize=8, ha='center')

    # SI definition box
    ax.text(3, -0.8, 'SI Definition (1967):\nThe second is 9,192,631,770 periods\n'
            'of radiation from Cs-133 hyperfine transition',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0',
                      edgecolor='black'))

    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-1.5, 2.8)
    ax.axis('off')

    save_figure(fig, 'atomic-second', chapter=18)


def leap_second():
    """Diagram showing how leap seconds work."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 4))

    # Timeline
    ax.axhline(2, color='black', linewidth=2, xmin=0.05, xmax=0.95)

    # Normal seconds
    for i in range(8):
        x = 1 + i * 0.8
        ax.plot(x, 2, '|', color='blue', markersize=15, markeredgewidth=2)
        if i < 5:
            ax.text(x, 1.7, f':5{7+i}', fontsize=7, ha='center')
        elif i == 5:
            ax.text(x, 1.7, ':59', fontsize=7, ha='center', color='red')
        elif i == 6:
            ax.text(x, 1.7, ':60', fontsize=7, ha='center', color='green', fontweight='bold')
        else:
            ax.text(x, 1.7, ':00', fontsize=7, ha='center')

    # Labels
    ax.text(3.4, 2.3, '23:59', fontsize=10, ha='center')
    ax.text(6.6, 2.3, '00:00', fontsize=10, ha='center')

    # Leap second highlight
    leap_x = 1 + 6 * 0.8
    ax.add_patch(Rectangle((leap_x - 0.3, 1.4), 0.6, 1.2,
                            facecolor='green', alpha=0.2, edgecolor='green',
                            linewidth=2))
    ax.text(leap_x, 0.9, 'LEAP\nSECOND', fontsize=8, ha='center',
            color='green', fontweight='bold')

    # UT1 vs UTC diagram
    ax.axhline(0.3, color='blue', linewidth=2, xmin=0.1, xmax=0.9, linestyle='--')
    ax.axhline(0, color='red', linewidth=2, xmin=0.1, xmax=0.9)

    ax.text(0.5, 0.3, 'UT1 (Earth)', fontsize=8, ha='left', va='bottom', color='blue')
    ax.text(0.5, 0, 'UTC (Atomic)', fontsize=8, ha='left', va='top', color='red')

    # Divergence and correction
    ax.annotate('', xy=(4, 0.3), xytext=(4, 0),
                arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
    ax.text(4.2, 0.15, 'Drift\n<0.9s', fontsize=7, ha='left', va='center', color='green')

    # Step correction
    ax.plot([6, 6], [0, 0.3], 'g-', linewidth=2)
    ax.text(6.2, 0.15, 'Leap\nsecond\ncorrects', fontsize=7, ha='left', va='center', color='green')

    ax.set_xlim(0, 8)
    ax.set_ylim(-0.5, 2.8)
    ax.axis('off')

    save_figure(fig, 'leap-second', chapter=18)


def timekeeping_stack():
    """The layers of time abstraction from Sun to atomic."""
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 7))

    layers = [
        ('Apparent Solar Time', 'Sun position in sky', '#ffcc00', 6),
        ('Mean Solar Time', 'Fictitious mean Sun', '#ff9900', 5),
        ('Greenwich Mean Time', 'Mean solar at Greenwich', '#ff6600', 4),
        ('Universal Time (UT1)', 'GMT + polar corrections', '#cc3300', 3),
        ('Atomic Time (TAI)', 'Cesium oscillations', '#0066cc', 2),
        ('UTC', 'TAI + leap seconds', '#003399', 1),
    ]

    box_width = 3.5
    box_height = 0.8

    for label, desc, color, y in layers:
        box = FancyBboxPatch((0 - box_width/2, y - box_height/2),
                             box_width, box_height,
                             boxstyle="round,pad=0.05",
                             facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(box)
        ax.text(0, y, f'{label}\n({desc})', fontsize=8, ha='center', va='center',
                color='white', fontweight='bold')

    # Arrows
    for i in range(len(layers) - 1):
        ax.annotate('', xy=(0, layers[i+1][3] + box_height/2),
                    xytext=(0, layers[i][3] - box_height/2),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

    # Annotations
    ax.text(2.2, 5.5, 'Human\nperception', fontsize=8, ha='left', color='gray')
    ax.text(2.2, 1.5, 'Physical\nprinciple', fontsize=8, ha='left', color='gray')

    # Arrow showing abstraction direction
    ax.annotate('', xy=(2.5, 1), xytext=(2.5, 6),
                arrowprops=dict(arrowstyle='->', color='gray', lw=2))
    ax.text(2.7, 3.5, 'Increasing\nabstraction', fontsize=8, ha='left',
            va='center', color='gray', rotation=270)

    ax.set_xlim(-3, 4)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    save_figure(fig, 'timekeeping-stack', chapter=18)


if __name__ == "__main__":
    sidereal_vs_solar()
    ut_variants()
    atomic_second()
    leap_second()
    timekeeping_stack()
