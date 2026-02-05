#!/usr/bin/env python3
"""Generate figures for Chapter 19: The Quadrant and Sextant."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Arc, Wedge, FancyArrowPatch
import numpy as np


def double_reflection():
    """Diagram showing the double-reflection principle.

    Rotating mirror by theta rotates reflected ray by 2*theta.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    # Index mirror
    mirror1_x, mirror1_y = 0, 0
    mirror1_angle = 30  # degrees from vertical
    mirror_len = 1
    dx = mirror_len * np.sin(np.radians(mirror1_angle)) / 2
    dy = mirror_len * np.cos(np.radians(mirror1_angle)) / 2
    ax.plot([mirror1_x - dx, mirror1_x + dx],
            [mirror1_y - dy, mirror1_y + dy], 'b-', linewidth=4)
    ax.text(-0.3, 0.7, 'Index\nmirror', fontsize=8, ha='center', color='blue')

    # Horizon mirror
    mirror2_x, mirror2_y = 2.5, 0
    ax.plot([mirror2_x, mirror2_x], [-0.5, 0.5], 'g-', linewidth=4)
    ax.text(2.7, 0.7, 'Horizon\nmirror', fontsize=8, ha='left', color='green')

    # Incoming ray (from star)
    star_x, star_y = -2, 1.5
    ax.annotate('', xy=(mirror1_x - dx*0.8, mirror1_y + dy*0.8),
                xytext=(star_x, star_y),
                arrowprops=dict(arrowstyle='->', color='orange', lw=2))
    ax.text(star_x - 0.2, star_y + 0.2, 'From star', fontsize=8, ha='right', color='orange')

    # Reflected ray to horizon mirror
    ax.annotate('', xy=(mirror2_x - 0.1, 0),
                xytext=(mirror1_x + dx*0.5, mirror1_y - dy*0.5),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))

    # Final reflected ray (to observer eye)
    ax.annotate('', xy=(4, -0.8),
                xytext=(mirror2_x + 0.1, 0),
                arrowprops=dict(arrowstyle='->', color='purple', lw=2))
    ax.text(4.2, -0.8, 'To eye', fontsize=8, ha='left', color='purple')

    # Angle annotation at index mirror
    arc1 = Arc((mirror1_x, mirror1_y), 0.8, 0.8, angle=0,
               theta1=90-mirror1_angle, theta2=90+20, color='blue', linewidth=1.5)
    ax.add_patch(arc1)
    ax.text(-0.5, 0.2, r'$\theta$', fontsize=10, color='blue')

    # Result annotation
    ax.text(1.5, -1.5, r'Mirror rotates $\theta$ $\rightarrow$ Ray rotates $2\theta$' + '\n'
            r'60$^\circ$ arc measures up to 120$^\circ$',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-3, 5)
    ax.set_ylim(-2, 2.5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'double-reflection', chapter=19)


