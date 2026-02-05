#!/usr/bin/env python3
"""Generate figures for Chapter 17: The 1884 Meridian Conference."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Wedge, Rectangle
import numpy as np


def candidate_meridians():
    """Map showing the candidate prime meridians.

    Shows Greenwich, Paris, Washington, Ferro, and Atlantic meridians.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 5))

    # Simple world outline (very simplified)
    # Europe/Africa
    ax.fill([-10, 40, 40, -10], [35, 35, 70, 70], color='#d4c4a8', alpha=0.5)
    ax.fill([-20, 50, 50, -20], [-35, -35, 35, 35], color='#d4c4a8', alpha=0.5)

    # Americas
    ax.fill([-130, -60, -60, -130], [15, 15, 70, 70], color='#d4c4a8', alpha=0.5)
    ax.fill([-80, -35, -35, -80], [-55, -55, 15, 15], color='#d4c4a8', alpha=0.5)

    # Asia
    ax.fill([40, 150, 150, 40], [0, 0, 70, 70], color='#d4c4a8', alpha=0.5)

    # Candidate meridians
    meridians = [
        (0, 'Greenwich', '#1f77b4', 'solid', 3),
        (2.33, 'Paris', '#ff7f0e', 'dashed', 2),
        (-77, 'Washington', '#2ca02c', 'dashed', 2),
        (-18, 'Ferro', '#9467bd', 'dotted', 2),
        (-30, 'Atlantic\n(neutral)', '#d62728', 'dotted', 2),
    ]

    for lon, name, color, style, lw in meridians:
        ax.axvline(lon, color=color, linestyle=style, linewidth=lw, alpha=0.8)
        y_pos = 75 if lon > -50 else 75
        ax.text(lon, y_pos, name, fontsize=8, ha='center', color=color,
                rotation=90 if len(name) > 10 else 0)

    # Mark cities
    cities = [
        (0, 51.5, 'London'),
        (2.33, 48.9, 'Paris'),
        (-77, 38.9, 'Washington'),
    ]

    for lon, lat, name in cities:
        ax.plot(lon, lat, 'ko', markersize=6)
        ax.text(lon + 5, lat, name, fontsize=7, va='center')

    # Ocean labels
    ax.text(-45, 30, 'Atlantic\nOcean', fontsize=9, ha='center',
            color='#4169E1', alpha=0.7)
    ax.text(80, 30, 'Indian\nOcean', fontsize=9, ha='center',
            color='#4169E1', alpha=0.7)

    ax.set_xlim(-140, 160)
    ax.set_ylim(-60, 85)
    ax.set_xlabel('Longitude', fontsize=10)
    ax.set_ylabel('Latitude', fontsize=10)
    ax.grid(True, alpha=0.3)

    # Legend
    handles = [mpatches.Patch(color=m[2], label=m[1]) for m in meridians[:3]]
    ax.legend(handles=handles, loc='lower left', fontsize=8)

    plt.tight_layout()
    save_figure(fig, 'candidate-meridians', chapter=17)


