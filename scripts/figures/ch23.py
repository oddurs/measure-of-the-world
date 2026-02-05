#!/usr/bin/env python3
"""Generate figures for Chapter 23: Light Pollution and the Move to Herstmonceux."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Wedge, Polygon
import numpy as np


def skyglow_physics():
    """Diagram showing how light pollution creates skyglow."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 5))

    # Ground
    ax.fill([-4, 4, 4, -4], [0, 0, -0.5, -0.5], color='#2d2d2d')

    # City buildings
    buildings = [
        (-3, 0.8), (-2.5, 1.2), (-2, 0.6), (-1.5, 1.5), (-1, 0.9),
        (1, 1.1), (1.5, 0.7), (2, 1.3), (2.5, 0.8), (3, 1.0)
    ]
    for x, h in buildings:
        ax.add_patch(Rectangle((x-0.2, 0), 0.4, h, facecolor='#4a4a4a',
                                edgecolor='black'))

    # Street lights
    light_positions = [-2.5, -1, 0, 1.5, 2.5]
    for lx in light_positions:
        # Light fixture
        ax.plot([lx, lx], [0, 0.4], 'k-', linewidth=2)
        ax.add_patch(Circle((lx, 0.45), 0.08, facecolor='#FFD700', edgecolor='black'))

        # Light rays going up (the problem)
        for angle in range(60, 121, 15):
            dx = 0.8 * np.cos(np.radians(angle))
            dy = 0.8 * np.sin(np.radians(angle))
            ax.annotate('', xy=(lx+dx, 0.45+dy), xytext=(lx, 0.45),
                       arrowprops=dict(arrowstyle='-', color='yellow',
                                      lw=1, alpha=0.6))

    # Atmosphere layer with scattering
    for y in np.linspace(1.5, 3.5, 8):
        alpha = 0.15 * (1 - (y - 1.5) / 2.5)
        ax.fill([-4, 4, 4, -4], [y, y, y+0.3, y+0.3],
                color='#FFA500', alpha=alpha)

    # Scattered light indication
    ax.text(0, 2.5, 'Light scattered by\natmospheric particles',
            fontsize=8, ha='center', color='orange', alpha=0.8)

    # Stars (dimmed by skyglow)
    np.random.seed(42)
    for _ in range(15):
        sx = np.random.uniform(-3.5, 3.5)
        sy = np.random.uniform(3.5, 4.5)
        size = np.random.uniform(2, 5)
        alpha = np.random.uniform(0.3, 0.6)  # Dimmed
        ax.plot(sx, sy, '*', color='white', markersize=size, alpha=alpha)

    ax.text(0, 4.7, 'Stars obscured by skyglow', fontsize=9, ha='center',
            color='white')

    # Dark sky (gradient effect)
    ax.set_facecolor('#1a1a3a')

    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-0.5, 5)
    ax.axis('off')

    save_figure(fig, 'skyglow-physics', chapter=23)


