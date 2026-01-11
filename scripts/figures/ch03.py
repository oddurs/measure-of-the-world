#!/usr/bin/env python3
"""Generate figures for Chapter 3: Instruments and Methods of the Observatory."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Arc
import numpy as np


def celestial_coordinates():
    """Diagram of the celestial coordinate system.

    Shows right ascension (RA) measured along the celestial equator
    and declination (Dec) measured north/south from it.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 6))

    # Draw celestial sphere as a circle
    theta = np.linspace(0, 2 * np.pi, 100)
    r = 1.0
    ax.plot(r * np.cos(theta), r * np.sin(theta), 'k-', linewidth=1.5)

    # Celestial equator (ellipse to show 3D perspective)
    eq_theta = np.linspace(0, 2 * np.pi, 100)
    eq_a = 1.0  # semi-major axis
    eq_b = 0.3  # semi-minor axis (perspective)
    ax.plot(eq_a * np.cos(eq_theta), eq_b * np.sin(eq_theta), 'k-', linewidth=1.2)
    ax.text(1.05, 0.0, 'Celestial\nEquator', fontsize=8, ha='left', va='center')

    # North celestial pole
    ax.plot(0, 1, 'ko', markersize=6)
    ax.text(0.08, 1.0, 'North\nCelestial Pole', fontsize=8, ha='left', va='center')

    # South celestial pole
    ax.plot(0, -1, 'ko', markersize=4)
    ax.text(0.08, -1.0, 'South\nCelestial Pole', fontsize=8, ha='left', va='center')

    # Vernal equinox point (on the equator, right side)
    ve_x, ve_y = 1.0, 0.0
    ax.plot(ve_x, ve_y, 'k*', markersize=10)
    ax.text(1.12, 0.15, 'Vernal\nEquinox', fontsize=8, ha='left', va='bottom',
            style='italic')

    # A sample star position
    star_ra = 45  # degrees from vernal equinox
    star_dec = 35  # degrees north of equator

    # Calculate star position on sphere (simplified 2D projection)
    star_ra_rad = np.radians(star_ra)
    star_dec_rad = np.radians(star_dec)
    # Project onto our view
    star_x = np.cos(star_dec_rad) * np.cos(star_ra_rad)
    star_y = np.sin(star_dec_rad)
    ax.plot(star_x, star_y, '*', color='#1f77b4', markersize=15)
    ax.text(star_x + 0.08, star_y + 0.05, 'Star', fontsize=9, color='#1f77b4')

    # Right ascension arc (along equator from vernal equinox)
    ra_arc_theta = np.linspace(0, star_ra_rad, 30)
    ra_arc_r = 0.5
    ra_arc_x = ra_arc_r * np.cos(ra_arc_theta)
    ra_arc_y = ra_arc_r * 0.3 * np.sin(ra_arc_theta)  # Perspective
    ax.plot(ra_arc_x, ra_arc_y, '-', color='#2ca02c', linewidth=2)
    ax.annotate('', xy=(ra_arc_x[-1], ra_arc_y[-1]),
                xytext=(ra_arc_x[-2], ra_arc_y[-2]),
                arrowprops=dict(arrowstyle='->', color='#2ca02c', lw=1.5))
    ax.text(0.55, -0.12, 'Right Ascension', fontsize=9, color='#2ca02c',
            ha='center', rotation=-5)

    # Declination arc (from equator to star, along meridian)
    # Draw a vertical arc from the equator point to the star
    eq_point_x = np.cos(star_ra_rad)
    eq_point_y = 0.3 * np.sin(star_ra_rad)  # On the equator ellipse

    # Simple vertical line for declination
    dec_line_y = np.linspace(eq_point_y, star_y, 20)
    dec_line_x = np.linspace(eq_point_x, star_x, 20)
    ax.plot(dec_line_x, dec_line_y, '-', color='#d62728', linewidth=2)
    ax.annotate('', xy=(star_x, star_y - 0.05),
                xytext=(star_x, star_y - 0.15),
                arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.5))
    ax.text(star_x + 0.12, (eq_point_y + star_y) / 2, 'Declination',
            fontsize=9, color='#d62728', ha='left', va='center', rotation=70)

    # Reference lines (hour circles - meridians)
    for ra in [0, 90, 180, 270]:
        ra_rad = np.radians(ra)
        x = np.cos(ra_rad)
        y_eq = 0.3 * np.sin(ra_rad)
        ax.plot([0, x], [1, y_eq], 'k:', linewidth=0.5, alpha=0.3)
        ax.plot([0, x], [-1, y_eq], 'k:', linewidth=0.5, alpha=0.3)

    # Legend box
    ax.text(0, -1.4,
            r'RA: measured eastward from vernal equinox (0h to 24h)' + '\n' +
            r'Dec: measured from equator ($-90°$ to $+90°$)',
            fontsize=8, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-1.4, 1.5)
    ax.set_ylim(-1.6, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'celestial-coordinates', chapter=3)


