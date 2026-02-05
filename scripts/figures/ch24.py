#!/usr/bin/env python3
"""Generate figures for Chapter 24: Heritage, Tourism, and Symbolism."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Wedge, Polygon, Arc
import numpy as np


def meridian_offset_detail():
    """Detailed diagram of the 102m offset between Airy and WGS84 meridians."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 5))

    # Ground representation
    ax.fill([-50, 150, 150, -50], [-0.5, -0.5, 0, 0], color='#90EE90', alpha=0.5)

    # Observatory building outline
    ax.add_patch(Rectangle((-20, 0), 50, 25, facecolor='#f5f5dc',
                           edgecolor='black', linewidth=2))
    ax.text(5, 27, 'Royal Observatory', fontsize=10, ha='center', fontweight='bold')

    # Airy Transit Circle location (brass line)
    ax.axvline(0, color='#B8860B', linewidth=6, ymin=0, ymax=0.85)
    ax.add_patch(Rectangle((-3, 0), 6, 0.5, facecolor='#B8860B', edgecolor='black'))
    ax.text(0, -3, "Airy Transit Circle\n(Brass Line)\n0° 0' 0\" (Astronomical)",
            fontsize=8, ha='center', color='#B8860B', fontweight='bold')

    # WGS84 meridian
    ax.axvline(102, color='#1f77b4', linewidth=4, linestyle='--', ymin=0, ymax=0.85)
    ax.text(102, -3, "WGS84 Meridian\n(GPS Zero)\n0° 0' 0\" (Geodetic)",
            fontsize=8, ha='center', color='#1f77b4', fontweight='bold')

    # Distance annotation
    ax.annotate('', xy=(102, 15), xytext=(0, 15),
                arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax.text(51, 17, '102.478 meters', fontsize=10, ha='center', color='red',
            fontweight='bold')

    # Tourists at brass line
    for x in [-8, 0, 8]:
        ax.plot(x, 5, 'o', color='#ff7f0e', markersize=8)
        ax.plot([x, x], [2, 5], 'k-', linewidth=1)  # body
    ax.text(0, 8, 'Tourists straddle\n"wrong" line', fontsize=7, ha='center',
            color='#ff7f0e')

    # GPS reading indication
    ax.add_patch(Rectangle((85, 5), 30, 12, facecolor='white',
                            edgecolor='black', linewidth=1))
    ax.text(100, 14, 'GPS Reading:', fontsize=7, ha='center')
    ax.text(100, 10, "0° 0' 5.31\" W", fontsize=9, ha='center',
            fontweight='bold', color='red')
    ax.text(100, 6.5, '(at brass line)', fontsize=6, ha='center', color='gray')

    # Explanation
    explanation = ('The offset arises from:\n'
                   '1. Local gravity anomalies (deflection of vertical)\n'
                   '2. Different reference frames (geoid vs ellipsoid)')
    ax.text(130, 22, explanation, fontsize=7, ha='left', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0',
                      edgecolor='gray'))

    ax.set_xlim(-60, 170)
    ax.set_ylim(-8, 32)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'meridian-offset-detail', chapter=24)


