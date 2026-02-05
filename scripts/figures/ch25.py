#!/usr/bin/env python3
"""Generate figures for Chapter 25: Lessons for Science and Society."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Wedge, Polygon, Arrow
import numpy as np


def precision_evolution():
    """Evolution of positional precision from ancient to modern times."""
    setup_style()
    fig, ax = plt.subplots(figsize=(9, 5))

    # Data: (year, precision in arcseconds, method, color)
    data = [
        (1600, 60, 'Naked eye', '#d62728'),
        (1675, 10, 'Early telescopes', '#ff7f0e'),
        (1750, 2, 'Improved optics', '#2ca02c'),
        (1850, 0.3, 'Transit circles', '#1f77b4'),
        (1950, 0.05, 'Photographic', '#9467bd'),
        (2000, 0.001, 'CCD + satellites', '#17becf'),
        (2020, 0.00001, 'VLBI / Gaia', '#bcbd22'),
    ]

    years = [d[0] for d in data]
    precision = [d[1] for d in data]
    labels = [d[2] for d in data]
    colors = [d[3] for d in data]

    # Log scale for precision
    ax.semilogy(years, precision, 'k-', linewidth=2, marker='o', markersize=10)

    for year, prec, label, color in data:
        ax.semilogy(year, prec, 'o', color=color, markersize=12, zorder=5)
        va = 'bottom' if prec > 1 else 'top'
        offset = 1.5 if prec > 1 else 0.7
        ax.text(year, prec * offset if va == 'bottom' else prec / offset,
                f'{label}\n({prec}\")', fontsize=7, ha='center', va=va, color=color)

    # Reference lines
    ax.axhline(1, color='gray', linestyle='--', alpha=0.5)
    ax.text(1580, 1.2, '1 arcsecond', fontsize=7, color='gray')

    ax.axhline(1/3600, color='gray', linestyle='--', alpha=0.5)
    ax.text(1580, 1/3600 * 1.3, '1 milliarcsecond', fontsize=7, color='gray')

    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Positional Precision (arcseconds)', fontsize=10)
    ax.set_title('Four Centuries of Improving Precision', fontsize=11)
    ax.set_xlim(1550, 2050)
    ax.set_ylim(1e-6, 200)
    ax.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    save_figure(fig, 'precision-evolution', chapter=25)


def patronage_models():
    """Different models of scientific patronage through history."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 5))

    # Timeline base
    ax.axhline(2, color='black', linewidth=2, xmin=0.05, xmax=0.95)

    # Eras
    eras = [
        (1675, 1850, 'Royal Patronage', '#9467bd', 3.5),
        (1850, 1950, 'Imperial Science', '#1f77b4', 3.5),
        (1950, 2020, 'Government Funding', '#2ca02c', 3.5),
    ]

    for start, end, label, color, y in eras:
        width = end - start
        ax.add_patch(Rectangle((start, 2.1), width, 1,
                                facecolor=color, edgecolor='black', alpha=0.7))
        ax.text((start + end) / 2, 2.6, label, fontsize=8, ha='center',
                va='center', color='white', fontweight='bold')

    # Key events
    events = [
        (1675, 'Charles II\nfounds RGO', '#9467bd'),
        (1767, 'Nautical\nAlmanac', '#9467bd'),
        (1884, 'Meridian\nConference', '#1f77b4'),
        (1957, 'Move to\nHerstmonceux', '#2ca02c'),
        (1998, 'RGO\ncloses', '#d62728'),
    ]

    for year, label, color in events:
        ax.plot(year, 2, 'o', color=color, markersize=10, zorder=5)
        ax.plot([year, year], [2, 1.3], '-', color=color, linewidth=1)
        ax.text(year, 1.0, label, fontsize=7, ha='center', va='top', color=color)
        ax.text(year, 0.4, str(year), fontsize=7, ha='center', color='gray')

    # Lessons box
    lessons = ('Key Lessons:\n'
               '• Long-term vision requires stable funding\n'
               '• Navigation needs drove practical astronomy\n'
               '• International cooperation superseded competition')
    ax.text(1850, 4.5, lessons, fontsize=8, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0',
                      edgecolor='gray'))

    ax.set_xlim(1650, 2030)
    ax.set_ylim(0, 5)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_yticks([])

    plt.tight_layout()
    save_figure(fig, 'patronage-models', chapter=25)