def limiting_magnitude():
    """Chart showing limiting magnitude vs sky brightness."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    # Sky brightness (mag/arcsec^2)
    sky_brightness = np.array([22, 21, 20, 19, 18, 17, 16])
    limiting_mag = np.array([6.5, 6.0, 5.5, 5.0, 4.5, 4.0, 3.5])

    # Locations on the scale
    locations = [
        (22, 'Dark site (Bortle 1)', '#006400'),
        (21, 'Rural (Bortle 3)', '#228B22'),
        (20, 'Suburban (Bortle 5)', '#FFD700'),
        (19, 'Urban (Bortle 7)', '#FFA500'),
        (18, 'City center (Bortle 9)', '#FF4500'),
        (17, 'Greenwich 1950s', '#FF0000'),
    ]

    # Plot the relationship
    ax.plot(sky_brightness, limiting_mag, 'b-', linewidth=2, marker='o', markersize=8)

    # Add location markers
    for sky, label, color in locations:
        lim = np.interp(sky, sky_brightness[::-1], limiting_mag[::-1])
        ax.plot(sky, lim, 'o', color=color, markersize=12, zorder=5)
        ha = 'left' if sky > 19 else 'right'
        offset = 0.3 if sky > 19 else -0.3
        ax.annotate(label, xy=(sky, lim), xytext=(sky+offset, lim+0.2),
                   fontsize=7, ha=ha, color=color,
                   arrowprops=dict(arrowstyle='-', color=color, lw=0.5))

    # Reference lines
    ax.axhline(6.0, color='green', linestyle='--', alpha=0.5, linewidth=1)
    ax.text(16.2, 6.1, 'Naked-eye limit\n(dark sky)', fontsize=7, ha='left',
            color='green')

    ax.axhline(4.0, color='red', linestyle='--', alpha=0.5, linewidth=1)
    ax.text(16.2, 4.1, 'Only bright stars\nvisible', fontsize=7, ha='left',
            color='red')

    ax.set_xlabel('Sky Brightness (mag/arcsec²)', fontsize=10)
    ax.set_ylabel('Limiting Magnitude (naked eye)', fontsize=10)
    ax.set_title('Light Pollution Effect on Star Visibility', fontsize=11)

    ax.invert_xaxis()  # Brighter sky = smaller number
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    save_figure(fig, 'limiting-magnitude', chapter=23)


def observatory_migration():
    """Timeline showing observatory moves to escape light pollution."""
    setup_style()
    fig, ax = plt.subplots(figsize=(9, 4))

    # Timeline
    ax.axhline(1.5, color='black', linewidth=2, xmin=0.05, xmax=0.95)

    events = [
        (1675, 'Greenwich\nfounded', '#1f77b4', 'above'),
        (1884, 'Prime Meridian\nestablished', '#2ca02c', 'below'),
        (1948, 'Light pollution\nproblematic', '#ff7f0e', 'above'),
        (1957, 'Move to\nHerstmonceux', '#d62728', 'below'),
        (1979, 'Isaac Newton Tel.\nto La Palma', '#9467bd', 'above'),
        (1990, 'All telescopes\nto Canaries', '#8c564b', 'below'),
    ]

    for year, label, color, pos in events:
        y_marker = 1.5
        y_text = 2.2 if pos == 'above' else 0.8
        y_line = 1.9 if pos == 'above' else 1.1

        ax.plot(year, y_marker, 'o', color=color, markersize=12, zorder=5)
        ax.plot([year, year], [y_marker, y_line], '-', color=color, linewidth=1)
        ax.text(year, y_text, label, fontsize=7, ha='center',
                va='bottom' if pos == 'above' else 'top', color=color)
        ax.text(year, y_marker - 0.3 if pos == 'above' else y_marker + 0.3,
                str(year), fontsize=7, ha='center', color='gray')

    # Light pollution growth indication
    x_pollution = np.linspace(1900, 1990, 50)
    y_pollution = 0.5 + 0.5 * (1 - np.exp(-(x_pollution - 1900) / 30))
    ax.fill_between(x_pollution, 0, y_pollution, color='orange', alpha=0.3)
    ax.text(1945, 0.25, 'Growing light\npollution', fontsize=7, ha='center',
            color='orange', alpha=0.8)

    ax.set_xlim(1650, 2010)
    ax.set_ylim(0, 3)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_yticks([])

    ax.set_title('Royal Observatory Migration from Light Pollution', fontsize=11)

    plt.tight_layout()
    save_figure(fig, 'observatory-migration', chapter=23)


def herstmonceux_site():
    """Comparison of Greenwich and Herstmonceux sites."""
    setup_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Greenwich (polluted)
    ax1.set_title('Greenwich (1950s)', fontsize=11, fontweight='bold')
    ax1.set_facecolor('#3a3a4a')

    # London skyline
    for x in np.linspace(-3, 3, 15):
        h = np.random.uniform(0.5, 1.5)
        ax1.add_patch(Rectangle((x-0.15, 0), 0.3, h, facecolor='#2a2a2a',
                                 edgecolor='black'))
        # Lit windows
        for wy in np.arange(0.2, h, 0.25):
            if np.random.random() > 0.3:
                ax1.plot(x, wy, 's', color='yellow', markersize=2)

    # Skyglow dome
    theta = np.linspace(0, np.pi, 50)
    r = 2
    x_dome = r * np.cos(theta)
    y_dome = r * np.sin(theta) + 0.5
    ax1.fill(np.append(x_dome, x_dome[0]), np.append(y_dome, 0.5),
             color='#FFA500', alpha=0.3)

    # Few visible stars
    for _ in range(5):
        ax1.plot(np.random.uniform(-3, 3), np.random.uniform(2, 3),
                '*', color='white', markersize=3, alpha=0.5)

    ax1.text(0, 3.3, 'Heavy skyglow\nFew stars visible', fontsize=8, ha='center',
             color='orange')

    ax1.set_xlim(-4, 4)
    ax1.set_ylim(0, 3.7)
    ax1.axis('off')

    # Herstmonceux (dark)
    ax2.set_title('Herstmonceux (1958)', fontsize=11, fontweight='bold')
    ax2.set_facecolor('#0a0a1a')

    # Rural landscape
    ax2.fill([-4, 4, 4, -4], [0, 0, 0.3, 0.3], color='#1a3a1a')

    # Castle silhouette
    castle_x = [-1, -1, -0.8, -0.8, -0.5, -0.5, 0, 0, 0.5, 0.5, 0.8, 0.8, 1, 1]
    castle_y = [0, 0.8, 0.8, 1.2, 1.2, 0.8, 0.8, 1.0, 1.0, 0.8, 0.8, 1.2, 1.2, 0]
    ax2.fill(castle_x, castle_y, color='#1a1a1a', edgecolor='black')

    # Telescope dome
    ax2.add_patch(Wedge((2.5, 0.3), 0.5, 0, 180, facecolor='#3a3a3a',
                        edgecolor='black'))

    # Many visible stars
    np.random.seed(123)
    for _ in range(50):
        ax2.plot(np.random.uniform(-3.5, 3.5), np.random.uniform(0.8, 3.5),
                '*', color='white', markersize=np.random.uniform(1, 4))

    # Milky Way suggestion
    for _ in range(100):
        mx = np.random.uniform(-1, 1) + np.random.uniform(-3.5, 3.5) * 0.1
        my = np.random.uniform(1.5, 3)
        ax2.plot(mx, my, '.', color='white', markersize=0.5, alpha=0.3)

    ax2.text(0, 3.5, 'Dark skies\nMilky Way visible', fontsize=8, ha='center',
             color='#add8e6')

    ax2.set_xlim(-4, 4)
    ax2.set_ylim(0, 3.7)
    ax2.axis('off')

    plt.tight_layout()
    save_figure(fig, 'site-comparison', chapter=23)


def canary_islands_sites():
    """Map showing modern observatory sites in the Canary Islands."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    # Simplified map of Canary Islands
    # La Palma
    la_palma = np.array([[-17.9, 28.9], [-17.7, 28.85], [-17.75, 28.7],
                         [-17.95, 28.65], [-18.0, 28.75], [-17.9, 28.9]])
    ax.fill(la_palma[:, 0], la_palma[:, 1], color='#8B4513', edgecolor='black')
    ax.text(-17.85, 28.78, 'La Palma', fontsize=8, ha='center', color='white',
            fontweight='bold')

    # Tenerife
    tenerife = np.array([[-16.9, 28.55], [-16.1, 28.45], [-16.2, 28.0],
                         [-16.95, 28.1], [-16.9, 28.55]])
    ax.fill(tenerife[:, 0], tenerife[:, 1], color='#8B4513', edgecolor='black')
    ax.text(-16.5, 28.25, 'Tenerife', fontsize=8, ha='center', color='white')

    # Observatory locations
    obs_sites = [
        (-17.88, 28.76, 'Roque de los Muchachos\n(2426m)', '#1f77b4'),
        (-16.51, 28.30, 'Teide Observatory\n(2390m)', '#ff7f0e'),
    ]

    for lon, lat, name, color in obs_sites:
        ax.plot(lon, lat, '*', color=color, markersize=15, markeredgecolor='black')
        ax.text(lon + 0.15, lat, name, fontsize=7, ha='left', va='center', color=color)

    # UK connection
    ax.annotate('', xy=(-17.88, 28.76), xytext=(-15.5, 29.5),
                arrowprops=dict(arrowstyle='<-', color='blue', lw=2,
                               connectionstyle='arc3,rad=-0.2'))
    ax.text(-15.5, 29.6, 'Isaac Newton\nTelescope (1984)', fontsize=8, ha='center',
            color='blue')

    # Inset: Why these sites are good
    info_box = ('Advantages:\n'
                '• Above inversion layer\n'
                '• Stable atmosphere\n'
                '• Low light pollution\n'
                '• 300+ clear nights/year')
    ax.text(-16.0, 27.8, info_box, fontsize=7, ha='left',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='gray', alpha=0.9))

    # Ocean
    ax.set_facecolor('#4169E1')
    ax.text(-17.0, 29.3, 'Atlantic Ocean', fontsize=9, ha='center',
            color='white', alpha=0.7)

    ax.set_xlim(-18.3, -15.3)
    ax.set_ylim(27.5, 29.7)
    ax.set_xlabel('Longitude', fontsize=10)
    ax.set_ylabel('Latitude', fontsize=10)

    save_figure(fig, 'canary-islands-sites', chapter=23)


if __name__ == "__main__":
    skyglow_physics()
    limiting_magnitude()
    observatory_migration()
    herstmonceux_site()
    canary_islands_sites()