def deflection_of_vertical():
    """Diagram explaining deflection of the vertical."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    # Earth cross-section (simplified)
    earth_r = 2
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(earth_r * np.cos(theta), earth_r * np.sin(theta), 'k-', linewidth=2)
    ax.fill(earth_r * np.cos(theta), earth_r * np.sin(theta),
            color='#8B4513', alpha=0.3)

    # Mass anomaly (denser rock)
    anomaly_x, anomaly_y = 1.0, 1.2
    ax.add_patch(Circle((anomaly_x, anomaly_y), 0.4, facecolor='#4a4a4a',
                        edgecolor='black', linewidth=2))
    ax.text(anomaly_x, anomaly_y, 'Dense\nrock', fontsize=6, ha='center',
            va='center', color='white')

    # Observer location on surface
    obs_angle = 60  # degrees from horizontal
    obs_x = earth_r * np.cos(np.radians(obs_angle))
    obs_y = earth_r * np.sin(np.radians(obs_angle))
    ax.plot(obs_x, obs_y, 'go', markersize=10)
    ax.text(obs_x + 0.3, obs_y + 0.3, 'Observer', fontsize=8, color='green')

    # True vertical (toward Earth center)
    ax.annotate('', xy=(0, 0), xytext=(obs_x, obs_y),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax.text(-0.3, 0.5, 'True vertical\n(to Earth center)', fontsize=7,
            ha='right', color='blue')

    # Plumb line (deflected toward mass)
    # Calculate deflection toward the anomaly
    deflection_angle = 8  # degrees
    plumb_angle = obs_angle - deflection_angle
    plumb_length = 1.5
    plumb_end_x = obs_x - plumb_length * np.cos(np.radians(plumb_angle))
    plumb_end_y = obs_y - plumb_length * np.sin(np.radians(plumb_angle))

    ax.annotate('', xy=(plumb_end_x, plumb_end_y), xytext=(obs_x, obs_y),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(plumb_end_x - 0.3, plumb_end_y, 'Plumb line\n(local vertical)',
            fontsize=7, ha='right', color='red')

    # Deflection angle arc
    arc = Arc((obs_x, obs_y), 0.8, 0.8, angle=180+obs_angle,
              theta1=-deflection_angle, theta2=0, color='purple', linewidth=2)
    ax.add_patch(arc)
    ax.text(obs_x - 0.6, obs_y - 0.3, r'$\varepsilon$', fontsize=12, color='purple')

    # Gravity vectors toward anomaly
    for i in range(3):
        gx = obs_x + 0.2 * i
        gy = obs_y - 0.1 * i
        ax.annotate('', xy=(anomaly_x, anomaly_y),
                   xytext=(gx, gy),
                   arrowprops=dict(arrowstyle='->', color='orange', lw=1,
                                  alpha=0.5, connectionstyle='arc3,rad=0.1'))

    ax.text(1.8, 0.3, 'Extra gravitational\npull toward mass', fontsize=7,
            color='orange')

    # Info box
    ax.text(0, -2.8, 'At Greenwich, local mass anomalies deflect the vertical\n'
            'by ~5 arcseconds, causing the 102m offset',
            fontsize=8, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='gray'))

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3.3, 3)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'deflection-of-vertical', chapter=24)


def time_ball():
    """The Greenwich Time Ball mechanism and purpose."""
    setup_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Left: Time ball sequence
    ax1.set_title('Time Ball Signal Sequence', fontsize=11, fontweight='bold')

    times = ['12:55', '12:58', '13:00']
    positions = [0.3, 0.8, 0.2]  # Height on mast
    labels = ['Ball raised\nhalfway', 'Ball at top', 'Ball drops\n(TIME SIGNAL)']

    for i, (time, pos, label) in enumerate(zip(times, positions, labels)):
        x = i * 2

        # Mast
        ax1.plot([x, x], [0, 2], 'k-', linewidth=4)

        # Cross-arm at top
        ax1.plot([x-0.3, x+0.3], [2, 2], 'k-', linewidth=3)

        # Ball
        ball_y = pos * 1.5 + 0.3
        color = 'red' if i < 2 else 'green'
        ax1.add_patch(Circle((x, ball_y), 0.2, facecolor=color, edgecolor='black'))

        # Time label
        ax1.text(x, -0.3, time, fontsize=10, ha='center', fontweight='bold')

        # Description
        ax1.text(x, -0.8, label, fontsize=7, ha='center')

        # Drop arrow for last frame
        if i == 2:
            ax1.annotate('', xy=(x, 0.5), xytext=(x, 1.5),
                        arrowprops=dict(arrowstyle='->', color='green', lw=2))

    ax1.set_xlim(-1, 5)
    ax1.set_ylim(-1.5, 2.8)
    ax1.set_aspect('equal')
    ax1.axis('off')

    # Right: Ships waiting for signal
    ax2.set_title('Ships in Thames Synchronized Chronometers', fontsize=11,
                  fontweight='bold')

    # Water
    ax2.fill([-3, 3, 3, -3], [-0.5, -0.5, 0, 0], color='#4169E1', alpha=0.5)

    # Ships
    ship_positions = [(-2, 0.2), (0, 0.3), (1.5, 0.15)]
    for sx, sy in ship_positions:
        # Hull
        hull_x = [sx-0.4, sx+0.4, sx+0.3, sx-0.3]
        hull_y = [sy, sy, sy-0.2, sy-0.2]
        ax2.fill(hull_x, hull_y, color='#8B4513', edgecolor='black')
        # Mast
        ax2.plot([sx, sx], [sy, sy+0.8], 'k-', linewidth=2)

    # Observatory on hill
    ax2.fill([-0.5, 0.5, 0.5, -0.5], [1.5, 1.5, 2, 2], color='#f5f5dc',
             edgecolor='black')

    # Time ball on observatory
    ax2.plot([0, 0], [2, 2.5], 'k-', linewidth=3)
    ax2.add_patch(Circle((0, 2.3), 0.15, facecolor='red', edgecolor='black'))

    # Sight lines from ships
    for sx, sy in ship_positions:
        ax2.plot([sx, 0], [sy+0.5, 2.3], 'r--', linewidth=1, alpha=0.5)

    ax2.text(0, 2.8, 'Time Ball visible\nfrom river', fontsize=7, ha='center')

    # Chronometer on ship
    ax2.add_patch(Circle((-2, 0.6), 0.15, facecolor='#FFD700', edgecolor='black'))
    ax2.text(-2, 0.9, 'Chronometer\nset to 13:00', fontsize=6, ha='center')

    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-0.8, 3.2)
    ax2.set_aspect('equal')
    ax2.axis('off')

    plt.tight_layout()
    save_figure(fig, 'time-ball', chapter=24)


def visitor_experience():
    """The tourist experience at the Prime Meridian."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 5))

    # Courtyard layout (top view)
    ax.add_patch(Rectangle((-3, -2), 6, 4, facecolor='#d4d4d4',
                           edgecolor='black', linewidth=2, fill=True))

    # Brass meridian line
    ax.plot([0, 0], [-2, 2], color='#B8860B', linewidth=8)
    ax.text(0, 2.3, 'Brass Meridian Line', fontsize=9, ha='center',
            color='#B8860B', fontweight='bold')

    # Photo spots
    photo_spots = [(-1.5, 0), (1.5, 0), (0, -1.5)]
    for px, py in photo_spots:
        ax.plot(px, py, 's', color='#1f77b4', markersize=12)
        ax.text(px, py, 'P', fontsize=8, ha='center', va='center', color='white',
                fontweight='bold')

    # Straddle pose indication
    ax.plot(-0.3, 0.5, 'o', color='#ff7f0e', markersize=10)
    ax.plot(0.3, 0.5, 'o', color='#ff7f0e', markersize=10)
    ax.plot([0, 0], [0.5, 0.8], 'k-', linewidth=2)
    ax.plot(0, 0.9, 'o', color='#ffccaa', markersize=8)
    ax.text(0.8, 0.7, '"One foot in each\nhemisphere"', fontsize=7, ha='left',
            color='#ff7f0e')

    # Buildings around
    ax.add_patch(Rectangle((-3.5, -2.5), 0.5, 5, facecolor='#f5f5dc',
                           edgecolor='black'))
    ax.text(-3.25, 0, 'F\nl\na\nm\ns\nt\ne\ne\nd', fontsize=5, ha='center',
            va='center')

    ax.add_patch(Rectangle((3, -2.5), 0.5, 5, facecolor='#f5f5dc',
                           edgecolor='black'))
    ax.text(3.25, 0, 'M\ne\nr\ni\nd\ni\na\nn\n\nB\nl\nd\ng', fontsize=5,
            ha='center', va='center')

    # Laser beam (at night)
    ax.annotate('', xy=(0, 3), xytext=(0, 2),
                arrowprops=dict(arrowstyle='-', color='green', lw=3, alpha=0.7))
    ax.text(0.5, 2.5, 'Green laser\n(night)', fontsize=7, ha='left', color='green')

    # Annual visitors stat
    ax.text(0, -3.2, 'Over 1 million visitors annually', fontsize=10, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffffcc',
                      edgecolor='gray'))

    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-3.8, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'visitor-experience', chapter=24)


