#!/usr/bin/env python3
"""Generate figures for Chapter 15: Mean Time and the Equation of Time."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch
import numpy as np


def equation_of_time_graph():
    """Graph showing the equation of time over a full year.

    Shows both components (eccentricity and obliquity) and total.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 5))

    # Calculate equation of time for each day
    days = np.arange(1, 366)

    # Orbital parameters
    e = 0.0167  # eccentricity
    epsilon = np.radians(23.44)  # obliquity

    # Mean anomaly (0 at perihelion, Jan 3)
    M = 2 * np.pi * (days - 3) / 365.25

    # Eccentricity component (in minutes)
    E_ecc = -2 * e * np.sin(M) * (24 * 60) / (2 * np.pi)

    # Obliquity component
    # Ecliptic longitude (simplified)
    L = 2 * np.pi * (days - 80) / 365.25  # 0 at vernal equinox (March 21)
    E_obliq = -np.tan(epsilon/2)**2 * np.sin(2 * L) * (24 * 60) / (2 * np.pi)

    # Total equation of time
    E_total = E_ecc + E_obliq

    # Plot
    ax.plot(days, E_ecc, 'b--', linewidth=1.5, alpha=0.7, label='Eccentricity effect')
    ax.plot(days, E_obliq, 'r--', linewidth=1.5, alpha=0.7, label='Obliquity effect')
    ax.plot(days, E_total, 'k-', linewidth=2, label='Total (Equation of Time)')

    # Zero line
    ax.axhline(0, color='gray', linestyle='-', linewidth=0.5)

    # Month labels
    month_starts = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ax.set_xticks(month_starts)
    ax.set_xticklabels(month_names, fontsize=8)

    # Mark extrema
    extrema = [
        (45, '+14.3 min', 'Feb 11'),
        (135, '-3.7 min', 'May 14'),
        (210, '+6.4 min', 'Jul 26'),
        (307, '-16.3 min', 'Nov 3'),
    ]

    for day, value, date in extrema:
        y = E_total[day-1]
        ax.plot(day, y, 'ko', markersize=6)
        offset = 1.5 if y > 0 else -1.5
        ax.annotate(f'{date}', xy=(day, y), xytext=(day, y + offset),
                    fontsize=7, ha='center')

    ax.set_xlabel('Day of Year', fontsize=10)
    ax.set_ylabel('Equation of Time (minutes)', fontsize=10)
    ax.set_xlim(0, 366)
    ax.set_ylim(-20, 20)
    ax.legend(loc='lower right', fontsize=9)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    save_figure(fig, 'equation-of-time', chapter=15)


