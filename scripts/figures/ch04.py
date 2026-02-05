#!/usr/bin/env python3
"""Generate figures for Chapter 4: The Mural Arc and the Method of Transits."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


def transit_geometry():
    """Diagram showing the geometry of meridian transit observations.

    Illustrates how right ascension equals local sidereal time at the
    moment a star crosses the meridian.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 5))

    # Draw celestial sphere outline
    theta = np.linspace(0, 2 * np.pi, 100)
    ax.plot(np.cos(theta), np.sin(theta), 'k-', linewidth=1)

    # Celestial equator (tilted ellipse)
    eq_a, eq_b = 1.0, 0.35
    ax.plot(eq_a * np.cos(theta), eq_b * np.sin(theta), 'k-', linewidth=1.2)
    ax.text(1.05, 0.05, 'Celestial\nequator', fontsize=7, ha='left', va='center')

    # Meridian plane (vertical line through center)
    ax.plot([0, 0], [-1, 1], 'b-', linewidth=2, label='Meridian')
    ax.text(0.08, 0.85, 'Meridian', fontsize=8, color='blue', ha='left')

    # Celestial pole (top)
    ax.plot(0, 1, 'ko', markersize=5)
    ax.text(0.08, 1.0, 'NCP', fontsize=8, ha='left')

    # Zenith
    ax.plot(0, 0.7, 'k^', markersize=6)
    ax.text(0.08, 0.7, 'Zenith', fontsize=8, ha='left')

    # Observer at center
    ax.plot(0, 0, 'ko', markersize=4)

    # Star path (arc across the sky, east to west)
    star_dec = 30  # degrees
    dec_rad = np.radians(star_dec)
    # Path is a circle at constant declination
    path_theta = np.linspace(-0.8, 0.8, 50)
    path_y = np.sin(dec_rad) + 0.1  # offset for visibility
    path_x = 0.6 * np.sin(path_theta)
    path_y_vals = path_y + 0.15 * np.cos(path_theta)
    ax.plot(path_x, path_y_vals, 'gray', linewidth=1.5, linestyle='--')

    # Arrow showing direction of motion (east to west)
    ax.annotate('', xy=(-0.3, path_y + 0.1), xytext=(0.3, path_y + 0.1),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1))
    ax.text(0, path_y + 0.22, 'Star path (E to W)', fontsize=7, ha='center',
            color='gray')

    # Star at transit (on meridian)
    star_x, star_y = 0, path_y + 0.15
    ax.plot(star_x, star_y, '*', color='#1f77b4', markersize=14)
    ax.text(0.1, star_y, 'Star at\ntransit', fontsize=8, ha='left',
            color='#1f77b4')

    # Vernal equinox point on celestial equator
    ve_angle = -60  # degrees from meridian
    ve_rad = np.radians(ve_angle)
    ve_x = eq_a * np.cos(ve_rad)
    ve_y = eq_b * np.sin(ve_rad)
    ax.plot(ve_x, ve_y, 'g*', markersize=10)
    ax.text(ve_x - 0.1, ve_y - 0.12, 'Vernal\nequinox', fontsize=7,
            ha='center', color='green')

    # Arc showing right ascension (from vernal equinox to star's meridian)
    ra_arc = np.linspace(ve_rad, 0, 30)
    ra_r = 0.5
    ax.plot(ra_r * np.cos(ra_arc), ra_r * eq_b/eq_a * np.sin(ra_arc),
            'g-', linewidth=2)
    ax.text(0.35, -0.05, r'RA = $\alpha$', fontsize=9, color='green')

    # Key equation box
    ax.text(0, -0.85, r'At transit: $\alpha_{star} = \alpha_{LST}$' + '\n' +
            r'(Right Ascension = Local Sidereal Time)',
            fontsize=9, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor='#cccccc'))

    # Horizon line
    ax.plot([-1.1, 1.1], [-0.5, -0.5], 'k-', linewidth=0.8, alpha=0.5)
    ax.text(1.0, -0.55, 'Horizon', fontsize=7, ha='right', color='gray')

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.0, 1.15)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'transit-geometry', chapter=4)