def conference_vote():
    """Visualization of the 1884 conference vote."""
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    categories = ['In Favor', 'Against', 'Abstained']
    values = [22, 1, 2]
    colors = ['#2ca02c', '#d62728', '#ff7f0e']

    bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=1)

    # Value labels
    for bar, val in zip(bars, values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.5,
                str(val), ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Nations labels
    labels = [
        '22 nations\n(incl. Britain,\nGermany, USA)',
        'San Domingo',
        'France, Brazil'
    ]
    for bar, label in zip(bars, labels):
        ax.text(bar.get_x() + bar.get_width()/2, -2,
                label, ha='center', va='top', fontsize=7)

    ax.set_ylabel('Number of Nations', fontsize=10)
    ax.set_ylim(-4, 26)
    ax.set_title('Vote on Greenwich as Prime Meridian\nOctober 13, 1884', fontsize=11)

    plt.tight_layout()
    save_figure(fig, 'conference-vote', chapter=17)


def time_zones():
    """Diagram showing the 15-degree time zone concept."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 4))

    # Draw simplified Earth as rectangle (Mercator-like)
    # Time zone bands
    colors = plt.cm.RdYlBu(np.linspace(0, 1, 24))

    for i in range(-12, 12):
        lon_start = i * 15
        lon_end = (i + 1) * 15
        color = colors[i + 12]
        ax.fill([lon_start, lon_end, lon_end, lon_start],
                [-60, -60, 60, 60], color=color, alpha=0.5)
        ax.axvline(lon_start, color='gray', linewidth=0.5, alpha=0.5)

        # Zone labels
        if -180 < lon_start < 180:
            offset = i
            sign = '+' if offset >= 0 else ''
            ax.text((lon_start + lon_end) / 2, 65,
                    f'UTC{sign}{offset}', fontsize=6, ha='center', rotation=90)

    # Greenwich meridian (bold)
    ax.axvline(0, color='black', linewidth=3)
    ax.text(0, 75, 'Greenwich\n(UTC+0)', fontsize=9, ha='center', fontweight='bold')

    # Example cities
    cities = [
        (-75, 40, 'New York\nUTC-5'),
        (0, 51, 'London\nUTC+0'),
        (139, 36, 'Tokyo\nUTC+9'),
    ]

    for lon, lat, name in cities:
        ax.plot(lon, lat, 'ko', markersize=6)
        ax.text(lon, lat - 15, name, fontsize=7, ha='center')

    # 15 degree annotation
    ax.annotate('', xy=(15, -70), xytext=(0, -70),
                arrowprops=dict(arrowstyle='<->', color='black', lw=2))
    ax.text(7.5, -78, '15° = 1 hour', fontsize=9, ha='center')

    ax.set_xlim(-180, 180)
    ax.set_ylim(-85, 85)
    ax.set_xlabel('Longitude (degrees)', fontsize=10)
    ax.set_xticks([-180, -90, 0, 90, 180])

    plt.tight_layout()
    save_figure(fig, 'time-zones', chapter=17)


def adoption_timeline():
    """Timeline showing adoption of Greenwich meridian by various nations."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 4))

    events = [
        (1850, 'UK Railways begin\nusing Greenwich', '#1f77b4'),
        (1884, 'Meridian\nConference', '#d62728'),
        (1883, 'US Railways adopt\n4 time zones', '#2ca02c'),
        (1900, 'Germany adopts\nGreenwich', '#ff7f0e'),
        (1911, 'France adopts\nGreenwich', '#9467bd'),
        (1960, 'Universal\nadoption', '#8c564b'),
    ]

    # Timeline
    ax.axhline(1, color='black', linewidth=2)

    for year, label, color in events:
        ax.plot(year, 1, 'o', color=color, markersize=12, zorder=5)
        ax.plot([year, year], [1, 1.8], '-', color=color, linewidth=1)
        ax.text(year, 1.9, label, fontsize=7, ha='center', va='bottom',
                color=color)
        ax.text(year, 0.7, str(year), fontsize=8, ha='center')

    # Highlight conference
    ax.axvline(1884, color='red', linestyle='--', linewidth=1, alpha=0.5)

    ax.set_xlim(1840, 1970)
    ax.set_ylim(0, 3)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_yticks([])

    ax.set_title('Adoption of Greenwich as Prime Meridian', fontsize=11)

    plt.tight_layout()
    save_figure(fig, 'adoption-timeline', chapter=17)


def meridian_offset():
    """Diagram showing the 102m offset between Airy and WGS84."""
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    # Ground representation
    ax.axhline(0, color='#8B4513', linewidth=3)
    ax.fill_between([-150, 150], [-20, -20], [0, 0], color='#d4c4a8', alpha=0.5)

    # Airy meridian (tourist brass line)
    ax.axvline(0, color='#B8860B', linewidth=6)
    ax.text(0, 50, "Airy's\nTransit Circle\n(1884)", fontsize=9, ha='center',
            color='#B8860B', fontweight='bold')

    # WGS84 meridian
    ax.axvline(102, color='#1f77b4', linewidth=4, linestyle='--')
    ax.text(102, 50, 'WGS84\nMeridian\n(GPS)', fontsize=9, ha='center',
            color='#1f77b4', fontweight='bold')

    # Distance arrow
    ax.annotate('', xy=(102, -10), xytext=(0, -10),
                arrowprops=dict(arrowstyle='<->', color='green', lw=2))
    ax.text(51, -15, '102 meters', fontsize=10, ha='center', color='green',
            fontweight='bold')

    # Tourists
    for x in [-20, 0, 20]:
        ax.plot(x, 5, 'o', color='#ff7f0e', markersize=6)
    ax.text(0, 15, 'Tourists', fontsize=8, ha='center', color='#ff7f0e')

    ax.set_xlim(-80, 180)
    ax.set_ylim(-25, 70)
    ax.set_xlabel('Distance from brass line (meters)', fontsize=10)
    ax.set_yticks([])
    ax.set_aspect('equal')

    plt.tight_layout()
    save_figure(fig, 'meridian-offset', chapter=17)


if __name__ == "__main__":
    candidate_meridians()
    conference_vote()
    time_zones()
    adoption_timeline()
    meridian_offset()
