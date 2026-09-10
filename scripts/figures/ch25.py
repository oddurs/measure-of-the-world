#!/usr/bin/env python3
"""Generate figures for Chapter 25: Lessons for Science and Society."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Wedge, Polygon, Arrow, RegularPolygon
import numpy as np


def precision_evolution():
    """Evolution of positional precision from ancient to modern times."""
    setup_style()
    fig, ax = plt.subplots(figsize=(6.12, 3.42))

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

    # The first three points sit close together on both axes, so their captions
    # alternate side and are pushed off centre rather than stacked.
    placement = {
        1600: ('center', 'bottom', 0, 1.6),
        1675: ('left', 'bottom', 14, 1.3),
        1750: ('left', 'top', 14, 0.75),
        1850: ('center', 'top', 0, 0.42),
    }
    for year, prec, label, color in data:
        ax.semilogy(year, prec, 'o', color=color, markersize=12, zorder=5)
        ha, va, dx, factor = placement.get(
            year, ('center', 'bottom' if prec > 1 else 'top',
                   0, 1.5 if prec > 1 else 0.7))
        ax.text(year + dx, prec * factor, f'{label}\n({prec}\")', fontsize=7,
                ha=ha, va=va, color=color)

    # Reference lines
    ax.axhline(1, color='gray', linestyle='--', alpha=0.5)
    ax.text(1580, 1.2, '1 arcsecond', fontsize=7, color='gray')

    ax.axhline(1/3600, color='gray', linestyle='--', alpha=0.5)
    ax.text(1580, 1/3600 * 1.3, '1 milliarcsecond', fontsize=7, color='gray')

    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Positional Precision (arcseconds)', fontsize=10)
    ax.set_title('Four Centuries of Improving Precision', fontsize=11)
    ax.set_xlim(1550, 2050)
    ax.set_ylim(1e-6, 900)
    ax.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    save_figure(fig, 'precision-evolution', chapter=25)


def patronage_models():
    """Different models of scientific patronage through history."""
    setup_style()
    fig, ax = plt.subplots(figsize=(6.48, 4.05))

    # Timeline base
    ax.axhline(2, color='black', linewidth=2, xmin=0.05, xmax=0.95)

    # Eras
    # The shortest era carries the longest name, so the captions sit above the
    # bands, with the last one raised clear of its neighbour.
    eras = [
        (1675, 1850, 'Royal Patronage', '#9467bd', 3.25),
        (1850, 1950, 'Imperial Science', '#1f77b4', 3.25),
        (1950, 2020, 'Government Funding', '#2ca02c', 3.85),
    ]

    for start, end, label, color, y in eras:
        width = end - start
        ax.add_patch(Rectangle((start, 2.1), width, 1,
                                facecolor=color, edgecolor='black', alpha=0.7))
        ax.plot([(start + end) / 2, (start + end) / 2], [3.1, y - 0.04],
                '-', color=color, linewidth=0.8)
        ax.text((start + end) / 2, y, label, fontsize=8, ha='center',
                va='bottom', color=color, fontweight='bold')

    # Key events
    events = [
        (1675, 'Charles II\nfounds RGO', '#9467bd'),
        (1767, 'Nautical\nAlmanac', '#9467bd'),
        (1884, 'Meridian\nConference', '#1f77b4'),
        (1957, 'Move to\nHerstmonceux', '#2ca02c'),
        (1998, 'RGO\ncloses', '#d62728'),
    ]

    row_edges = [1650.0, 1650.0]
    for year, label, color in events:
        row = 0 if year - 22 >= row_edges[0] else 1
        row_edges[row] = year + 22
        text_y = 1.0 - 1.25 * row
        ax.plot(year, 2, 'o', color=color, markersize=10, zorder=5)
        ax.plot([year, year], [2, text_y + 0.06], '-', color=color, linewidth=1)
        ax.text(year, text_y, label, fontsize=7, ha='center', va='top',
                color=color)
        ax.text(year, text_y - 0.70, str(year), fontsize=7, ha='center',
                va='top', color='gray')

    # Lessons box
    lessons = ('Key Lessons:\n'
               '• Long-term vision requires stable funding\n'
               '• Navigation needs drove practical astronomy\n'
               '• International cooperation superseded competition')
    ax.text(1850, 5.7, lessons, fontsize=8, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0',
                      edgecolor='gray'))

    ax.set_xlim(1650, 2030)
    ax.set_ylim(-1.5, 5.9)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_yticks([])

    plt.tight_layout()
    save_figure(fig, 'patronage-models', chapter=25)


def standards_infrastructure():
    """The invisible infrastructure of global standards."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7.12, 5.32))

    # Layers of standards (pyramid)
    layers = [
        ('SI Units (meter, second, kilogram)', '#003366', 0),
        ('Geodetic Reference (WGS84, ITRF)', '#004d99', 1),
        ('Time Standards (UTC, TAI)', '#0066cc', 2),
        ('Navigation (GPS, GLONASS, Galileo)', '#3399ff', 3),
        ('Applications (Aviation, Maritime, Finance)', '#66b3ff', 4),
    ]

    # The narrowest layer carries the longest caption, so the pyramid is wide
    # and shallow: the top course still has to hold 42 characters.
    pyramid_base = 9
    layer_height = 0.8

    for label, color, level in layers:
        # Trapezoid shape
        shrink = level * 0.32
        bottom_left = -pyramid_base/2 + shrink
        bottom_right = pyramid_base/2 - shrink
        top_shrink = (level + 1) * 0.32
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
    ax.annotate('Greenwich\ncontributions', xy=(-3.5, 2.2), xytext=(-5.1, 2.9),
                fontsize=8, ha='left', va='center',
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                color='red')

    # Arrows showing dependencies
    ax.annotate('', xy=(4.9, 0.4), xytext=(4.9, 3.6),
                arrowprops=dict(arrowstyle='<-', color='black', lw=2))
    ax.text(5.1, 2, 'Depends\non', fontsize=8, ha='left', va='center')

    ax.set_xlim(-5.2, 6.4)
    ax.set_ylim(-0.5, 4.3)
    # No equal aspect: the courses are a schematic stack, not a measured shape,
    # and squaring them shrinks every caption below the print floor.
    ax.axis('off')

    save_figure(fig, 'standards-infrastructure', chapter=25)