def error_budget():
    """Bar chart showing the error budget for transit observations.

    Shows both right ascension and declination error sources.
    """
    setup_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 4))

    # Right ascension errors
    ra_sources = ['Clock drift', 'Reaction time']
    ra_errors = [10, 7.5]  # arcseconds (midpoint of ranges)
    ra_ranges = [(5, 15), (5, 10)]

    bars1 = ax1.barh(ra_sources, ra_errors, color='#1f77b4', edgecolor='black',
                     linewidth=0.5, height=0.5)
    # Add error bars for ranges
    for i, (low, high) in enumerate(ra_ranges):
        ax1.plot([low, high], [i, i], 'k-', linewidth=2)
        ax1.plot([low, low], [i-0.1, i+0.1], 'k-', linewidth=1.5)
        ax1.plot([high, high], [i-0.1, i+0.1], 'k-', linewidth=1.5)

    ax1.set_xlabel('Error (arcseconds)')
    ax1.set_title('Right Ascension', fontsize=10)
    ax1.set_xlim(0, 25)
    ax1.grid(True, axis='x', alpha=0.3)

    # Declination errors
    dec_sources = ['Refraction', 'Graduation', 'Flexure/collimation']
    dec_errors = [12.5, 7.5, 4]  # arcseconds (midpoint of ranges)
    dec_ranges = [(5, 20), (5, 10), (3, 5)]

    bars2 = ax2.barh(dec_sources, dec_errors, color='#ff7f0e', edgecolor='black',
                     linewidth=0.5, height=0.5)
    # Add error bars for ranges
    for i, (low, high) in enumerate(dec_ranges):
        ax2.plot([low, high], [i, i], 'k-', linewidth=2)
        ax2.plot([low, low], [i-0.1, i+0.1], 'k-', linewidth=1.5)
        ax2.plot([high, high], [i-0.1, i+0.1], 'k-', linewidth=1.5)

    ax2.set_xlabel('Error (arcseconds)')
    ax2.set_title('Declination', fontsize=10)
    ax2.set_xlim(0, 25)
    ax2.grid(True, axis='x', alpha=0.3)

    # Combined error note
    fig.text(0.5, 0.02, 'Combined typical error: 15-20 arcsec per observation; '
             '10 arcsec after averaging',
             ha='center', fontsize=8, style='italic')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15)

    save_figure(fig, 'error-budget', chapter=4)


def refraction_curve():
    """Plot of atmospheric refraction as a function of altitude.

    Shows how refraction increases dramatically near the horizon.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    # Altitude range (degrees)
    altitude = np.linspace(5, 90, 100)

    # Bessel's formula: R ≈ 58.3 * cot(h) arcseconds
    # cot(h) = 1/tan(h)
    refraction = 58.3 / np.tan(np.radians(altitude))

    ax.plot(altitude, refraction, 'k-', linewidth=1.5)

    # Mark key points
    key_alts = [10, 20, 45, 90]
    for alt in key_alts:
        ref = 58.3 / np.tan(np.radians(alt))
        ax.plot(alt, ref, 'ko', markersize=5)
        if alt == 90:
            ax.annotate(f'{alt}°: {ref:.0f}"', xy=(alt, ref),
                        xytext=(alt - 8, ref + 30), fontsize=8)
        elif alt == 10:
            ax.annotate(f'{alt}°: {ref:.0f}"', xy=(alt, ref),
                        xytext=(alt + 3, ref - 20), fontsize=8)
        else:
            ax.annotate(f'{alt}°: {ref:.0f}"', xy=(alt, ref),
                        xytext=(alt + 3, ref + 15), fontsize=8)

    # Shaded region for "danger zone" near horizon
    danger_alt = np.linspace(5, 20, 50)
    danger_ref = 58.3 / np.tan(np.radians(danger_alt))
    ax.fill_between(danger_alt, 0, danger_ref, alpha=0.2, color='red')
    ax.text(12, 200, 'High\nuncertainty', fontsize=8, color='red',
            ha='center', style='italic')

    # Preferred observation zone
    ax.axvspan(45, 90, alpha=0.1, color='green')
    ax.text(67, 200, 'Preferred\nobserving zone', fontsize=8, color='green',
            ha='center', style='italic')

    ax.set_xlabel('Altitude (degrees)')
    ax.set_ylabel('Refraction (arcseconds)')
    ax.set_xlim(0, 95)
    ax.set_ylim(0, 350)
    ax.grid(True, alpha=0.3)

    # Formula annotation
    ax.text(50, 300, r"Bessel's formula: $R \approx 58.3 \cot(h)$",
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    save_figure(fig, 'refraction-curve', chapter=4)


if __name__ == "__main__":
    transit_geometry()
    error_budget()
    refraction_curve()