def analemma():
    """The analemma - figure-8 pattern traced by the Sun.

    Shows position of Sun at same clock time throughout the year.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(5, 7))

    # Calculate analemma points
    days = np.arange(1, 366)

    # Orbital parameters
    e = 0.0167
    epsilon = np.radians(23.44)

    # Mean anomaly
    M = 2 * np.pi * (days - 3) / 365.25

    # Equation of time (x-axis, in degrees)
    L = 2 * np.pi * (days - 80) / 365.25
    E_ecc = -2 * e * np.sin(M)
    E_obliq = -np.tan(epsilon/2)**2 * np.sin(2 * L)
    E_total = (E_ecc + E_obliq) * (180 / np.pi)  # convert to degrees
    x = E_total * 4  # 4 minutes per degree of rotation

    # Declination (y-axis)
    decl = np.degrees(np.arcsin(np.sin(epsilon) * np.sin(L)))

    # Plot the analemma
    ax.plot(x, decl, 'b-', linewidth=2)

    # Mark solstices and equinoxes
    special_days = [
        (1, 'Jan 1', 'left'),
        (80, 'Mar 20', 'right'),
        (172, 'Jun 21', 'left'),
        (265, 'Sep 22', 'right'),
        (356, 'Dec 21', 'right'),
    ]

    for day, label, ha in special_days:
        ax.plot(x[day-1], decl[day-1], 'ro', markersize=8)
        offset = 0.5 if ha == 'left' else -0.5
        ax.annotate(label, xy=(x[day-1], decl[day-1]),
                    xytext=(x[day-1] + offset, decl[day-1] + 2),
                    fontsize=8, ha=ha,
                    arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

    # Labels
    ax.set_xlabel('Equation of Time (minutes)', fontsize=10)
    ax.set_ylabel('Solar Declination (degrees)', fontsize=10)

    # Add cardinal directions
    ax.text(0, 26, 'N', fontsize=10, ha='center', fontweight='bold')
    ax.text(0, -26, 'S', fontsize=10, ha='center', fontweight='bold')
    ax.text(20, 0, 'Sun early', fontsize=8, ha='right', color='gray')
    ax.text(-20, 0, 'Sun late', fontsize=8, ha='left', color='gray')

    ax.axhline(0, color='gray', linestyle='--', linewidth=0.5)
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.5)

    ax.set_xlim(-20, 20)
    ax.set_ylim(-28, 28)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')

    plt.tight_layout()
    save_figure(fig, 'analemma', chapter=15)


def eccentricity_effect():
    """Diagram showing how Earth's elliptical orbit causes the eccentricity effect.

    Shows faster motion at perihelion, slower at aphelion.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    # Earth's orbit (ellipse)
    a = 2.5  # semi-major axis (scaled)
    e = 0.4  # exaggerated eccentricity for visibility
    b = a * np.sqrt(1 - e**2)

    theta = np.linspace(0, 2*np.pi, 100)
    x_orbit = a * np.cos(theta) - a * e
    y_orbit = b * np.sin(theta)

    ax.plot(x_orbit, y_orbit, 'b-', linewidth=1.5)

    # Sun at focus
    sun = Circle((0, 0), 0.2, facecolor='#FFD700', edgecolor='black', linewidth=1.5)
    ax.add_patch(sun)
    ax.text(0, -0.45, 'Sun', fontsize=9, ha='center')

    # Earth at perihelion (closest)
    perihelion_x = a * (1 - e) - a * e
    earth_p = Circle((perihelion_x, 0), 0.12, facecolor='#1f77b4', edgecolor='black')
    ax.add_patch(earth_p)
    ax.text(perihelion_x, 0.3, 'Perihelion\n(Jan 3)', fontsize=8, ha='center')

    # Velocity arrow at perihelion (large)
    ax.annotate('', xy=(perihelion_x, 0.7), xytext=(perihelion_x, 0.15),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(perihelion_x + 0.3, 0.5, 'Fast', fontsize=8, color='red')

    # Earth at aphelion (farthest)
    aphelion_x = -a * (1 + e) - a * e
    earth_a = Circle((aphelion_x, 0), 0.12, facecolor='#1f77b4', edgecolor='black')
    ax.add_patch(earth_a)
    ax.text(aphelion_x, 0.3, 'Aphelion\n(Jul 4)', fontsize=8, ha='center')

    # Velocity arrow at aphelion (small)
    ax.annotate('', xy=(aphelion_x, 0.4), xytext=(aphelion_x, 0.15),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax.text(aphelion_x - 0.3, 0.35, 'Slow', fontsize=8, ha='right', color='blue')

    # Semi-major axis annotation
    ax.plot([0, a - a*e], [0.8, 0.8], 'k-', linewidth=1)
    ax.plot([0, 0], [0.75, 0.85], 'k-', linewidth=1)
    ax.plot([a - a*e, a - a*e], [0.75, 0.85], 'k-', linewidth=1)
    ax.text((a - a*e)/2, 0.95, 'a', fontsize=10, ha='center')

    # Note about effect
    ax.text(0, -2.2, 'Earth moves faster at perihelion,\nslower at aphelion\n' +
            r'($v^2 = GM(2/r - 1/a)$)',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-6, 3)
    ax.set_ylim(-2.8, 1.8)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'eccentricity-effect', chapter=15)


def obliquity_effect():
    """Diagram showing how the obliquity of the ecliptic affects the equation of time.

    Shows projection from ecliptic to equator.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    # Celestial sphere (simplified as circle)
    sphere = Circle((0, 0), 2, fill=False, edgecolor='black', linewidth=1.5)
    ax.add_patch(sphere)

    # Celestial equator (horizontal line)
    ax.plot([-2, 2], [0, 0], 'b-', linewidth=2, label='Celestial equator')

    # Ecliptic (tilted line)
    epsilon = np.radians(23.44)
    x_ecl = np.linspace(-2, 2, 100)
    y_ecl = x_ecl * np.tan(epsilon)

    # Clip to sphere
    mask = x_ecl**2 + y_ecl**2 <= 4
    ax.plot(x_ecl[mask], y_ecl[mask], 'r-', linewidth=2, label='Ecliptic')

    # Sun positions at different times
    sun_positions = [
        (0, 0, 'Equinox'),
        (1.5, 1.5 * np.tan(epsilon), 'Summer'),
        (-1.5, -1.5 * np.tan(epsilon), 'Winter'),
    ]

    for x, y, label in sun_positions:
        # Sun on ecliptic
        ax.plot(x, y, 'o', color='#FFD700', markersize=10,
                markeredgecolor='black')

        # Projection to equator
        ax.plot([x, x], [y, 0], 'g--', linewidth=1)
        ax.plot(x, 0, 'go', markersize=5)

        # Label
        offset = 0.2 if y >= 0 else -0.2
        ax.text(x, y + offset, label, fontsize=8, ha='center',
                va='bottom' if y >= 0 else 'top')

    # Obliquity angle
    arc_theta = np.linspace(0, epsilon, 20)
    arc_r = 0.8
    ax.plot(arc_r * np.cos(arc_theta), arc_r * np.sin(arc_theta), 'k-', linewidth=1)
    ax.text(0.7, 0.2, r'$\epsilon = 23.44°$', fontsize=9)

    # Movement arrows on ecliptic
    ax.annotate('', xy=(0.8, 0.8 * np.tan(epsilon)),
                xytext=(0.5, 0.5 * np.tan(epsilon)),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

    # Movement arrows on equator (different spacing)
    ax.annotate('', xy=(0.85, -0.15), xytext=(0.55, -0.15),
                arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

    ax.text(0.7, -0.35, 'Faster', fontsize=7, ha='center', color='blue')
    ax.text(0.65, 0.5, 'Same\nmotion', fontsize=7, ha='center', color='red')

    # Legend
    ax.legend(loc='lower left', fontsize=8)

    # Note
    ax.text(0, -2.5, 'Near equinoxes: small ecliptic motion\n'
            + 'projects to large equator motion',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-2.8, 2.8)
    ax.set_ylim(-3, 2.5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'obliquity-effect', chapter=15)


def mean_vs_apparent():
    """Diagram comparing mean solar time to apparent solar time."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 4))

    # Timeline
    hours = np.arange(0, 25)

    # Mean solar day (uniform)
    ax.axhline(2, color='blue', linewidth=2)
    for h in hours:
        ax.plot(h, 2, '|', color='blue', markersize=10, markeredgewidth=2)
    ax.text(-1, 2, 'Mean solar\ntime (clock)', fontsize=9, ha='right', va='center',
            color='blue')

    # Apparent solar day (varies)
    # On a day when Sun is 10 minutes slow
    ax.axhline(1, color='red', linewidth=2)
    for h in hours:
        # Offset by equation of time
        offset = 10/60  # 10 minutes
        ax.plot(h + offset, 1, '|', color='red', markersize=10, markeredgewidth=2)
    ax.text(-1, 1, 'Apparent solar\ntime (sundial)', fontsize=9, ha='right',
            va='center', color='red')

    # Highlight noon
    ax.axvline(12, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax.text(12, 2.5, 'Noon (clock)', fontsize=8, ha='center', color='blue')
    ax.text(12 + 10/60, 0.5, 'Noon (Sun)', fontsize=8, ha='center', color='red')

    # Difference arrow
    ax.annotate('', xy=(12 + 10/60, 0.7), xytext=(12, 0.7),
                arrowprops=dict(arrowstyle='<->', color='green', lw=2))
    ax.text(12 + 5/60, 0.3, 'Equation\nof time', fontsize=8, ha='center', color='green')

    ax.set_xlim(-2, 25)
    ax.set_ylim(-0.5, 3)
    ax.set_xticks([0, 6, 12, 18, 24])
    ax.set_xticklabels(['0h', '6h', '12h', '18h', '24h'])
    ax.set_xlabel('Hour', fontsize=10)
    ax.set_yticks([])

    save_figure(fig, 'mean-vs-apparent', chapter=15)


if __name__ == "__main__":
    equation_of_time_graph()
    analemma()
    eccentricity_effect()
    obliquity_effect()
    mean_vs_apparent()