def greenwich_symbolism():
    """Greenwich as symbol of global coordination."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    # Central globe
    globe_r = 1.5
    theta = np.linspace(0, 2*np.pi, 100)
    ax.fill(globe_r * np.cos(theta), globe_r * np.sin(theta),
            color='#4169E1', alpha=0.3, edgecolor='black', linewidth=2)

    # Meridian lines
    for lon in range(-60, 90, 30):
        x_offset = globe_r * np.sin(np.radians(lon))
        visible_range = np.sqrt(1 - (x_offset/globe_r)**2) if abs(x_offset) < globe_r else 0
        if visible_range > 0:
            y_range = np.linspace(-visible_range * globe_r, visible_range * globe_r, 50)
            ax.plot(np.full_like(y_range, x_offset), y_range, 'k-', linewidth=0.5, alpha=0.5)

    # Prime meridian highlighted
    ax.plot([0, 0], [-globe_r, globe_r], 'r-', linewidth=3)
    ax.text(0.2, 0, 'Prime\nMeridian', fontsize=7, ha='left', color='red')

    # Connecting lines to concepts
    concepts = [
        (3, 2, 'UTC / Time Zones'),
        (3, 0.5, 'GPS Navigation'),
        (3, -1, 'Maritime Coordination'),
        (-3, 2, 'Scientific Standard'),
        (-3, 0.5, 'Aviation Routes'),
        (-3, -1, 'International Law'),
    ]

    for cx, cy, label in concepts:
        ax.annotate(label, xy=(0, 0), xytext=(cx, cy),
                   fontsize=8, ha='center' if cx > 0 else 'center',
                   arrowprops=dict(arrowstyle='->', color='gray', lw=1,
                                  connectionstyle='arc3,rad=0.2'))

    # Legacy box
    ax.text(0, -2.5, 'Greenwich: Where space meets time\nThe zero point of global coordination',
            fontsize=9, ha='center', style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0',
                      edgecolor='gray'))

    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'greenwich-symbolism', chapter=24)


if __name__ == "__main__":
    meridian_offset_detail()
    deflection_of_vertical()
    time_ball()
    visitor_experience()
    greenwich_symbolism()