def standards_infrastructure():
    """The invisible infrastructure of global standards."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 6))

    # Layers of standards (pyramid)
    layers = [
        ('SI Units (meter, second, kilogram)', '#003366', 0),
        ('Geodetic Reference (WGS84, ITRF)', '#004d99', 1),
        ('Time Standards (UTC, TAI)', '#0066cc', 2),
        ('Navigation (GPS, GLONASS, Galileo)', '#3399ff', 3),
        ('Applications (Aviation, Maritime, Finance)', '#66b3ff', 4),
    ]

    pyramid_base = 6
    layer_height = 0.8

    for label, color, level in layers:
        # Trapezoid shape
        shrink = level * 0.4
        bottom_left = -pyramid_base/2 + shrink
        bottom_right = pyramid_base/2 - shrink
        top_shrink = (level + 1) * 0.4
        top_left = -pyramid_base/2 + top_shrink
        top_right = pyramid_base/2 - top_shrink

        y_bottom = level * layer_height
        y_top = (level + 1) * layer_height

        vertices = [(bottom_left, y_bottom), (bottom_right, y_bottom),
                    (top_right, y_top), (top_left, y_top)]
        ax.add_patch(Polygon(vertices, facecolor=color, edgecolor='black',
                            linewidth=1))

        ax.text(0, (y_bottom + y_top) / 2, label, fontsize=8, ha='center',
                va='center', color='white', fontweight='bold')

    # Greenwich connection
    ax.annotate('Greenwich\ncontributions', xy=(0, 2), xytext=(-4, 3),
                fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                color='red')

    # Arrows showing dependencies
    ax.annotate('', xy=(3.5, 0.4), xytext=(3.5, 3.6),
                arrowprops=dict(arrowstyle='<-', color='black', lw=2))
    ax.text(4, 2, 'Depends\non', fontsize=8, ha='left', va='center')

    ax.set_xlim(-5, 5)
    ax.set_ylim(-0.5, 5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'standards-infrastructure', chapter=25)


def international_cooperation():
    """Timeline of international scientific cooperation."""
    setup_style()
    fig, ax = plt.subplots(figsize=(9, 4))

    # Timeline
    ax.axhline(1.5, color='black', linewidth=2, xmin=0.03, xmax=0.97)

    organizations = [
        (1875, 'Metre\nConvention', '#1f77b4'),
        (1884, 'Meridian\nConference', '#ff7f0e'),
        (1919, 'IAU\nfounded', '#2ca02c'),
        (1955, 'UTC\nagreement', '#d62728'),
        (1988, 'GPS\ncivilian', '#9467bd'),
        (2016, 'SI\nredefined', '#8c564b'),
    ]

    for i, (year, label, color) in enumerate(organizations):
        y_pos = 2.3 if i % 2 == 0 else 0.7
        line_end = 1.9 if i % 2 == 0 else 1.1

        ax.plot(year, 1.5, 'o', color=color, markersize=12, zorder=5)
        ax.plot([year, year], [1.5, line_end], '-', color=color, linewidth=1.5)
        ax.text(year, y_pos, label, fontsize=7, ha='center',
                va='bottom' if i % 2 == 0 else 'top', color=color)
        ax.text(year, 1.5 - 0.2 if i % 2 == 0 else 1.5 + 0.2,
                str(year), fontsize=7, ha='center',
                va='top' if i % 2 == 0 else 'bottom', color='gray')

    # Trend arrow
    ax.annotate('', xy=(2020, 1.5), xytext=(1870, 1.5),
                arrowprops=dict(arrowstyle='->', color='green', lw=3, alpha=0.3))
    ax.text(1950, 0.2, 'Increasing global coordination', fontsize=9,
            ha='center', color='green', alpha=0.7)

    ax.set_xlim(1850, 2030)
    ax.set_ylim(0, 3)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_yticks([])
    ax.set_title('From National to International Standards', fontsize=11)

    plt.tight_layout()
    save_figure(fig, 'international-cooperation', chapter=25)


def greenwich_legacy():
    """Summary diagram of Greenwich's enduring legacy."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 6))

    # Central circle - Greenwich
    ax.add_patch(Circle((0, 0), 1, facecolor='#003366', edgecolor='black',
                        linewidth=2))
    ax.text(0, 0, 'Greenwich\nObservatory\n(1675-1998)', fontsize=9, ha='center',
            va='center', color='white', fontweight='bold')

    # Radiating achievements
    achievements = [
        (45, 'Prime Meridian\n(0° longitude)'),
        (90, 'Universal Time\n(GMT → UTC)'),
        (135, 'Nautical\nAlmanac'),
        (180, 'Star\nCatalogues'),
        (225, 'Navigation\nTables'),
        (270, 'Time Ball\nService'),
        (315, 'Transit\nInstruments'),
        (0, 'Precision\nStandards'),
    ]

    for angle, label in achievements:
        rad = np.radians(angle)
        # Outer circle for achievement
        x = 2.5 * np.cos(rad)
        y = 2.5 * np.sin(rad)
        ax.add_patch(Circle((x, y), 0.6, facecolor='#ff7f0e', edgecolor='black',
                            alpha=0.8))
        ax.text(x, y, label, fontsize=6, ha='center', va='center',
                fontweight='bold')

        # Connection line
        x1 = 1.1 * np.cos(rad)
        y1 = 1.1 * np.sin(rad)
        x2 = 1.9 * np.cos(rad)
        y2 = 1.9 * np.sin(rad)
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1.5)

    # Modern continuations (outer ring)
    modern = [
        (22.5, 'GPS', '#2ca02c'),
        (67.5, 'Atomic\nClocks', '#2ca02c'),
        (112.5, 'VLBI', '#2ca02c'),
        (157.5, 'Space\nGeodesy', '#2ca02c'),
    ]

    for angle, label, color in modern:
        rad = np.radians(angle)
        x = 3.8 * np.cos(rad)
        y = 3.8 * np.sin(rad)
        ax.add_patch(Circle((x, y), 0.45, facecolor=color, edgecolor='black',
                            alpha=0.7))
        ax.text(x, y, label, fontsize=6, ha='center', va='center',
                color='white', fontweight='bold')

        # Dashed line from achievement to modern
        x1 = 3.1 * np.cos(rad)
        y1 = 3.1 * np.sin(rad)
        x2 = 3.35 * np.cos(rad)
        y2 = 3.35 * np.sin(rad)
        ax.plot([x1, x2], [y1, y2], 'g--', linewidth=1)

    # Legend
    ax.text(0, -4.2, 'Orange: Historical achievements    Green: Modern continuations',
            fontsize=8, ha='center')

    ax.set_xlim(-4.8, 4.8)
    ax.set_ylim(-4.6, 4.6)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'greenwich-legacy', chapter=25)


if __name__ == "__main__":
    precision_evolution()
    patronage_models()
    standards_infrastructure()
    international_cooperation()
    greenwich_legacy()