def sextant_components():
    """Labeled diagram of sextant components."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 6))

    # Frame (pie-slice shape)
    frame_theta = np.linspace(0, np.radians(60), 50)
    frame_r = 3
    frame_x = frame_r * np.cos(frame_theta)
    frame_y = frame_r * np.sin(frame_theta)
    ax.plot(frame_x, frame_y, 'k-', linewidth=3)
    ax.plot([0, frame_x[0]], [0, frame_y[0]], 'k-', linewidth=3)
    ax.plot([0, frame_x[-1]], [0, frame_y[-1]], 'k-', linewidth=3)
    ax.fill(np.concatenate([[0], frame_x, [0]]),
            np.concatenate([[0], frame_y, [0]]),
            color='#c0c0c0', alpha=0.3)

    # Arc graduations
    for deg in range(0, 61, 10):
        angle = np.radians(deg)
        x_inner = 2.6 * np.cos(angle)
        y_inner = 2.6 * np.sin(angle)
        x_outer = 3 * np.cos(angle)
        y_outer = 3 * np.sin(angle)
        ax.plot([x_inner, x_outer], [y_inner, y_outer], 'k-', linewidth=1)
        ax.text(3.2 * np.cos(angle), 3.2 * np.sin(angle),
                f'{deg*2}', fontsize=7, ha='center', va='center')

    ax.text(3.5 * np.cos(np.radians(30)), 3.5 * np.sin(np.radians(30)),
            'Arc\n(graduated)', fontsize=8, ha='center', color='gray')

    # Index arm
    index_angle = np.radians(25)
    ax.plot([0, 2.8*np.cos(index_angle)], [0, 2.8*np.sin(index_angle)],
            'b-', linewidth=3)
    ax.text(1.5*np.cos(index_angle) + 0.3, 1.5*np.sin(index_angle) + 0.3,
            'Index arm', fontsize=8, ha='left', color='blue')

    # Index mirror
    mirror_x = 0.8 * np.cos(index_angle)
    mirror_y = 0.8 * np.sin(index_angle)
    ax.add_patch(Rectangle((mirror_x - 0.15, mirror_y - 0.2), 0.3, 0.4,
                            angle=np.degrees(index_angle), facecolor='#87CEEB',
                            edgecolor='black', linewidth=1))
    ax.annotate('Index mirror', xy=(mirror_x, mirror_y),
                xytext=(mirror_x - 0.8, mirror_y + 0.8),
                fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

    # Horizon mirror
    hz_x, hz_y = 2.5, 0.3
    ax.add_patch(Rectangle((hz_x - 0.1, hz_y - 0.25), 0.2, 0.5,
                            facecolor='#87CEEB', edgecolor='black', linewidth=1))
    ax.annotate('Horizon mirror\n(half-silvered)', xy=(hz_x, hz_y),
                xytext=(hz_x + 0.7, hz_y + 0.8),
                fontsize=8, ha='left',
                arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

    # Telescope
    ax.plot([2.3, 3.5], [0.3, 0.3], 'k-', linewidth=5)
    ax.add_patch(Circle((3.5, 0.3), 0.15, facecolor='black'))
    ax.text(3.7, 0.3, 'Telescope', fontsize=8, ha='left', va='center')

    # Shades
    for i in range(3):
        shade_x = 1.5 + i * 0.15
        ax.add_patch(Rectangle((shade_x, 0.6), 0.1, 0.4,
                                facecolor='#8B0000', alpha=0.5,
                                edgecolor='black', linewidth=0.5))
    ax.text(1.65, 1.2, 'Shades', fontsize=8, ha='center')

    # Drum/vernier
    drum_x = 2.8 * np.cos(index_angle)
    drum_y = 2.8 * np.sin(index_angle)
    ax.add_patch(Circle((drum_x, drum_y), 0.15, facecolor='#ffd700',
                         edgecolor='black', linewidth=1))
    ax.annotate('Micrometer\ndrum', xy=(drum_x, drum_y),
                xytext=(drum_x + 0.5, drum_y + 0.6),
                fontsize=8, ha='left',
                arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

    # Pivot point
    ax.add_patch(Circle((0, 0), 0.08, facecolor='black'))
    ax.text(-0.3, -0.2, 'Pivot', fontsize=8, ha='right')

    # Handle
    ax.plot([-0.3, -0.3], [-0.5, -1.5], 'k-', linewidth=8)
    ax.text(-0.5, -1, 'Handle', fontsize=8, ha='right', va='center')

    ax.set_xlim(-1.5, 4.5)
    ax.set_ylim(-2, 4)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'sextant-components', chapter=19)


def vernier_scale():
    """How the vernier scale allows precise angle reading."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 3))

    # Main scale
    main_start = 0
    main_spacing = 0.5  # represents 1 degree
    for i in range(12):
        x = main_start + i * main_spacing
        ax.plot([x, x], [1.5, 2], 'k-', linewidth=2)
        if i % 2 == 0:
            ax.text(x, 2.1, f'{47 + i//2}', fontsize=8, ha='center')

    ax.plot([main_start - 0.2, main_start + 11 * main_spacing + 0.2],
            [1.5, 1.5], 'k-', linewidth=2)
    ax.text(-0.5, 1.75, 'Main scale\n(degrees)', fontsize=8, ha='right')

    # Vernier scale (shifted to show reading)
    vernier_offset = 0.35  # position on main scale
    vernier_spacing = main_spacing * 9 / 10  # 9 main divisions = 10 vernier
    for i in range(11):
        x = vernier_offset + i * vernier_spacing
        ax.plot([x, x], [0.8, 1.3], 'b-', linewidth=1.5)
        ax.text(x, 0.6, str(i), fontsize=6, ha='center', color='blue')

    ax.plot([vernier_offset - 0.1, vernier_offset + 10 * vernier_spacing + 0.1],
            [1.3, 1.3], 'b-', linewidth=2)
    ax.text(-0.5, 1.05, 'Vernier scale\n(minutes)', fontsize=8, ha='right', color='blue')

    # Highlight alignment
    align_idx = 4  # 4th vernier mark aligns with a main scale mark
    align_x = vernier_offset + align_idx * vernier_spacing
    ax.add_patch(Rectangle((align_x - 0.08, 0.75), 0.16, 1.3,
                            facecolor='green', alpha=0.3))
    ax.annotate('Alignment here\n= 4 minutes', xy=(align_x, 0.5),
                xytext=(align_x + 1, 0.2),
                fontsize=8, ha='left', color='green',
                arrowprops=dict(arrowstyle='->', color='green', lw=1))

    # Index mark
    ax.plot([vernier_offset, vernier_offset], [1.4, 1.6], 'r-', linewidth=3)
    ax.annotate('Index mark\nat 47.X degrees', xy=(vernier_offset, 1.5),
                xytext=(vernier_offset - 0.5, 2.5),
                fontsize=8, ha='center', color='red',
                arrowprops=dict(arrowstyle='->', color='red', lw=1))

    # Result
    ax.text(3, -0.3, "Reading: 47\u00b0 04'", fontsize=10, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0',
                      edgecolor='black'))

    ax.set_xlim(-1.5, 6)
    ax.set_ylim(-0.8, 3)
    ax.axis('off')

    save_figure(fig, 'vernier-scale', chapter=19)