def international_cooperation():
    """Timeline of international scientific cooperation."""
    setup_style()
    fig, ax = plt.subplots(figsize=(6.08, 2.66))

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
    ax.text(1950, 0.02, 'Increasing global coordination', fontsize=9,
            ha='center', va='top', color='green', alpha=0.7)

    ax.set_xlim(1850, 2030)
    ax.set_ylim(-0.5, 3)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_yticks([])
    ax.set_title('From National to International Standards', fontsize=11)

    plt.tight_layout()
    save_figure(fig, 'international-cooperation', chapter=25)


def greenwich_legacy():
    """Summary diagram of Greenwich's enduring legacy."""
    setup_style()
    # Taller than wide-ish: every node caption is set inside its circle, so the
    # circles have to be big enough to hold two lines of eight point type.
    fig, ax = plt.subplots(figsize=(7.31, 6.37))

    # Central circle - Greenwich
    ax.add_patch(Circle((0, 0), 1.25, facecolor='#003366', edgecolor='black',
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
        x = 3.25 * np.cos(rad)
        y = 3.25 * np.sin(rad)
        ax.add_patch(Circle((x, y), 1.16, facecolor='#ff7f0e', edgecolor='black',
                            alpha=0.8))
        ax.text(x, y, label, fontsize=7, ha='center', va='center',
                fontweight='bold')

        # Connection line
        x1 = 1.32 * np.cos(rad)
        y1 = 1.32 * np.sin(rad)
        x2 = 2.05 * np.cos(rad)
        y2 = 2.05 * np.sin(rad)
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
        x = 5.20 * np.cos(rad)
        y = 5.20 * np.sin(rad)
        # A hexagon, not a circle: the historical/modern distinction has to
        # survive a greyscale printing, and shape does where hue does not.
        ax.add_patch(RegularPolygon((x, y), numVertices=6, radius=0.86,
                                    orientation=np.radians(30),
                                    facecolor=color, edgecolor='black',
                                    linewidth=1.2, alpha=0.35))
        ax.text(x, y, label, fontsize=7, ha='center', va='center',
                color='black', fontweight='bold')


    ax.set_xlim(-6.2, 6.2)
    ax.set_ylim(-4.7, 6.2)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'greenwich-legacy', chapter=25)


if __name__ == "__main__":
    precision_evolution()
    patronage_models()
    standards_infrastructure()
    international_cooperation()
    greenwich_legacy()
