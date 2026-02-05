#!/usr/bin/env python3
"""Generate figures for Chapter 22: Meridian Instruments."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Arc, Wedge, FancyArrowPatch
import numpy as np


def transit_instrument():
    """Diagram of a transit instrument showing key components."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 6))

    # Piers (stone pillars)
    pier_color = '#808080'
    ax.add_patch(Rectangle((-3, -0.5), 0.8, 3, facecolor=pier_color, edgecolor='black'))
    ax.add_patch(Rectangle((2.2, -0.5), 0.8, 3, facecolor=pier_color, edgecolor='black'))
    ax.text(-2.6, 1, 'Stone\nPier', fontsize=7, ha='center', va='center')
    ax.text(2.6, 1, 'Stone\nPier', fontsize=7, ha='center', va='center')

    # Pivots (Y-shaped bearings on top of piers)
    for x in [-2.6, 2.6]:
        ax.plot([x-0.2, x, x+0.2], [2.5, 2.8, 2.5], 'k-', linewidth=3)
        ax.plot(x, 2.65, 'o', color='#B8860B', markersize=8)

    # Horizontal axis (telescope tube)
    ax.plot([-2.6, 2.6], [2.65, 2.65], color='#4a4a4a', linewidth=8)
    ax.text(0, 2.65, 'Horizontal Axis', fontsize=8, ha='center', va='bottom',
            color='white', fontweight='bold')

    # Telescope tube (perpendicular to axis)
    telescope_angle = 60  # degrees from horizontal
    tube_length = 2.5
    dx = tube_length * np.cos(np.radians(telescope_angle))
    dy = tube_length * np.sin(np.radians(telescope_angle))

    ax.plot([0-dx, 0+dx], [2.65-dy, 2.65+dy], color='#2c2c2c', linewidth=12)
    ax.plot([0-dx, 0+dx], [2.65-dy, 2.65+dy], color='#1f77b4', linewidth=8)

    # Eyepiece end
    ax.add_patch(Circle((0-dx, 2.65-dy), 0.2, facecolor='#333', edgecolor='black'))
    ax.text(0-dx-0.5, 2.65-dy, 'Eyepiece', fontsize=7, ha='right', va='center')

    # Objective end
    ax.add_patch(Circle((0+dx, 2.65+dy), 0.25, facecolor='#87CEEB', edgecolor='black'))
    ax.text(0+dx+0.5, 2.65+dy, 'Objective\nLens', fontsize=7, ha='left', va='center')

    # Graduated circle on axis
    circle_x = 1.5
    ax.add_patch(Circle((circle_x, 2.65), 0.6, facecolor='#FFD700', edgecolor='black',
                        linewidth=2, alpha=0.8))
    # Add tick marks on circle
    for angle in range(0, 360, 15):
        r1, r2 = 0.5, 0.6
        x1 = circle_x + r1 * np.cos(np.radians(angle))
        y1 = 2.65 + r1 * np.sin(np.radians(angle))
        x2 = circle_x + r2 * np.cos(np.radians(angle))
        y2 = 2.65 + r2 * np.sin(np.radians(angle))
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=0.5)
    ax.text(circle_x, 2.65-1, 'Graduated\nCircle', fontsize=7, ha='center', va='top')

    # Crosshairs in field of view (inset)
    inset_x, inset_y = 4, 4
    ax.add_patch(Circle((inset_x, inset_y), 0.8, facecolor='black', edgecolor='gray'))
    ax.plot([inset_x-0.7, inset_x+0.7], [inset_y, inset_y], 'r-', linewidth=0.5)
    ax.plot([inset_x, inset_x], [inset_y-0.7, inset_y+0.7], 'r-', linewidth=0.5)
    # Multiple vertical wires
    for offset in [-0.3, 0.3]:
        ax.plot([inset_x+offset, inset_x+offset], [inset_y-0.5, inset_y+0.5],
                'r-', linewidth=0.5, alpha=0.5)
    ax.plot(inset_x+0.1, inset_y+0.2, '*', color='white', markersize=4)
    ax.text(inset_x, inset_y-1.2, 'Field of View\n(crosshairs)', fontsize=7, ha='center')

    # Arrow showing rotation
    arc = Arc((0, 2.65), 1.5, 1.5, angle=0, theta1=30, theta2=150,
              color='green', linewidth=2, linestyle='--')
    ax.add_patch(arc)
    ax.annotate('', xy=(0.3, 3.3), xytext=(0.5, 3.5),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5))
    ax.text(0, 3.8, 'Rotation in\nmeridian plane', fontsize=7, ha='center', color='green')

    # Meridian line on ground
    ax.axhline(-0.5, color='#8B4513', linewidth=3, xmin=0.1, xmax=0.9)
    ax.plot([0, 0], [-0.5, 0.5], 'r--', linewidth=2)
    ax.text(0, -0.8, 'Meridian Line (N-S)', fontsize=8, ha='center', color='red')

    ax.set_xlim(-4.5, 6)
    ax.set_ylim(-1.5, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'transit-instrument', chapter=22)


