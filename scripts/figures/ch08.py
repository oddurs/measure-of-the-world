#!/usr/bin/env python3
"""Generate figures for Chapter 8: The Lunar Distance Method."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Arc, Circle
import numpy as np


def lunar_parallax():
    """Diagram showing the effect of parallax on lunar observations.

    Parallax causes the Moon to appear displaced when observed from
    Earth's surface vs. Earth's center.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 5))

    # Earth (large circle at bottom)
    earth_center = (0, -2)
    earth_radius = 1.5
    earth = Circle(earth_center, earth_radius, facecolor='#87CEEB',
                   edgecolor='black', linewidth=1.5, alpha=0.6)
    ax.add_patch(earth)
    ax.text(0, -2, 'Earth', fontsize=10, ha='center', va='center')

    # Observer on Earth's surface
    obs_angle = 60  # degrees from vertical
    obs_x = earth_center[0] + earth_radius * np.sin(np.radians(obs_angle))
    obs_y = earth_center[1] + earth_radius * np.cos(np.radians(obs_angle))
    ax.plot(obs_x, obs_y, 'ko', markersize=8)
    ax.text(obs_x + 0.15, obs_y + 0.1, 'Observer', fontsize=9, ha='left')

    # Moon position (true, from Earth center)
    moon_dist = 4.0  # arbitrary units
    moon_angle = 30  # degrees from vertical
    moon_x = moon_dist * np.sin(np.radians(moon_angle))
    moon_y = moon_dist * np.cos(np.radians(moon_angle)) - 2

    ax.plot(moon_x, moon_y, 'o', color='#FFD700', markersize=15)
    ax.text(moon_x + 0.2, moon_y + 0.2, 'Moon\n(true position)', fontsize=8, ha='left')

    # Line from Earth center to Moon (true direction)
    ax.plot([0, moon_x], [-2, moon_y], 'b--', linewidth=1, alpha=0.7, label='From Earth center')

    # Line from observer to Moon (apparent direction)
    ax.plot([obs_x, moon_x], [obs_y, moon_y], 'r-', linewidth=1.5, label='From observer')

    # Extend the apparent line to show apparent position
    direction_x = moon_x - obs_x
    direction_y = moon_y - obs_y
    length = np.sqrt(direction_x**2 + direction_y**2)
    apparent_x = obs_x + direction_x * 1.3
    apparent_y = obs_y + direction_y * 1.3
    ax.plot([obs_x, apparent_x], [obs_y, apparent_y], 'r:', linewidth=1, alpha=0.5)

    # Parallax angle annotation
    arc_radius = 1.5
    # Draw arc to show parallax angle
    ax.annotate('', xy=(moon_x - 0.3, moon_y - 0.5),
                xytext=(moon_x - 0.1, moon_y - 0.8),
                arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
    ax.text(moon_x - 0.5, moon_y - 0.4, 'Parallax\nangle', fontsize=8, color='green', ha='center')

    # Formula box
    ax.text(0, 2.5, r'Parallax in altitude: $p = HP \cdot \cos(h)$' + '\n' +
            r'$HP \approx 57$ arcmin (lunar horizontal parallax)',
            fontsize=9, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.legend(loc='upper right', fontsize=8)
    ax.set_xlim(-3, 4)
    ax.set_ylim(-4, 3)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'lunar-parallax', chapter=8)


def clearing_procedure():
    """Flowchart showing the clearing procedure for lunar distances.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 6))

    # Box dimensions
    box_width = 2.2
    box_height = 0.6

    # Define steps
    steps = [
        ('Sextant\nObservation', 0, 5, '#e6f3ff'),
        ('Index Error\nCorrection', 0, 4, '#fff2e6'),
        ('Parallax\nCorrection', 0, 3, '#ffe6e6'),
        ('Refraction\nCorrection', 0, 2, '#e6ffe6'),
        ('True Lunar\nDistance', 0, 1, '#e6e6ff'),
        ('Table\nLookup', 0, 0, '#f0e6ff'),
        ('Greenwich\nTime', 0, -1, '#ffffcc'),
    ]

    # Draw boxes and arrows
    for label, x, y, color in steps:
        box = FancyBboxPatch((x - box_width/2, y - box_height/2),
                             box_width, box_height,
                             boxstyle="round,pad=0.05,rounding_size=0.1",
                             facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=9)

    # Arrows between boxes
    for i in range(len(steps) - 1):
        y1 = steps[i][2] - box_height/2
        y2 = steps[i+1][2] + box_height/2
        ax.annotate('', xy=(0, y2), xytext=(0, y1),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.2))

    # Side annotations with magnitudes
    annotations = [
        (4, 'Raw angle from sextant'),
        (3, 'Subtract instrument error (few arcmin)'),
        (2, r'Subtract $HP \cdot \cos(h) \approx 20-50$ arcmin'),
        (1, r'Add/subtract $\sim 1-5$ arcmin'),
        (0, 'Compare with Mayer/Maskelyne tables'),
        (-1, r'Interpolate: $\Delta t \rightarrow$ longitude'),
    ]

    for y, text in annotations:
        ax.text(1.4, y, text, fontsize=7, ha='left', va='center',
                color='#555555', style='italic')

    ax.set_xlim(-2, 4.5)
    ax.set_ylim(-2, 6)
    ax.axis('off')

    save_figure(fig, 'clearing-procedure', chapter=8)


def lunar_distance_errors():
    """Bar chart showing error sources in lunar distance method.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    sources = ['Sextant\nprecision', 'Table\naccuracy', 'Parallax/\nRefraction',
               'Interpolation', 'Combined\n(RSS)']
    errors = [3, 1, 3, 0.5, 4.4]  # arcminutes
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

    bars = ax.bar(sources, errors, color=colors, edgecolor='black', linewidth=0.5)

    # Add horizontal line for "combined" level
    ax.axhline(y=4.4, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)

    # Value labels
    for bar, err in zip(bars, errors):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.2,
                f'{err:.1f}\'', ha='center', fontsize=9)

    ax.set_ylabel('Error (arcminutes)')
    ax.set_title('Error Sources in Lunar Distance Method', fontsize=10)
    ax.set_ylim(0, 6)
    ax.grid(True, axis='y', alpha=0.3)

    # Annotation
    ax.text(0.5, -0.15, r'Combined error of $\sim$4 arcmin $\rightarrow$ $\sim$30 nautical miles',
            fontsize=8, style='italic', ha='center', transform=ax.transAxes)

    plt.tight_layout()

    save_figure(fig, 'lunar-distance-errors', chapter=8)