def sextant_errors():
    """Error sources in sextant observation."""
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 5))

    errors = [
        ('Reading error', 30, 'Random, reduces with averaging'),
        ('Horizon definition', 60, 'Haze, waves, observer height'),
        ('Index error', 75, 'Correctable with calibration'),
        ('Refraction', 30, 'Tables provide correction'),
        ('Instrument errors', 45, 'Arc, perpendicularity, centering'),
    ]

    y_positions = np.arange(len(errors))
    values = [e[1] for e in errors]
    labels = [e[0] for e in errors]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

    bars = ax.barh(y_positions, values, color=colors, edgecolor='black', linewidth=0.5)

    ax.set_yticks(y_positions)
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel('Error magnitude (arcseconds)', fontsize=10)
    ax.set_xlim(0, 100)

    # Notes
    for i, (name, val, note) in enumerate(errors):
        ax.text(val + 2, i, f'{val}"', fontsize=8, va='center')

    # Total RSS
    total_rss = np.sqrt(sum(v**2 for v in values))
    ax.axvline(total_rss, color='red', linestyle='--', linewidth=2)
    ax.text(total_rss + 2, len(errors) - 0.5, f'Total (RSS)\n{total_rss:.0f}"',
            fontsize=8, color='red', va='center')

    ax.grid(True, axis='x', alpha=0.3)

    plt.tight_layout()
    save_figure(fig, 'sextant-errors', chapter=19)