def mural_circle():
    """Diagram of a mural circle mounted on a wall."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 6))

    # Wall
    ax.fill([-3, 3, 3, -3], [0, 0, 5, 5], color='#d4c4a8', alpha=0.5)
    ax.text(0, 4.7, 'Meridian Wall (N-S)', fontsize=9, ha='center')

    # Large graduated circle
    circle_r = 2
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(circle_r * np.cos(theta), 2.5 + circle_r * np.sin(theta),
            'k-', linewidth=3)

    # Graduation marks
    for angle in range(0, 360, 5):
        r1 = circle_r - 0.1
        r2 = circle_r if angle % 15 != 0 else circle_r + 0.15
        x1 = r1 * np.cos(np.radians(angle))
        y1 = 2.5 + r1 * np.sin(np.radians(angle))
        x2 = r2 * np.cos(np.radians(angle))
        y2 = 2.5 + r2 * np.sin(np.radians(angle))
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=0.5 if angle % 15 != 0 else 1)

    # Degree labels
    for angle in [0, 90, 180, 270]:
        r = circle_r + 0.4
        x = r * np.cos(np.radians(angle))
        y = 2.5 + r * np.sin(np.radians(angle))
        ax.text(x, y, f'{angle}°', fontsize=8, ha='center', va='center')

    # Telescope mounted at center
    ax.add_patch(Circle((0, 2.5), 0.15, facecolor='#333', edgecolor='black'))

    # Telescope pointing at 45 degrees altitude
    telescope_angle = 45
    tube_length = 1.8
    dx = tube_length * np.cos(np.radians(telescope_angle))
    dy = tube_length * np.sin(np.radians(telescope_angle))
    ax.plot([0, dx], [2.5, 2.5+dy], color='#1f77b4', linewidth=6)
    ax.add_patch(Circle((dx, 2.5+dy), 0.12, facecolor='#87CEEB', edgecolor='black'))

    # Pointer/index
    ax.plot([0, 1.5*np.cos(np.radians(45))], [2.5, 2.5+1.5*np.sin(np.radians(45))],
            'r-', linewidth=2)
    ax.text(1.2, 3.3, 'Index', fontsize=7, ha='left', color='red')

    # Microscope for reading
    microscope_x = 1.7
    microscope_y = 2.5 + 1.7 * np.sin(np.radians(30))
    ax.plot([microscope_x, microscope_x+0.5], [microscope_y, microscope_y+0.3],
            'g-', linewidth=3)
    ax.add_patch(Circle((microscope_x+0.5, microscope_y+0.3), 0.1,
                        facecolor='#333', edgecolor='black'))
    ax.text(microscope_x+0.7, microscope_y+0.3, 'Reading\nMicroscope', fontsize=7,
            ha='left', va='center', color='green')

    # Altitude annotation
    arc = Arc((0, 2.5), 1, 1, angle=0, theta1=0, theta2=45,
              color='purple', linewidth=2)
    ax.add_patch(arc)
    ax.text(0.5, 2.7, '45°', fontsize=9, color='purple')

    # Horizon line
    ax.axhline(2.5, color='gray', linestyle='--', linewidth=1, xmin=0.55, xmax=0.95)
    ax.text(2.8, 2.5, 'Horizon', fontsize=7, ha='left', va='bottom', color='gray')

    ax.set_xlim(-3.5, 4)
    ax.set_ylim(-0.5, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'mural-circle', chapter=22)


def pivot_bearing():
    """Detailed view of precision pivot and bearing."""
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 5))

    # Y-shaped bearing (cross-section)
    bearing_color = '#B8860B'
    ax.fill([-1, -0.3, -0.3, -0.5, -0.5, -1, -1],
            [0, 0, 1.2, 1.5, 2, 2, 0],
            color=bearing_color, edgecolor='black', linewidth=2)
    ax.fill([1, 0.3, 0.3, 0.5, 0.5, 1, 1],
            [0, 0, 1.2, 1.5, 2, 2, 0],
            color=bearing_color, edgecolor='black', linewidth=2)

    # Cylindrical pivot (cross-section as circle)
    ax.add_patch(Circle((0, 1.5), 0.4, facecolor='#4a4a4a', edgecolor='black', linewidth=2))
    ax.text(0, 1.5, 'Pivot', fontsize=8, ha='center', va='center', color='white')

    # Contact points
    ax.plot(-0.35, 1.25, 'ro', markersize=8)
    ax.plot(0.35, 1.25, 'ro', markersize=8)
    ax.text(0, 0.8, 'Contact\nPoints', fontsize=7, ha='center', color='red')

    # Labels
    ax.text(-0.7, 2.2, 'Bearing', fontsize=9, ha='center', va='bottom')
    ax.annotate('', xy=(-0.7, 2), xytext=(-0.7, 2.2),
                arrowprops=dict(arrowstyle='->', color='black', lw=1))

    # Precision note
    ax.text(0, -0.8, 'Pivot ground to <0.001 inch\ncircularity tolerance',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0', edgecolor='gray'))

    # Oil film indication
    ax.plot([-0.38, -0.32], [1.35, 1.15], 'b-', linewidth=4, alpha=0.3)
    ax.plot([0.38, 0.32], [1.35, 1.15], 'b-', linewidth=4, alpha=0.3)
    ax.text(1.2, 1.3, 'Oil film', fontsize=7, ha='left', color='blue')

    # Axis direction
    ax.annotate('', xy=(1.5, 1.5), xytext=(0.5, 1.5),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(1.5, 1.7, 'Axis\ndirection', fontsize=7, ha='left', color='green')

    ax.set_xlim(-2, 2.5)
    ax.set_ylim(-1.5, 3)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'pivot-bearing', chapter=22)


def level_and_collimator():
    """Diagram showing striding level and collimator for alignment."""
    setup_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Left: Striding level
    ax1.set_title('Striding Level', fontsize=11, fontweight='bold')

    # Level body
    ax1.add_patch(Rectangle((-2, 0.8), 4, 0.4, facecolor='#B8860B', edgecolor='black'))

    # Legs striding over axis
    ax1.plot([-1.5, -1.5], [0, 0.8], 'k-', linewidth=3)
    ax1.plot([1.5, 1.5], [0, 0.8], 'k-', linewidth=3)

    # V-notches at bottom of legs
    for x in [-1.5, 1.5]:
        ax1.plot([x-0.15, x, x+0.15], [-0.15, 0, -0.15], 'k-', linewidth=2)

    # Axis (cylinder)
    ax1.add_patch(Rectangle((-2.5, -0.15), 5, 0.3, facecolor='#4a4a4a', edgecolor='black'))
    ax1.text(0, -0.5, 'Telescope Axis', fontsize=8, ha='center')

    # Bubble vial
    ax1.add_patch(Rectangle((-1.2, 1), 2.4, 0.2, facecolor='#90EE90',
                            edgecolor='black', alpha=0.7))
    ax1.add_patch(Circle((0, 1.1), 0.08, facecolor='#006400'))  # bubble
    ax1.text(0, 1.4, 'Spirit Level', fontsize=7, ha='center')

    # Graduations on vial
    for x in np.linspace(-1, 1, 11):
        ax1.plot([x, x], [0.95, 1], 'k-', linewidth=0.5)

    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-1, 2)
    ax1.set_aspect('equal')
    ax1.axis('off')

    # Right: Collimator
    ax2.set_title('Collimating Telescope', fontsize=11, fontweight='bold')

    # Main telescope
    ax2.add_patch(Rectangle((-2, -0.2), 3, 0.4, facecolor='#1f77b4', edgecolor='black'))

    # Objective lens
    ax2.add_patch(Rectangle((1, -0.3), 0.15, 0.6, facecolor='#87CEEB', edgecolor='black'))
    ax2.text(1.4, 0, 'Objective', fontsize=7, ha='left', va='center')

    # Crosshair at focal point
    ax2.plot([-2, -2], [-0.15, 0.15], 'r-', linewidth=1)
    ax2.plot([-2.1, -1.9], [0, 0], 'r-', linewidth=1)
    ax2.text(-2, -0.5, 'Illuminated\nCrosshair', fontsize=7, ha='center')

    # Parallel rays emerging
    for y in [-0.1, 0, 0.1]:
        ax2.annotate('', xy=(3, y), xytext=(1.2, y),
                    arrowprops=dict(arrowstyle='->', color='orange', lw=1))

    ax2.text(2.5, 0.4, 'Parallel light\n(simulates star\nat infinity)', fontsize=7,
             ha='center', color='orange')

    # Mounting suggestion
    ax2.add_patch(Rectangle((-2.3, -0.5), 0.3, 1, facecolor='gray', edgecolor='black'))
    ax2.text(-2.3, -0.8, 'Fixed\nMount', fontsize=6, ha='center')

    ax2.set_xlim(-3, 4)
    ax2.set_ylim(-1.5, 1.5)
    ax2.set_aspect('equal')
    ax2.axis('off')

    plt.tight_layout()
    save_figure(fig, 'level-and-collimator', chapter=22)


def airy_transit_circle():
    """The Airy Transit Circle that defined the Prime Meridian."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 6))

    # Room outline
    ax.add_patch(Rectangle((-3.5, 0), 7, 5, facecolor='#f5f5dc',
                           edgecolor='black', linewidth=2, fill=True))

    # Roof slit
    ax.fill([-0.8, 0.8, 0.8, -0.8], [5, 5, 5.5, 5.5], color='#87CEEB')
    ax.plot([-0.8, -0.8], [5, 5.5], 'k-', linewidth=2)
    ax.plot([0.8, 0.8], [5, 5.5], 'k-', linewidth=2)
    ax.text(0, 5.7, 'Roof Slit\n(N-S aligned)', fontsize=7, ha='center')

    # Piers
    for x in [-2, 2]:
        ax.add_patch(Rectangle((x-0.4, 0), 0.8, 3, facecolor='#808080',
                                edgecolor='black', linewidth=1))

    # Axis
    ax.plot([-2, 2], [3, 3], color='#4a4a4a', linewidth=10)

    # Telescope
    telescope_angle = 70
    tube_length = 2.2
    dx = tube_length * np.cos(np.radians(telescope_angle))
    dy = tube_length * np.sin(np.radians(telescope_angle))
    ax.plot([0-dx, 0+dx], [3-dy, 3+dy], color='#1f77b4', linewidth=8)

    # Graduated circles on both ends of axis
    for x in [-1.5, 1.5]:
        ax.add_patch(Circle((x, 3), 0.5, facecolor='#FFD700',
                            edgecolor='black', linewidth=2, alpha=0.8))

    # Star at top
    ax.plot(0, 5.8, '*', color='yellow', markersize=15, markeredgecolor='black')
    ax.text(0.3, 5.8, 'Star on\nmeridian', fontsize=7, ha='left', va='center')

    # Sight line
    ax.plot([0, 0], [3, 5.5], 'r--', linewidth=1, alpha=0.5)

    # Labels
    ax.text(-2, 2.5, 'East\nPier', fontsize=7, ha='center', va='top')
    ax.text(2, 2.5, 'West\nPier', fontsize=7, ha='center', va='top')

    # Ground meridian mark
    ax.plot(0, 0.1, 'v', color='red', markersize=10)
    ax.text(0, -0.3, 'Prime Meridian\n0° 0\' 0\"', fontsize=8, ha='center',
            color='red', fontweight='bold')

    # Specifications box
    specs = 'Airy Transit Circle (1851)\nAperture: 8 inches\nFocal length: 11.75 feet\nCircle diameter: 6 feet'
    ax.text(3.3, 4, specs, fontsize=7, ha='left', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray'))

    ax.set_xlim(-4, 5)
    ax.set_ylim(-0.8, 6.5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'airy-transit-circle', chapter=22)


def meridian_observation():
    """Sequence showing how a transit observation is made."""
    setup_style()
    fig, axes = plt.subplots(1, 4, figsize=(10, 3))

    titles = ['1. Star Approaching', '2. First Wire', '3. Central Wire', '4. Last Wire']

    for i, (ax, title) in enumerate(zip(axes, titles)):
        # Eyepiece view (dark circle)
        ax.add_patch(Circle((0, 0), 1, facecolor='black', edgecolor='gray'))

        # Crosshairs
        ax.plot([-0.9, 0.9], [0, 0], 'r-', linewidth=0.5, alpha=0.5)
        # Multiple vertical wires
        for x in [-0.5, -0.25, 0, 0.25, 0.5]:
            lw = 1 if x == 0 else 0.5
            ax.plot([x, x], [-0.8, 0.8], 'r-', linewidth=lw)

        # Star position (moving from left to right)
        star_x = -0.7 + i * 0.4
        ax.plot(star_x, 0.2, '*', color='white', markersize=8)

        # Time marker for each wire crossing
        if i > 0:
            ax.text(0, -1.3, f't{i}', fontsize=9, ha='center', color='blue')

        ax.set_title(title, fontsize=8)
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.5, 1.3)
        ax.set_aspect('equal')
        ax.axis('off')

    # Add explanation at bottom
    fig.text(0.5, 0.02, 'Transit time = mean of wire crossing times (eliminates personal equation)',
             fontsize=9, ha='center')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15)
    save_figure(fig, 'meridian-observation', chapter=22)


if __name__ == "__main__":
    transit_instrument()
    mural_circle()
    pivot_bearing()
    level_and_collimator()
    airy_transit_circle()
    meridian_observation()