def moon_motion_rate():
    """Show the Moon's motion rate among the stars.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    # Time over one sidereal month
    days = np.linspace(0, 27.3, 100)
    hours = days * 24

    # Moon's angular position (simplified)
    position = (days / 27.3) * 360  # degrees

    ax.plot(days, position, 'b-', linewidth=1.5)

    # Mark key rates
    ax.axhline(y=180, color='gray', linestyle=':', linewidth=0.8, alpha=0.5)
    ax.axhline(y=360, color='gray', linestyle=':', linewidth=0.8, alpha=0.5)

    # Rate annotation
    ax.text(13.65, 190, '180 deg in 13.65 days', fontsize=8, ha='center', color='gray')

    # Show 1-hour motion
    ax.annotate('', xy=(1, 12), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    ax.text(0.5, 20, r'1 hour: $\sim 0.5$ deg', fontsize=9, color='red')

    ax.set_xlabel('Days')
    ax.set_ylabel('Angular position (degrees)')
    ax.set_title('Moon Motion Through the Zodiac', fontsize=10)
    ax.set_xlim(0, 28)
    ax.set_ylim(0, 380)
    ax.grid(True, alpha=0.3)

    # Key equation
    ax.text(20, 50, r'Rate: $\frac{360°}{27.3 \text{ days}} \approx 0.5°/\text{hour}$',
            fontsize=10, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    save_figure(fig, 'moon-motion-rate', chapter=8)


if __name__ == "__main__":
    lunar_parallax()
    clearing_procedure()
    lunar_distance_errors()
    moon_motion_rate()