def sextant_evolution():
    """Evolution of sextant precision 1731-1900."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 4))

    years = [1731, 1760, 1780, 1810, 1850, 1900]
    precision = [120, 60, 60, 30, 30, 15]  # arcseconds
    labels = ['Hadley\noctant', 'Ramsden\ntelescope', 'Troughton\nvernier',
              'Drum\nmicrometer', 'Dividing\nengine', 'Standardized\ndesign']

    ax.semilogy(years, precision, 'b-o', linewidth=2, markersize=8)

    for year, prec, label in zip(years, precision, labels):
        ax.annotate(label, xy=(year, prec),
                    xytext=(year, prec * 1.5),
                    fontsize=7, ha='center', va='bottom')

    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Typical precision (arcseconds)', fontsize=10)
    ax.set_xlim(1720, 1920)
    ax.set_ylim(10, 200)
    ax.grid(True, alpha=0.3)

    # Reference line
    ax.axhline(60, color='gray', linestyle=':', linewidth=1, alpha=0.7)
    ax.text(1720, 65, "1' (1 nautical mile)", fontsize=7, color='gray')

    plt.tight_layout()
    save_figure(fig, 'sextant-evolution', chapter=19)


def altitude_observation():
    """Diagram showing altitude observation at sea."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    # Horizon
    ax.axhline(0, color='#4169E1', linewidth=3)
    ax.fill_between([-4, 4], [-1, -1], [0, 0], color='#4169E1', alpha=0.3)
    ax.text(-3.5, -0.5, 'Sea', fontsize=9, color='#4169E1')

    # Sun
    sun = Circle((2, 2.5), 0.4, facecolor='#FFD700', edgecolor='#FFA500', linewidth=2)
    ax.add_patch(sun)
    ax.text(2, 3.2, 'Sun', fontsize=9, ha='center')

    # Observer
    obs_x, obs_y = -2, 0.5
    ax.plot(obs_x, obs_y, 'ko', markersize=10)
    ax.plot([obs_x, obs_x], [0, obs_y], 'k-', linewidth=3)
    ax.text(obs_x, -0.3, 'Observer', fontsize=8, ha='center')

    # Sextant (simplified)
    sext_x, sext_y = obs_x + 0.3, obs_y + 0.3
    ax.plot([sext_x, sext_x + 0.8], [sext_y, sext_y], 'k-', linewidth=4)

    # Line to horizon
    ax.plot([sext_x + 0.8, 4], [sext_y, 0], 'g--', linewidth=1.5, alpha=0.7)
    ax.text(1, 0.2, 'Direct view\nof horizon', fontsize=7, ha='center', color='green')

    # Line to sun (reflected)
    ax.plot([sext_x + 0.4, 2], [sext_y + 0.1, 2.1], 'r--', linewidth=1.5, alpha=0.7)
    ax.text(0, 1.5, 'Reflected\nSun image', fontsize=7, ha='center', color='red')

    # Altitude angle
    arc = Arc((sext_x + 0.8, sext_y), 2, 2, angle=0, theta1=-10, theta2=40,
              color='purple', linewidth=2)
    ax.add_patch(arc)
    ax.text(0.5, 0.8, r'Altitude $h$', fontsize=10, color='purple')

    # View through telescope
    inset_ax = fig.add_axes([0.65, 0.55, 0.25, 0.35])
    inset_ax.set_xlim(-1, 1)
    inset_ax.set_ylim(-1, 1)
    inset_ax.set_aspect('equal')

    # Circular view
    circle = Circle((0, 0), 0.9, fill=False, edgecolor='black', linewidth=2)
    inset_ax.add_patch(circle)

    # Horizon line in view
    inset_ax.axhline(-0.3, color='#4169E1', linewidth=2)

    # Sun image touching horizon
    sun_view = Circle((0, -0.1), 0.2, facecolor='#FFD700', edgecolor='#FFA500')
    inset_ax.add_patch(sun_view)

    inset_ax.text(0, 0.6, 'Eyepiece view', fontsize=7, ha='center')
    inset_ax.axis('off')

    ax.set_xlim(-4, 4)
    ax.set_ylim(-1.2, 4)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'altitude-observation', chapter=19)


if __name__ == "__main__":
    double_reflection()
    sextant_components()
    vernier_scale()
    sextant_errors()
    sextant_evolution()
    altitude_observation()