def atmospheric_refraction():
    """Diagram showing atmospheric refraction effect on star observations.

    Light from a star bends as it passes through Earth's atmosphere,
    making stars appear higher than they actually are.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    # Earth's surface (curved)
    earth_theta = np.linspace(-0.3, 0.3, 100)
    earth_r = 2.0
    earth_x = earth_r * np.sin(earth_theta)
    earth_y = earth_r * np.cos(earth_theta) - earth_r + 0.2
    ax.fill_between(earth_x, earth_y, -0.5, color='#8B7355', alpha=0.6)
    ax.plot(earth_x, earth_y, 'k-', linewidth=1.5)

    # Atmosphere layers (gradient)
    for i, (height, alpha) in enumerate([(0.3, 0.15), (0.6, 0.10), (0.9, 0.05)]):
        atm_y = earth_y + height
        ax.fill_between(earth_x, earth_y + (i * 0.3), atm_y,
                        color='#87CEEB', alpha=alpha)

    ax.text(-0.55, 0.5, 'Atmosphere', fontsize=8, color='#4682B4',
            ha='center', rotation=90)

    # Observer
    obs_x, obs_y = 0, 0.22
    ax.plot(obs_x, obs_y, 'ko', markersize=8)
    ax.text(obs_x + 0.05, obs_y - 0.08, 'Observer', fontsize=8, ha='left')

    # True star position (outside atmosphere)
    true_star_x, true_star_y = 0.8, 1.5
    ax.plot(true_star_x, true_star_y, '*', color='#1f77b4', markersize=12)
    ax.text(true_star_x + 0.05, true_star_y, 'True position', fontsize=8,
            color='#1f77b4', ha='left')

    # Apparent star position (higher)
    app_star_x, app_star_y = 0.65, 1.6
    ax.plot(app_star_x, app_star_y, '*', color='#d62728', markersize=12,
            alpha=0.6)
    ax.text(app_star_x - 0.05, app_star_y + 0.05, 'Apparent\nposition',
            fontsize=8, color='#d62728', ha='right')

    # Light path - bent through atmosphere
    # From true star to top of atmosphere
    atm_top_y = 1.1
    entry_x = 0.45
    ax.plot([true_star_x, entry_x], [true_star_y, atm_top_y],
            'k--', linewidth=1, alpha=0.7)

    # Through atmosphere (bent) to observer
    ax.plot([entry_x, obs_x], [atm_top_y, obs_y],
            '#1f77b4', linewidth=1.5)

    # Observer's line of sight (extended straight)
    ax.plot([obs_x, app_star_x], [obs_y, app_star_y],
            '#d62728', linewidth=1.5, linestyle='--')

    # Angle annotations
    # True altitude
    ax.annotate('', xy=(0.4, 0.22), xytext=(0.0, 0.22),
                arrowprops=dict(arrowstyle='-', color='gray', lw=0.8))
    ax.text(0.25, 0.35, r'$h_{true}$', fontsize=10, ha='center')

    # Apparent altitude
    ax.text(0.15, 0.55, r'$h_{apparent}$', fontsize=10, ha='center',
            color='#d62728')

    # Refraction angle
    ax.annotate('', xy=(0.55, 1.3), xytext=(0.7, 1.4),
                arrowprops=dict(arrowstyle='<->', color='#2ca02c', lw=1.2))
    ax.text(0.75, 1.25, r'$R$', fontsize=11, color='#2ca02c')

    # Caption
    ax.text(0, -0.35,
            r'Refraction $R = h_{apparent} - h_{true}$' + '\n' +
            r'Effect increases near horizon (up to $\sim35$ arcmin)',
            fontsize=8, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-0.7, 1.1)
    ax.set_ylim(-0.5, 1.8)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'atmospheric-refraction', chapter=3)


def instrument_precision():
    """Relationship between instrument radius and achievable precision.

    Larger instruments allow finer scale divisions while remaining readable.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    # Instrument radii (feet)
    radii = np.array([1, 2, 3, 4, 5, 6, 7, 8])

    # Theoretical precision (arc-seconds) - inversely proportional to radius
    # Assuming minimum readable division of ~0.1mm, converted to arc-seconds
    # For a 1-foot radius: circumference = 2*pi*12 inches = ~75 inches
    # 90 degrees = 75/4 = ~19 inches of arc
    # 1 arc-minute = 19/90 = ~0.21 inches = ~5.3mm
    # Minimum readable: ~0.1mm = ~1.1 arc-seconds at 1 foot

    # Simplified model: precision proportional to 60/radius (arc-seconds)
    precision = 60 / radii  # arc-seconds achievable

    # Historical data points
    hist_radii = [6, 7]  # Tycho ~6ft, Flamsteed ~7ft
    hist_precision = [60, 15]  # Tycho ~1', Flamsteed ~15"
    hist_names = ['Tycho\n(Uraniborg)', 'Flamsteed\n(Greenwich)']

    # Plot theoretical curve
    radii_smooth = np.linspace(0.5, 8.5, 100)
    precision_smooth = 60 / radii_smooth
    ax.plot(radii_smooth, precision_smooth, 'k-', linewidth=1.5, alpha=0.5,
            label='Theoretical limit')

    # Plot historical points
    colors = ['#ff7f0e', '#1f77b4']
    for r, p, name, col in zip(hist_radii, hist_precision, hist_names, colors):
        ax.plot(r, p, 'o', markersize=10, color=col)
        ax.annotate(name, xy=(r, p), xytext=(r + 0.3, p + 5),
                    fontsize=9, color=col, ha='left')

    # Reference lines
    ax.axhline(y=60, color='gray', linestyle=':', linewidth=0.8, alpha=0.5)
    ax.text(0.7, 63, "1 arc-minute", fontsize=8, color='gray')

    ax.axhline(y=20, color='gray', linestyle=':', linewidth=0.8, alpha=0.5)
    ax.text(0.7, 23, "20 arc-seconds", fontsize=8, color='gray')

    ax.set_xlabel('Instrument radius (feet)')
    ax.set_ylabel('Achievable precision (arc-seconds)')
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 100)
    ax.grid(True, alpha=0.3)

    # Note about other factors
    ax.text(4.5, 85, 'Other factors: telescope use,\nclock timing, observer skill',
            fontsize=8, ha='center', style='italic', color='#555555')

    save_figure(fig, 'instrument-precision', chapter=3)


if __name__ == "__main__":
    celestial_coordinates()
    atmospheric_refraction()
    instrument_precision()
