#!/usr/bin/env python3
"""Generate figures for Chapter 2: The Founding of the Royal Observatory."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


def precision_comparison():
    """Compare positional accuracy of major star catalogs.

    Shows the revolutionary improvement from Tycho Brahe to Flamsteed,
    an order of magnitude in precision.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    # Historical catalog precision data (arc-seconds)
    catalogs = [
        ('Hipparchus\n(~130 BCE)', 3600, '#888888'),  # ~1 degree
        ('Ptolemy\n(~150 CE)', 1800, '#888888'),  # ~30 arc-min
        ('Ulugh Beg\n(1437)', 300, '#888888'),  # ~5 arc-min
        ('Tycho Brahe\n(1598)', 60, '#555555'),  # ~1 arc-min
        ('Flamsteed\n(1712)', 15, '#1f77b4'),  # 10-20 arc-sec, use midpoint
    ]

    names = [c[0] for c in catalogs]
    errors = [c[1] for c in catalogs]
    colors = [c[2] for c in catalogs]

    y_pos = np.arange(len(catalogs))

    # Horizontal bar chart
    bars = ax.barh(y_pos, errors, color=colors, edgecolor='black', linewidth=0.5)

    # Add value labels
    for i, (bar, error) in enumerate(zip(bars, errors)):
        if error >= 60:
            label = f"{error // 60}'"  # arc-minutes
        else:
            label = f'{error}"'  # arc-seconds
        ax.text(error + 50, bar.get_y() + bar.get_height()/2,
                label, va='center', fontsize=9)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(names)
    ax.set_xlabel('Positional error (arc-seconds)')
    ax.set_xscale('log')
    ax.set_xlim(5, 10000)

    # Add reference lines
    ax.axvline(x=60, color='gray', linestyle=':', linewidth=0.8, alpha=0.5)
    ax.axvline(x=3600, color='gray', linestyle=':', linewidth=0.8, alpha=0.5)
    ax.text(60, -0.6, "1'", ha='center', fontsize=8, color='gray')
    ax.text(3600, -0.6, "1°", ha='center', fontsize=8, color='gray')

    # Annotation for the improvement
    ax.annotate('', xy=(15, 4), xytext=(60, 3),
                arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=1.5))
    ax.text(30, 3.6, '4× improvement', fontsize=8, color='#1f77b4', ha='center')

    ax.invert_yaxis()
    ax.grid(True, axis='x', alpha=0.3)

    save_figure(fig, 'catalog-precision', chapter=2)


def mural_arc_principle():
    """Diagram showing the principle of the mural arc meridian transit.

    Shows how a fixed arc in the meridian plane measures both right ascension
    (from transit time) and declination (from altitude reading).
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(5, 5))

    # Draw the mural arc (quarter circle)
    arc_radius = 1.0
    theta = np.linspace(0, np.pi/2, 100)
    arc_x = arc_radius * np.cos(theta)
    arc_y = arc_radius * np.sin(theta)
    ax.plot(arc_x, arc_y, 'k-', linewidth=2.5)

    # Wall (vertical line at x=0)
    ax.plot([0, 0], [-0.1, 1.1], 'k-', linewidth=4, solid_capstyle='butt')
    ax.text(-0.08, 0.5, 'Wall\n(meridian\nplane)', fontsize=8, ha='right',
            va='center', color='#555555')

    # Graduated scale marks
    for angle in np.linspace(0, 90, 10):
        rad = np.radians(angle)
        x_inner = 0.92 * np.cos(rad)
        y_inner = 0.92 * np.sin(rad)
        x_outer = 1.0 * np.cos(rad)
        y_outer = 1.0 * np.sin(rad)
        ax.plot([x_inner, x_outer], [y_inner, y_outer], 'k-', linewidth=0.8)

    # Label some angles
    for angle, label in [(0, '0°'), (30, '30°'), (60, '60°'), (90, '90°')]:
        rad = np.radians(angle)
        x = 1.12 * np.cos(rad)
        y = 1.12 * np.sin(rad)
        ax.text(x, y, label, fontsize=8, ha='center', va='center')

    # Pivot point at origin
    ax.plot(0, 0, 'ko', markersize=8)
    ax.text(0.05, -0.08, 'Pivot', fontsize=8, ha='left')

    # Telescope/sighting arm pointing at a star (e.g., 45 degrees altitude)
    star_alt = 50  # degrees
    star_rad = np.radians(star_alt)
    arm_length = 1.3
    ax.plot([0, arm_length * np.cos(star_rad)],
            [0, arm_length * np.sin(star_rad)],
            'k-', linewidth=1.5)

    # Star symbol
    star_x = arm_length * np.cos(star_rad)
    star_y = arm_length * np.sin(star_rad)
    ax.plot(star_x, star_y, '*', color='#1f77b4', markersize=15)
    ax.text(star_x + 0.1, star_y + 0.05, 'Star on\nmeridian', fontsize=8,
            ha='left', va='bottom', color='#1f77b4')

    # Altitude arc
    alt_arc = np.linspace(0, star_rad, 30)
    alt_r = 0.3
    ax.plot(alt_r * np.cos(alt_arc), alt_r * np.sin(alt_arc), 'k-', linewidth=1)
    ax.text(0.38, 0.18, r'$h$', fontsize=11)

    # Horizon line
    ax.plot([-0.2, 1.4], [0, 0], 'k--', linewidth=0.8, alpha=0.5)
    ax.text(1.35, -0.05, 'Horizon', fontsize=8, ha='right', va='top',
            color='#555555')

    # North-South labels
    ax.annotate('', xy=(0.7, -0.25), xytext=(0.3, -0.25),
                arrowprops=dict(arrowstyle='<->', color='#555555', lw=1))
    ax.text(0.5, -0.32, 'N — S', fontsize=8, ha='center', color='#555555')

    # Clock annotation
    ax.text(0.7, 0.95, 'Transit time from\npendulum clock\n→ Right Ascension',
            fontsize=8, ha='left', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0',
                      edgecolor='#cccccc'))

    ax.text(0.7, 0.55, 'Altitude from\ngraduated scale\n→ Declination',
            fontsize=8, ha='left', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0',
                      edgecolor='#cccccc'))

    ax.set_xlim(-0.3, 1.5)
    ax.set_ylim(-0.45, 1.25)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'mural-arc-principle', chapter=2)


if __name__ == "__main__":
    precision_comparison()
    mural_arc_principle()
